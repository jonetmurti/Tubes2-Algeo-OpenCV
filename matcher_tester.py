import os
import cv2
import matcher

def show_img(path):
    img = cv2.imread(path)
    print(img)
    cv2.imshow(path, img)
    cv2.waitKey()

image_path = input("Input image path:")
database_path = input("Input database path:")

try:
    os.path.isfile(image_path)
    os.path.isfile(database_path)
except Exception as e:
    print ('Error: ', e)

match_algo = int(input("Input matching algorithm path: \n1.Euclidean\n2.Cosine\n")) - 1

if (match_algo > 1):
    print("Algorithm not available!")
    exit

ma = matcher.Matcher(database_path)

print('Query image ==========================================')
print(image_path)
show_img(image_path)

names, match = ma.match(image_path, match_algo, topn=3)
print ('Result images ========================================')
for i in range(3):
    # we got cosine distance, less cosine distance between vectors
    # more they similar, thus we subtruct it from 1 to get match value
    print(names[i])
    print ('Match %s' % (match[i]))
    show_img(names[i])