import math
import numpy as np
import pickle
import extractor

# Matching algorithm enum
EUCLIDEAN = 0
COSINE = 1

class Matcher(object):
    def __init__(self, pickled_db_path="features.dsc"):
        with open(pickled_db_path, 'rb') as fp:
            self.data = pickle.load(fp)
        self.names = []
        self.matrix = []
        for k, v in self.data.items():
            self.names.append(k)
            self.matrix.append(v)
        self.matrix = np.array(self.matrix)
        self.names = np.array(self.names)

    def cos_cdist(self, vector):
        # getting cosine distance between search image and images database
        result = []
        for dsc in self.matrix:
            dot = 0
            dsc_squaresum = 0
            vec_squaresum = 0
            for i in range(0, len(dsc)):
                dot += dsc[i] * vector[i]
                dsc_squaresum += dsc[i] ** 2
                vec_squaresum += vector[i] ** 2

            cos = dot / (math.sqrt(dsc_squaresum) * math.sqrt(vec_squaresum))
            result.append(cos)

        return result

    def euclidean_cdist(self, vector):
        # getting euclidean distance between search image and images database
        result = []
        for dsc in self.matrix:
            squaresum = 0
            for i in range(0, len(dsc)):
                squaresum += (vector[i] - dsc[i]) ** 2

            eucl_dist = math.sqrt(squaresum)
            result.append(eucl_dist)

        return result

    def match(self, image_path, algorithm=EUCLIDEAN, topn=5):
        features = extractor.extract_features(image_path)

        if (algorithm == EUCLIDEAN):
            img_distances = self.euclidean_cdist(features)
        elif (algorithm == COSINE):
            img_distances = self.cos_cdist(features)

        # getting top n records
        nearest_ids = np.argsort(img_distances)[:-topn-1:-1]
        nearest_img_paths = [self.names[i] for i in nearest_ids]
        nearest_img_distances = [img_distances[i] for i in nearest_ids]

        return nearest_img_paths, nearest_img_distances
