from PIL import Image
import os

def convert_jpg_to_png(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(folder_path, png_filename)
            img.save(png_path, "PNG")
            print(f"Converted: {filename} -> {png_filename}")

if __name__ == "__main__":
    folder = input("Enter the folder path: ")
    convert_jpg_to_png(folder)
