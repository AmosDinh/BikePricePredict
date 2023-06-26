import pickle
import numpy as np
import pathlib


train_embeddings = ['conv5_trainembds10000.pickle','conv5_trainembds20000.pickle',
                    'conv5_trainembds30000.pickle',
                    'conv5_trainembds40000.pickle',
                    'conv5_trainembds50000.pickle'
                    ]




train_paths = np.load('train_paths.npz')['data']


i = 0
for embedding_path in train_embeddings:
    stem =pathlib.Path(embedding_path).stem
    # create folder
    pathlib.Path(f'train_conv5_embeddings/{stem}').mkdir(parents=True, exist_ok=True)

    with open(embedding_path, 'rb') as f:
        my_object = pickle.load(f)
    
    for batch in my_object:
        for embedding in batch:
            np.save(f'train_conv5_embeddings/{stem}/{pathlib.Path(train_paths[i]).name}.npy', embedding)
            i+=1

        print(i)
            



train_embeddings = ['conv5_devembds1000.pickle'
                    ]
train_paths = np.load('dev_paths.npz')['data']

i = 0
for embedding_path in train_embeddings:
    stem =pathlib.Path(embedding_path).stem
    # create folder
    pathlib.Path(f'dev_conv5_embeddings/{stem}').mkdir(parents=True, exist_ok=True)

    with open(embedding_path, 'rb') as f:
        my_object = pickle.load(f)
    
    for batch in my_object:
        for embedding in batch:
            np.save(f'dev_conv5_embeddings/{stem}/{pathlib.Path(train_paths[i]).name}.npy', embedding)
            i+=1

        print(i)



train_embeddings = ['conv5_testembds1000.pickle'
                    ]
train_paths = np.load('test_paths.npz')['data']

i = 0
for embedding_path in train_embeddings:
    stem =pathlib.Path(embedding_path).stem
    # create folder
    pathlib.Path(f'test_conv5_embeddings/{stem}').mkdir(parents=True, exist_ok=True)
    with open(embedding_path, 'rb') as f:
        my_object = pickle.load(f)
    
    for batch in my_object:
        for embedding in batch:
            np.save(f'test_conv5_embeddings/{stem}/{pathlib.Path(train_paths[i]).name}.npy', embedding)
            i+=1

        print(i)