from PIL import Image, ImageOps
from tensorflow.image import resize
from tensorflow.keras.utils import save_img
import os

# resize all images in a folder, and save them to a new folder
def resize_images(folder, new_folder, size):
    os.makedirs(new_folder, exist_ok=True)
    print(len(os.listdir(folder)))
    errors =0 
    for i, file in enumerate(os.listdir(folder)):
        print(i, end='\r')
        try:
            image = Image.open(folder+file).convert("RGB")
            # Get the bounding box of the non-zero regions in the image
            bbox = ImageOps.invert(image.convert('L')).getbbox()


            # Crop the image to the bounding box
            cropped_image = image.crop(bbox)

            image = resize(cropped_image, size)
        
            
        except BaseException as error:
            print(error)
            print(errors)
            errors += 1
            continue 
        save_img(new_folder+file, image)
    
resize_images('keep_images/content/keep_images/', 'keep_images224/', (224,224))
resize_images('keep_images/content/keep_images/', 'keep_images448/', (448,448))
