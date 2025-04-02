import os
import shutil

def organise_files_by_type(folder_path):
    # get all files in folder
    files = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    # loop through each file
    for file in files:
        # get the file extension 
        file_extension = file.split('.')[-1].lower()

        # create a folder for the file type if it doesn't exist
        type_folder = os.path.join(folder_path, file_extension)
        if not os.path.exists(type_folder):
            os.makedirs(type_folder)

        # move the file to the appropriate folder
        shutil.move(os.path.join(folder_path, file), os.path.join(type_folder, file))
    print("Files organised by type successfully.")

# Example usage
folder_to_organize = "./test_folder"
organise_files_by_type(folder_to_organize)