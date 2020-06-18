#from skimage import draw, io
import json
import os
from cv2 import cv2
import numpy as np
from PIL import Image


img = Image.open("firstImage.png").save("sample1.bmp")

image = cv2.imread("sample1.bmp")
template = image[30:40,30:40,:]

result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)

print(np.unravel_index(result.argmax(),result.shape))
