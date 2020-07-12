# To use this script, configure your interpreter to use python3

import numpy as np
import json
import os
import glob
import base64

from matplotlib.pyplot import imread
from os import path
from io import BytesIO
from PIL import Image


#This function returns the origin of the label mask
def bbox2(img):
    rows = np.any(img, axis=1)
    cols = np.any(img, axis=0)
    try:
        rmin, rmax = np.where(rows)[0][[0, -1]]
        cmin, cmax = np.where(cols)[0][[0, -1]]
    except IndexError:
        # NOTE: Not sure this is the right decision on what to return for blank mask
        rmin, rmax = (0,0)
        cmin, cmax = (0,0)
    return (rmin,rmax+1), (cmin,cmax+1)



#create a file directory of the labelbox JSONs
files = []
path = 'labelbox'

#iterate over JSONS and print filenames
for filename in glob.glob(os.path.join(path, '*.json')): #only process .JSON files in folder.]\
    #open each JSON file
    with open(filename, encoding='utf-8', mode='r') as currentFile:
        data = currentFile.read()
        keyword = json.loads(data)
        files.append(keyword)


for file in files:

    # To get the instanceURI (or any element) from the labelbox JSON,
    # you need to navigate the lists and dicts of the file
    uri = file[1]['Label']['objects'][0]['instanceURI']
    print(uri)

    # Use the URI to extract a numpy image array from the server, put the array in mask_img
    print('\t * Downloading mask image from server')
    mask_img = imread(uri)

    # Create cropped, alpha-masked image feature
    (rmin,rmax),(cmin,cmax) = bbox2(mask_img[:,:,3])
    img_masked = np.zeros((rmax-rmin,cmax-cmin,4), dtype=np.uint8)
    img_masked[:,:,3] = mask_img[slice(rmin,rmax), slice(cmin,cmax), 3]

    # Use the numpy image array to find the origin
    origin = bbox2(mask_img)

    # Use the cropped image to create the base64 string that represents the image
    pil_img = Image.fromarray(np.uint8(img_masked))
    buff = BytesIO()
    pil_img.save(buff, format="PNG")
    data = base64.b64encode(buff.getvalue()).decode("utf-8")

    #print origin and then print the base64 string
    print(origin)
    print(data)