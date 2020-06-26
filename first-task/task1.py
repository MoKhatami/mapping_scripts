from skimage import draw
from skimage import io as skio
import numpy as np
import json
import os
import glob

from PIL import Image
import zlib
import io
import base64

img_dir = []
for filename in glob.glob('../../piconha2_jpg'):
    im=Image.open(filename)
    img_dir.append(im)
    print(len(img_dir))

data_dir = os.path.join('.','Book of Fortresses','Book of Fortresses')
ann_dir = os.path.join(data_dir,'ann')

ann_list = glob.glob(os.path.join(ann_dir,'*.json'))

for ann_path in ann_list:

    print(ann_path)

    # remove .json extension – should maybe use pathlib instead...
    img_filename = os.path.splitext(os.path.basename(ann_path))[0]
    # replace . with _ for mask subdirectory name
    mask_subdir = img_filename.replace('.','_')
    mask_subdir_path = os.path.join(mask_dir, mask_subdir)
    # remove .jpg extension
    img_name = os.path.splitext(img_filename)[0]
    img_path = os.path.join(img_dir, img_filename)

    img = skio.imread(img_path)

    try:
        os.mkdir(mask_subdir_path)
    except OSError:
        if not os.path.exists(mask_subdir_path):
            sys.exit("Error creating: " + mask_subdir_path)

    with open(ann_path,'r') as f:
        annotations = json.load(f)



def find_matches(big, small):
    arr_h = np.asarray(big)
    arr_n = np.asarray(small)

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
    print("made it")
    for filename in glob.glob('../piconha2_jpg'):
        print("im here")
        im=Image.open(filename)
        img_dir.append(im)
        print(len(img_dir))
        
    for i in range(len(img_dir) - 1):
        print(find_matches(img_dir[i], img_dir[i+1]))

main()


