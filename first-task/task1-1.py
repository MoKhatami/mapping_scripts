import cv2
import numpy as np

image = cv2.imread("first1.png")
template = cv2.imread("second.png")

result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)
print(result)
print(np.unravel_index(result.argmax(),result.shape))
