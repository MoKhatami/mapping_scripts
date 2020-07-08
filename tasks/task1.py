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
import numpy.ma as ma
import cv2

#create image directory
directories = "overlap"

#create directory for JSON files from supervisely
data_dir = os.path.join('.','Book of Fortresses','Book of Fortresses')
ann_dir = os.path.join(data_dir,'ann')
ann_list = glob.glob(os.path.join(ann_dir,'*.json'))

#method to check for image overlap
def match(big, small):
    #convert images to arrays
    #convert images to arrays
    arr_h = np.asarray(big)
    arr_n = np.asarray(small)
    # arr_h = np.where(arr_h<1, np.random.normal(), arr_h)
    # arr_n = np.where(arr_n<1, np.random.normal(), arr_n)



    # print(arr_h)
    # print(arr_n)
    print(arr_h.shape[:2])
    print(arr_n.shape[:2])

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
            print(arr_s)
            print(arr_t)
            print((arr_s == arr_h).all(1).any())
            if (arr_s == arr_h).all(1).any():                         # find if array contains other array
                print(big, small)
                matches.append((xmin, ymin))

            if(arr_h == arr_n).all():
               return ("Identical Image")

            return ("Different Images")

    return matches
    container = np.asarray(big)
    object = np.asarray(small)

    overlap = container == object

    return overlap


def main():

    #iterate over image directory
    img_dir = []
    for root, dirs, files in os.walk(directories):
        #print out files
        for j in range(len(files)):
            for k in range(len(files)):
                im = Image.open("overlap/" + files[j])
                im2 = Image.open("overlap/" + files[k])
                print(match(im, im2))
                img_dir.append(files[j])
                print(files[j], files[k])
                print()
            print(len(img_dir))

    # for i in range(len(img_dir) - 1):
    #     print(match(img_dir[i], img_dir[i+1]))


    #iterate over JSON directory
    for ann_path in ann_list:
        print(ann_path)
        with open(ann_path,'r') as f:
            annotations = json.load(f)

main()
