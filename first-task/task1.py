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


data_dir = os.path.join('.','Book of Fortresses','Book of Fortresses')
ann_dir = os.path.join(data_dir,'ann')
img_dir = os.path.join(data_dir,'img')
mask_dir = os.path.join(data_dir,'masked_features')

# Grabbed poly2mask function from:
# https://github.com/scikit-image/scikit-image/issues/1103#issuecomment-52378754

def poly2mask(vertex_row_coords, vertex_col_coords, shape):
    fill_row_coords, fill_col_coords = draw.polygon(vertex_row_coords, vertex_col_coords, shape)
    mask = np.zeros(shape, dtype=np.uint8)
    mask[fill_row_coords, fill_col_coords] = 255
    return mask

# https://docs.supervise.ly/data-organization/import-export/supervisely-format#bitmap
# Heeded a warning and changed `np.fromstring()` to `np.frombuffer()` and seems to work fine

def base64_2_mask(s):
    z = zlib.decompress(base64.b64decode(s))
    n = np.frombuffer(z, np.uint8)
    mask = cv2.imdecode(n, cv2.IMREAD_UNCHANGED)[:, :, 3]
    return mask

# Not using this one here, but including it for reference
def mask_2_base64(mask):
    img_pil = Image.fromarray(np.array(mask, dtype=np.uint8))
    img_pil.putpalette([0,0,0,255,255,255])
    bytes_io = io.BytesIO()
    img_pil.save(bytes_io, format='PNG', transparency=0, optimize=0)
    bytes = bytes_io.getvalue()
    return base64.b64encode(zlib.compress(bytes)).decode('utf-8')

try:
    os.mkdir(mask_dir)
except OSError:
    if not os.path.exists(mask_dir):
        sys.exit("Error creating: " + mask_dir)

ann_list = glob.glob(os.path.join(ann_dir,'*.json'))

im_big = Image.open(r"/Users/mokha/Sites/mapping_scripts/first-task/first1.png")
im_small = Image.open(r"/Users/mokha/Sites/mapping_scripts/first-task/first2.png")


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
