from PIL import Image
import os

folder_path = '/Users/aur316/Pictures/bck'
output_folder = '/Users/aur316/Pictures/bck64Blur'

if not os.path.exists(output_folder):
    os.makedirs(output_folder) 

for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        img = img.resize((640, 640), Image.Resampling.LANCZOS)
        img.save(os.path.join(output_folder, filename))

print("All images have been resized and saved to", output_folder)
# inditó kód python3 resize_images.py