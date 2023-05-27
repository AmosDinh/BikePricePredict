import os

for file in os.listdir('data/bicycles_all_keep_nondupes4/'):
    if ' ' in file:
        print(file)

for file in os.listdir('data/bicycles_all_keep_nondupes4/'):
    # remove file if condition is met
    if 'Steuern' in file:
        os.remove('data/bicycles_all_keep_nondupes4/'+file)