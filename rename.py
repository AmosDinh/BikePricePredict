import os
import uuid



for file in os.listdir('data/bicycles_all'):
    fullfilepath = 'data/bicycles_all'+'/'+file
    newfilepath = 'data/bicycles_all'+'/'+str(uuid.uuid3(uuid.NAMESPACE_URL,file)) + '_' + file.split('_')[-1]
    
    # rename   
    os.rename(fullfilepath, newfilepath)
        

   


