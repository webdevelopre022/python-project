import os

def rename_files(folder_path, new_base_name, file_extension):
    files = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]
    files.sort()  # Optional: sort files before renaming

    for count, filename in enumerate(files, start=1):
        new_name = f"{new_base_name}_{count}{file_extension}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f'Renamed: {filename} -> {new_name}')

if __name__ == "__main__":
    # Customize this section
    folder = input("Enter the folder path: ")
    base_name = input("Enter new base name: ")
    ext = input("Enter file extension (e.g., .txt, .jpg): ")

    rename_files(folder, base_name, ext)
  
