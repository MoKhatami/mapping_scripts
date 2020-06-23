import numpy as np
from PIL import Image

im_big = Image.open(r"/Users/mokha/Sites/mapping_scripts/first1.png")
im_small = Image.open(r"/Users/mokha/Sites/mapping_scripts/first2.png")


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


print(find_matches(im_big, im_small))
