import os
import shutil

# Define target directory (change this to the folder you want to organize)
TARGET_DIR = r"C:\Users\YourName\Downloads"  # Use raw string for Windows paths

# Define folder names by file type
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

def organize_files():
    for filename in os.listdir(TARGET_DIR):
        filepath = os.path.join(TARGET_DIR, filename)

        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()

            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    folder_path = os.path.join(TARGET_DIR, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(filepath, os.path.join(folder_path, filename))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(TARGET_DIR, 'Others')
                os.makedirs(other_path, exist_ok=True)
                shutil.move(filepath, os.path.join(other_path, filename))

if __name__ == "__main__":
    organize_files()
    print("File organization complete.")
  
