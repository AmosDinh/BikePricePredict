import os
import shutil
from PIL import Image

def add_to_dict(dict, image_path_str_list):
    for image2s in image_path_str_list:
        image2 = image2s.split("\\")[-1] + image2s.split("/")[-1]

        price2 = (image2.split("_")[1].split("‒")[0]+'X').replace('.X','').replace('X','')
        if price2.count('.') > 1:
            price2 = price2.replace('.', '', 1)

        if price2 not in dict.keys():
            dict[price2] = []
        dict[price2].append(image2s)

    return dict
    

def merge_folders(folder1, folder2, copytofolder, use_csv):
    # Create a new folder called "merged_chairs"
    if not os.path.exists(copytofolder):
        os.makedirs(copytofolder)
    
    # Get all images in both folders
    images1 = [ str(os.path.join(folder1, image)) for image in os.listdir(folder1) if image.endswith(".jpg")]

    images2 = [ str(os.path.join(folder2, image)) for image in os.listdir(folder2) if image.endswith(".jpg")]

    d = {}
    d = add_to_dict(d, images1)
    d = add_to_dict(d, images2)
    
    keep = set()
    remove = set()

    

    print(len(d))
    if not use_csv:
        with open('a.txt','a+', encoding="utf-8") as f:

            for key, value in d.items():
                
                images = {image:Image.open(image) for image in value}
                
                
                for imagepath, image in images.items():
                    
                    if imagepath in keep:
                        continue
                    for imagepath2, image2 in images.items():
                        if imagepath2 in keep:
                            continue
                        if imagepath == imagepath2:
                            continue
                        if image == image2:
                            print('same', len(keep))
                            if any(c.isalpha() for c in imagepath):
                                keep.add(imagepath)
                                remove.add(imagepath2)
                                f.write(imagepath2+'\n')
                            else:
                                keep.add(imagepath2)
                                remove.add(imagepath)
                                f.write(imagepath+'\n')
                            f.flush()
                
                        # if img1 == img2:
                        #     # If the images are identical, keep the one with letters in the name
                        #     if any(c.isalpha() for c in image1):
                        #         images2.remove(image2)
                        #     else:
                        #         images1.remove(image1)
    
    with open('a.txt','r', encoding="utf-8") as f:
        # add to remove
        for line in f:
            remove.add(line.strip())
                
    
    # Copy all remaining images from both folders to the new folder
    all = set()
    for key, value in d.items():
        all.update(value)
    
    keep = all - remove

    for image in keep:
        # Rename the image if it has a dash in the filename
        new_image_name = image.replace(".‒", "")
        new_image_name = new_image_name.split("\\")[-1]
        shutil.copy(image, os.path.join(copytofolder, new_image_name))


if __name__ == "__main__":
    copytofolder = "crawlers/fahrrad_google/images_removed_duplicates"
    merge_folders("crawlers/fahrrad_google/images", "crawlers/fahrrad_google/images_cloned", copytofolder,use_csv=False)