import os

# Directory path
label_dir = "train/labels"

# Loop through label files
for label_file in os.listdir(label_dir):
    if label_file.endswith(".txt"):
        # Read the content of the label file
        with open(os.path.join(label_dir, label_file), "r") as file:
            lines = file.readlines()
        
        # Modify class value
        modified_lines = []
        for line in lines:
            parts = line.strip().split(" ")
            class_id = int(parts[0])
            if class_id == 3:
                parts[0] = "7"  # Change class from 1 to 0
            modified_lines.append(" ".join(parts) + "\n")
        
        # Write modified content back to the file
        with open(os.path.join(label_dir, label_file), "w") as file:
            file.writelines(modified_lines)
