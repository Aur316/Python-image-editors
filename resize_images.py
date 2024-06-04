from PIL import Image
import os

folder_path = '/home/aur316/Letöltések/bck'
output_folder = '/home/aur316/Letöltések/bck640'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)  # Javítva: output_before helyett output_folder

for filename in os.listdir(folder_path):
    if filename.endswith('.png'):
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        img = img.resize((640, 640), Image.ANTIALIAS)
        img.save(os.path.join(output_folder, filename))

print("All images have been resized and saved to", output_folder)
# inditó kód python3 resize_images.py