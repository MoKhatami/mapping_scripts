from skimage import draw
from skimage import io as skio
import skimage
import numpy as np
from matplotlib.pyplot import imread
import json
import os
import glob
from os import path
from PIL import Image
import zlib
import io
import numpy.ma as ma
import cv2
import base64
import requests


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

def mask_2_base64(mask):
    img_pil = Image.fromarray(np.array(mask, dtype=np.uint8))
    img_pil.putpalette([0,0,0,255,255,255])
    bytes_io = io.BytesIO()
    img_pil.save(bytes_io, format='PNG', transparency=0, optimize=0)
    bytes = bytes_io.getvalue()
    return base64.b64encode(zlib.compress(bytes)).decode('utf-8')

#Label, objects, instanceURI
#create directory
files = []
filenames = []
path = 'labelbox'
map_dicts = []

#iterate over JSONS and print filenames
for filename in glob.glob(os.path.join(path, '*.json')): #only process .JSON files in folder.]\

    #open each JSON file
    with open(filename, encoding='utf-8', mode='r') as currentFile:
        data = currentFile.read()
        keyword = json.loads(data)
        files.append(keyword)

    filenames.append(filename)


#for i in files:
    #print(i['size']['height'])

label_box = files[0]
uri = label_box[1]['Label']['objects'][0]['instanceURI']
id = label_box[1]['Label']['objects'][0]['featureId']
print(uri)

print('\t * Downloading mask image from server')
# Delay just so we don't get kicked off of the server...
mask_img = imread(uri)

origin = bbox2(mask_img)

data = base64.b64encode(requests.get(uri).content)

print(origin)
print(data)
