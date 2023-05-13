from PIL import Image, ImageOps
import os



def resize_image(image, max_side_length):
    width, height = image.size

    # Set the maximum size for the larger dimension
    max_size = max_side_length

    # Calculate the new size of the image
    if width > height:
        new_width = max_size
        new_height = int(max_size * height / width)
    else:
        new_height = max_size
        new_width = int(max_size * width / height)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Create a new white image
    new_image = Image.new('RGB', (max_size, max_size), 'white')

    # Calculate the position of the resized image on the white image
    x = (max_size - new_width) // 2
    y = (max_size - new_height) // 2

    # Paste the resized image onto the white image
    new_image.paste(resized_image, (x, y))
    return new_image


errors = 0
# resize all images in a folder, and save them to a new folder
def resize_images(folder, new_folder, size, maintain_aspect_ratio):
    os.makedirs(new_folder, exist_ok=True)
    print(len(os.listdir(folder)))
    for i, file in enumerate(os.listdir(folder)):
        print(i, end='\r')
        try:
            image = Image.open(folder+file)
            # Get the bounding box of the non-zero regions in the image
            bbox = ImageOps.invert(image.convert('L')).getbbox()


            # Crop the image to the bounding box
            cropped_image = image.crop(bbox)

            if not maintain_aspect_ratio:
                image = cropped_image.resize((size, size), Image.ANTIALIAS)
            else:
                image = resize_image(cropped_image, size)
        except BaseException as error:
            print(error)
            print(errors)
            errors += 1
            continue 
        image.save(new_folder+file.replace('ÿ','').replace('ÿ',''))
    
    

# resize_images('data/bicycles_de/', 'data/bicycles_resized/', 1024, maintain_aspect_ratio=True)
# resize_images('data/bicycles_xxl/', 'data/bicycles_resized/', 1024, maintain_aspect_ratio=True)
# resize_images('data/chairs/', 'data/chairs_resized/', 1024, maintain_aspect_ratio=True)

resize_images('data/bicycles_all_keep_nondupes3/', 'data/bicycles_all_keep_nodupes4_resized/', 512, maintain_aspect_ratio=True)
