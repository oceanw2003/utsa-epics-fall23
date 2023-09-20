import os

folder_path = "C:\\Users\\ocean\\OneDrive\\Desktop\\Files\\UTSA\\UTSA Classes and Resourses\\Fall 2023\\EGR1352 EPICS\\50 Images"  # Replace this with your actual folder path
new_name_prefix = "C300"  # You can change this prefix if you want

# Get a list of all files in the folder
file_list = os.listdir(folder_path)
image_files = [file for file in file_list if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Sort the image files to ensure sequential renaming
image_files.sort()

# Rename the files sequentially
for index, old_name in enumerate(image_files, start=1):
    file_extension = os.path.splitext(old_name)[1]
    new_name = f"{new_name_prefix}_{index:03d}{file_extension}"
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed {old_name} to {new_name}")

print("Renaming complete!")
