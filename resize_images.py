from PIL import Image
import os

# resize all images in a folder, and save them to a new folder
def resize_images(folder, new_folder, size):
    os.makedirs(new_folder, exist_ok=True)
    for file in os.listdir(folder):
        image = Image.open(folder+file)
        image = image.resize((size, size), Image.ANTIALIAS)
        image.save(new_folder+file)
        print(file)
    

# resize_images('data/bicycles/', 'data/bicycles_resized/', 256)
# resize_images('data/chairs/', 'data/chairs_resized/', 256)