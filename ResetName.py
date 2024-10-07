import os
import sys

def rename_parent_directory(new_name):
    # Directory containing the script
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # Directory containting the parent dir
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    
    # Constructs the new path by joining the directory part of the parent directory's path with the new name
    new_parent_dir = os.path.join(parent_dir, new_name)
    # Rename the parent directory
    os.rename(current_dir, new_parent_dir)

def rename_project_name(new_name):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    directory_to_rename = os.path.join(current_dir, "OpenGLBasicTemplate")

    new_project_dir = os.path.join(current_dir, new_name)
    os.rename(directory_to_rename, new_project_dir)

def update_premake_file(new_name):
    # Read the content of the premake file
    premake_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "premake5.lua")
    with open(premake_file_path, 'r') as file:
        content = file.read()

    # Replace occurence of the old name with new name
    new_content = content.replace("OpenGLBasicTemplate", new_name)

    # Write the updated content back to the file
    with open(premake_file_path, 'w') as file:
        file.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python OpenGLBasicTemplate\ResetName.py <new_name>")
        sys.exit(1)

    new_name = sys.argv[1]
    rename_project_name(new_name)
    update_premake_file(new_name)
    rename_parent_directory(new_name)

    print(f"Project name changed to \"{new_name}\" successfully")