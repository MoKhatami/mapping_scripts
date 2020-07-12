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



def main():
    #create directory
    files = []
    path = 'mapping_scripts/ann'

    #iterate over JSONS and print filenames
    for filename in glob.glob(os.path.join(path, '*.json')): #only process .JSON files in folder.]\
        print(filename)

        #open each JSON file
        with open(filename, encoding='utf-8', mode='r') as currentFile:
            data = currentFile.read()
            keyword = json.loads(data)
            files.append(keyword)

    for i in files:
        print(i)
    currentFile.close()

main()
