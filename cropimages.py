import cv2
import numpy as np
import os

# Function to display an image using OpenCV
def show_image(image, title='Image'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to convert YOLO annotations to pixel coordinates
def yolo_to_pixel(annotations, image_shape):
    image_height, image_width, _ = image_shape
    
    x_center = annotations[1]
    y_center = annotations[2]
    width = annotations[3]
    height = annotations[4]
    x_min = int((x_center - width / 2) * image_width)
    y_min = int((y_center - height / 2) * image_height)
    x_max = int((x_center + width / 2) * image_width)
    y_max = int((y_center + height / 2) * image_height)
    
    return x_min, y_min, x_max, y_max

# Directory paths
image_dir = "train/images"
label_dir = "train/labels"
output_dir = "cropped"

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through image files
for image_file in os.listdir(image_dir):
    if image_file.endswith(".jpg"):
        # Load image
        image_path = os.path.join(image_dir, image_file)
        image = cv2.imread(image_path)
        
        # Load corresponding label file
        label_file = os.path.splitext(image_file)[0] + ".txt"
        label_path = os.path.join(label_dir, label_file)
        
        # Read annotations from label file
        with open(label_path, "r") as file:
            lines = file.readlines()
        
        # Process each annotation
        for line in lines:
            annotations = np.array(line.strip().split(" "), dtype=np.float32)
            
            # Convert YOLO annotations to pixel coordinates
            x_min, y_min, x_max, y_max = yolo_to_pixel(annotations, image.shape)
            
            # Crop the image
            cropped_image = image[y_min:y_max, x_min:x_max]
            
            # Save the cropped image
            output_file = os.path.join(output_dir, os.path.splitext(image_file)[0] + f"_cropped_{lines.index(line)}.jpg")
            cv2.imwrite(output_file, cropped_image)
