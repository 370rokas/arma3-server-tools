import os
import shutil

directory_source = "/home/steam/Steam/steamapps/workshop/content/107410/"
directory_dest = "/home/steam/arma3/mods/"
relative_path = "mods/"


def rename_to_lowercase(path):
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            old_dir_path = os.path.join(root, directory)
            new_dir_path = os.path.join(root, directory.lower())
            os.rename(old_dir_path, new_dir_path)
            print(f"Renamed folder: {old_dir_path} to {new_dir_path}")

        for file_name in files:
            old_file_path = os.path.join(root, file_name)
            new_file_name = file_name.lower()
            new_file_path = os.path.join(root, new_file_name)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed file: {old_file_path} to {new_file_path}")


# Create destination directory if it doesn't exist
if not os.path.exists(directory_dest):
    os.makedirs(directory_dest)
    print(f"Directory created: {directory_dest}")
else:
    print(f"Directory already exists: {directory_dest}")

# Delete old symlinks
for item in os.listdir(directory_dest):
    item_path = os.path.join(directory_dest, item)
    if os.path.islink(item_path):
        os.remove(item_path)
        print(f"Deleted symlink: {item_path}")

# Rename files/folders to lowercase for compat
rename_to_lowercase(directory_source)

# Create symlinks
for folder in os.listdir(directory_source):
    folder_path = os.path.join(directory_source, folder)
    if os.path.isdir(folder_path):
        folder_name = os.path.basename(folder_path)
        symlink_path = os.path.join(directory_dest, folder_name)
        os.symlink(folder_path, symlink_path)
        print(f"Created symlink: {symlink_path}")

# -mod param
cmdline = "-mod='"

for folder in os.listdir(directory_dest):
    folder_path = os.path.join(directory_dest, folder)
    if os.path.isdir(folder_path):
        folder_name = os.path.basename(folder_path)
        p = os.path.join(relative_path, folder_name)
        cmdline += p + ";"

cmdline += "'"

with open(directory_dest + "mods.txt", "w") as file:
    file.write(cmdline)

print(cmdline)
