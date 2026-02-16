import os
import shutil

# file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"]
}


def organize_folder(path):
    if not os.path.exists(path):
        print("Folder does not exist.")
        return

    for file in os.listdir(path):

        file_path = os.path.join(path, file)

        # skip folders
        if os.path.isdir(file_path):
            continue

        _, extension = os.path.splitext(file)

        moved = False

        for folder, extensions in FILE_TYPES.items():
            if extension.lower() in extensions:

                target_folder = os.path.join(path, folder)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, file))
                moved = True
                break

        # if extension not found
        if not moved:
            other_folder = os.path.join(path, "Others")

            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, file))

    print("Files organized successfully!")


# run program
folder_path = input("Enter folder path to organize: ")
organize_folder(folder_path)
