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


#create image directory
directories = "./overlap"

#create directory for JSON files from supervisely
data_dir = os.path.join('.','Book of Fortresses','Book of Fortresses')
ann_dir = os.path.join(data_dir,'ann')
ann_list = glob.glob(os.path.join(ann_dir,'*.json'))

#method to check for image overlap
def match(big, small):
    #convert images to arrays
    container = np.asarray(big)
    object = np.asarray(small)

    overlap = container == object

    return overlap


def main():

    #iterate over image directory
    img_dir = []
    for root, dirs, files in os.walk(directories):
        #print out files
        for file in files:
            img_dir.append(file)
            print(file)
        print(len(img_dir))

    for i in range(len(img_dir) - 1):
        print(match(img_dir[i], img_dir[i+1]))


    #iterate over JSON directory
    for ann_path in ann_list:
        print(ann_path)
        with open(ann_path,'r') as f:
            annotations = json.load(f)

main()
