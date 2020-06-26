from cv2 import cv2
import numpy as np
import os

for filename in os.listdir('piconha2_jpg'):
    if filename.endswith(".png") : 
         print(os.path.join(directory, filename))
        continue
    else:
        continue




image = cv2.imread("firstImage.png")
template = cv2.imread("secondImage.png")

result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
print(np.unravel_index(result.argmax(),result.shape))


