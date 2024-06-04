import os
from PIL import Image, ImageFilter

# Beállítások
input_folder = "/home/aur316/Letöltések/bck32"  # A mappa, ahol a képek találhatók
output_folder = "/home/aur316/Letöltések/bck32Blur"  # A mappa, ahová a képeket mentjük

# Kimeneti mappa létrehozása, ha nem létezik
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Végigmegyünk az input mappán és feldolgozzuk a képeket
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)
        
        # Blur effektus alkalmazása
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius=5))  # A 'radius' értékét növelheted vagy csökkentheted a kívánt blur erősségtől függően

        # Kép mentése az output mappába
        output_path = os.path.join(output_folder, filename)
        blurred_image.save(output_path)

        print(f"{filename} blurred and saved to {output_path}")
