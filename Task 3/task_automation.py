import os
import shutil

# Folder paths
source_folder = "source"
destination_folder = "organized"

# Create folders if they don't exist
if not os.path.exists(source_folder):
    os.makedirs(source_folder)

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav"]
}

# Organize files
for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()
        moved = False

        for folder, extensions in file_types.items():
            if file_extension in extensions:
                folder_path = os.path.join(destination_folder, folder)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, file_name))
                print(f"Moved {file_name} to {folder}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(destination_folder, "Others")

            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f"Moved {file_name} to Others")

print("File organization completed successfully!")
