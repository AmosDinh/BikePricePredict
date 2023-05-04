import os
import re

def rename(filename):
    pattern = r'(\d+\.\d{3})(?=\D|$)'
    return re.sub(pattern, lambda x: x.group().replace('.', ''), filename)


for file in os.listdir('data/chairs'):
  
    fileold = file
    file = rename(file)
    a, b, c = file.split('_') 
    c = c.replace('.jpg', '')
    filename = a + c + '_' + b + '.jpg'
    print(filename)
    # os.rename('data/chairs/'+fileold, 'data/chairs/'+filename)

# for file in os.listdir('data/bicycles'):
#     fileold = file
#     file = file.replace('ab ','')
#     file = file.replace('ab','')

#     if ".-" in file:
#         file = file.replace('.- ', '', 1).replace('.-', '', 1)
#     # if file.count('.') > 2:
#     #     file = file.replace('.', '', 1)
#     # name = file.replace(" ", "")

#     # price = name.split('_')[1]
#     # if price.count('.') > 1:
#     #     price = price.replace('.', '', 1).strip()
    
#     # # save file
    
#     # try:
#     #     name = name.split('_')[0]+'_'+name.split('_')[2]+"_"+price+".jpg"
#     # except:
#     #     name = name.split('_')[0]+"_"+price+".jpg"
#     file = rename(file)
#     file = file.replace(' ','')
#     print(file)
 
#     os.rename('data/bicycles/'+fileold, 'data/bicycles/'+file)

