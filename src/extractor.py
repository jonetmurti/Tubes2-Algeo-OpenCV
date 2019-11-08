import os
import cv2
import numpy as np
import pickle

def extract_features(image_path, vector_size=32):
    '''
    Feature extractor by Andrey Nikishaev modified for Python 3 by Ardi.
    https://medium.com/machine-learning-world/feature-extraction-and-similar-image-search-with-opencv-for-newbies-3c59796bf774
    '''
    image = cv2.imread(image_path)
    try:
        kaze = cv2.AKAZE_create()
        key = kaze.detect(image)
        key = sorted(key, key=lambda x: -x.response)[:vector_size]
        key, dsc = kaze.compute(image, key)
        dsc = dsc.flatten()
        needed_size = (vector_size * 64)
        if dsc.size < needed_size:
            dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    except cv2.error as e:
        print ('Error: ', e)
        return None

    return dsc

def batch_extract(images_path, pickled_db_path="features.dsc"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print ('Extracting features from image %s' % f)
        name = f
        result[name] = extract_features(f)
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        pickle.dump(result, fp)
