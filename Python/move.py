import os
import shutil

source_folder = "C:\\Users\\ocean\\OneDrive\\Desktop\\Files\\UTSA\\UTSA Classes and Resourses\\Fall 2023\\EGR1352 EPICS\\50 Images"  # Replace this with your source folder path
destination_base = "C:\\Users\\ocean\\OneDrive\\Desktop\\Files\\UTSA\\UTSA Classes and Resourses\\Fall 2023\\EGR1352 EPICS\\50 Images"  # Replace this with your destination base folder path
num_folders = 5  # Number of destination folders

# Create destination folders if they don't exist
for i in range(1, num_folders + 1):
    destination_folder = os.path.join(destination_base, f"Folder_{i}")
    os.makedirs(destination_folder, exist_ok=True)

# Move images to the destination folders
for index in range(1, 51):  # Assuming you have 50 images
    source_file = os.path.join(source_folder, f"C300_{index:03d}.jpg")  # Update the extension if needed
    destination_folder = os.path.join(destination_base, f"Folder_{(index - 1) % num_folders + 1}")
    destination_file = os.path.join(destination_folder, f"C300_{index:03d}.jpg")  # Update the extension if needed
    
    shutil.move(source_file, destination_file)
    print(f"Moved C300_{index:03d}.jpg to {destination_folder}")

print("Moving complete!")
