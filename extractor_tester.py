import os
import extractor

images_path = input("Input images path:")

try:
    os.path.isdir(images_path)
except Exception as e:
    print ('Error: ', e)

extractor.batch_extract(images_path)