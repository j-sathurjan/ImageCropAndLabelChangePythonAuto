import cv2
import numpy as np
import os

# Function to display an image using OpenCV
def show_image(image, title='Image'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load the YOLO annotations
annotations_file = r"train/labels/sa.txt"
annotations = np.loadtxt(annotations_file, delimiter=" ")

# Load the image
image_file = r"train/images/sa.jpg"
image = cv2.imread(image_file)
print(image.shape)
# Convert the YOLO annotations to pixel coordinates
image_height, image_width, _ = image.shape

x_center = annotations[1]
y_center = annotations[2]
width = annotations[3]
height = annotations[4]
x_min = int((x_center - width / 2) * image_width)
y_min = int((y_center - height / 2) * image_height)
x_max = int((x_center + width / 2) * image_width)
y_max = int((y_center + height / 2) * image_height)

print("x_min:", x_min)
print("y_min:", y_min)
print("x_max:", x_max)
print("y_max:", y_max)
# Crop the image
cropped_image = image[y_min:y_max, x_min:x_max]

# Show the cropped image
# show_image(cropped_image)


# Save the cropped image
output_dir = r"croped"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
output_file = os.path.join(output_dir, "cropped_image.jpg")
cv2.imwrite(output_file, cropped_image)