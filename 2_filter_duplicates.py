import os
from PIL import Image
import tqdm
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import shutil 

def process_images(folder_path1, folder_path2,savefolder):
    # Load all filenames in the path
    filenames1 = os.listdir(folder_path1)
    filenames2 = os.listdir(folder_path2)
    
    # Create a dictionary with key being the price and value the list of the images with that price
    images = {}
    for filename in filenames1 + filenames2:
        if filename.endswith('.jpg'):
            price = filename.split('_')[-1].split('.')[0]
            if price not in images:
                images[price] = []
            images[price].append(filename)
    
    # Load the images into memory using PIL
    #for price, image_list in tqdm.tqdm(list(images.items())):
    
    def worker(price,image_list):
        pil_images = []
        for image in image_list:
            if image in filenames1:
                pil_images.append(Image.open(os.path.join(folder_path1, image)))
            else:
                pil_images.append(Image.open(os.path.join(folder_path2, image)))
        
        # Compare the images against each other
        unique_images = []
        for i in range(len(pil_images)):
            is_unique = True
            for j in range(i+1, len(pil_images)):
                if pil_images[i] == pil_images[j]:
                    is_unique = False
                    break
            if is_unique:
                unique_images.append(image_list[i])
                pil_images[i] = None  # Exclude unique image from further comparison
        
        # Copy unique images to a new folder
        new_folder_path = savefolder
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        for image in unique_images:
            old_image_path = os.path.join(folder_path1, image) if image in filenames1 else os.path.join(folder_path2, image)
            new_image_path = os.path.join(new_folder_path, image)
            shutil.copy(old_image_path, new_image_path)
    
    # with ThreadPoolExecutor(max_workers=4) as executor:
    print(len(images.keys()))
    for _ in tqdm.tqdm(map(worker, images.keys(),images.values()), total=len(images.keys())):
        pass

process_images(r'data\bicycles_all_keep_nondupes3\data\bicycles_all_keep_nondupes3',r'data\bicycles_keep_half4\content\data\bicycles_all_keep', savefolder='data/bicycles_all_keep_nondupes4')