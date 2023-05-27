import os 
from PIL import Image
count = 0
def convert_to_jpg(filename):
        global count
        # print(filename)
        # check if file is jpg with PIL
        with Image.open(filename) as img:
            if img.format != 'JPEG':
                img.save(filename, 'JPEG')
            
            if ' EUR' in filename:
                os.rename(filename, filename.replace(' EUR', ''))
        # if 'i pore' in filename:
        #     os.remove(filename)
        #     print(count)
        # #     # split at + and take first part
        #     count +=1
        #     # os.rename(filename, filename.split('+')[0].strip() + '.jpg')
                

for file in os.listdir('images'):
    convert_to_jpg('images/' + file)

print(count)