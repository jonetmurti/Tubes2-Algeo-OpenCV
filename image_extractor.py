import os
import extractor

images_path = input("Input images path:")

try:
    os.path.isdir(images_path)
except Exception as e:
    print ('Error: ', e)

files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

extractor.batch_extract(images_path)