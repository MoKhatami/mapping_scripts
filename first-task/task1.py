from skimage import draw
from skimage import io as skio
import numpy as np
import json
import os
import glob
from os import path
from PIL import Image
import zlib
import io
import base64

directories = "./piconha2_jpg"
for root, dirs, files in os.walk(directories):
    print(files)
    img_dir.append(files)
    print(len(img_dir))

#create directory for JSON files from supervisely
data_dir = os.path.join('.','Book of Fortresses','Book of Fortresses')
ann_dir = os.path.join(data_dir,'ann')
ann_list = glob.glob(os.path.join(ann_dir,'*.json'))

#iterate over JSON files
for ann_path in ann_list:
    print(ann_path)
    with open(ann_path,'r') as f:
        annotations = json.load(f)


#method to check for image overlap
def find_matches(big, small):
    #convert images to arrays
    arr_h = np.asarray(big)
    arr_n = np.asarray(small)
    print(arr_h)

    y_h, x_h = arr_h.shape[:2]
    y_n, x_n = arr_n.shape[:2]

    xstop = x_h - x_n + 1
    ystop = y_h - y_n + 1

    matches = []
    for xmin in range(0, xstop):
        for ymin in range(0, ystop):
            xmax = xmin + x_n
            ymax = ymin + y_n

            arr_s = arr_h[ymin:ymax, xmin:xmax]     # Extract subimage
            arr_t = (arr_s == arr_n)                # Create test matrix
            if arr_t.all():                         # Only consider exact matches
                matches.append((xmin, ymin))

    return matches


def main():
    img_dir = []
    for root, dirs, files in os.walk(directories):
        #print out files
        for file in files:
            img_dir.append(files)
            print(files)
        print(len(img_dir))

    for i in range(len(img_dir) - 1):
        print(find_matches(img_dir[i], img_dir[i+1]))

main()
