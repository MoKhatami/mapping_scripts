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


#create image directory
directories = "overlap"

#create directory for JSON files from supervisely
data_dir = os.path.join('.','Book of Fortresses','Book of Fortresses')
ann_dir = os.path.join(data_dir,'ann')
ann_list = glob.glob(os.path.join(ann_dir,'*.json'))

#method to check for image overlap
def match(big, small):
    #convert images to arrays
    #convert images to arrays
    arr_h = np.asarray(big) #forms pixel array of container
    arr_n = np.asarray(small) #forms pixel array of label
    #ckb9l8t9x13rh0yd1dluf8y5x.png ckb9mmzok16kp0yejgwly0tz5.png
    #ckb9l8t9x13rh0yd1dluf8y5x.png ckb9lafog00d90ycqarsxdvyh.png
    arr_hOnes = np.where(arr_h > 0, 1, arr_h) #set any values that are not 0 in container array to 1 for easy comparison
    arr_nOnes = np.where(arr_n > 0, 1, arr_n) #set any values that are not 0 in label array to 1 for easy comparison
    freq_h = np.count_nonzero(arr_hOnes == 1) #container pixels
    freq_n = np.count_nonzero(arr_nOnes == 1) #label pixels
    print(arr_hOnes)
    print(arr_nOnes)
    arr_and = arr_hOnes & arr_nOnes #find where overlap is
    freq_and = np.count_nonzero(arr_and == 1)
    print(freq_h, freq_n, freq_and) #pixels covered by container, label, overlap respectively
    if((freq_n + 100000 < freq_and) & (freq_n - 100000 > freq_and)):
        return 1  #if overlapped region is within 100,000 pixels of the label, then we guess that this container holds this label
    # if(freq_and > 0):
    #     return 1
    
    #print(arr_and)



    # arr_h = np.where(arr_h<1, np.random.normal(), arr_h) 
    # arr_n = np.where(arr_n<1, np.random.normal(), arr_n)
    
    
    
    # print(arr_h)
    # print(arr_n)
    # print(arr_h.shape[:2])
    # print(arr_n.shape[:2])

    # y_h, x_h = arr_h.shape[:2]
    # y_n, x_n = arr_n.shape[:2]

    # xstop = x_h - x_n + 1
    # ystop = y_h - y_n + 1

    # matches = []
    # for xmin in range(0, xstop):
    #     for ymin in range(0, ystop):
    #         xmax = xmin + x_n
    #         ymax = ymin + y_n

    #         arr_s = arr_h[ymin:ymax, xmin:xmax]     # Extract subimage
    #         arr_t = (arr_s == arr_n)                # Create test matrix
    #         print(arr_s)
    #         print(arr_t)
    #         print((arr_s == arr_h).all(1).any())
    #         if (arr_s == arr_h).all(1).any():                         # find if array contains other array
    #             print(big, small)
    #             print()
    #             matches.append((xmin, ymin))
    #         if(arr_h == arr_n).all():
    #            return ("Identical Image")
            

    # return matches
    # container = np.asarray(big)
    # object = np.asarray(small)

    # overlap = container == object

    # return overlap


def main():

    #iterate over image directory
    img_dir = []
    for root, dirs, files in os.walk(directories):
        #print out files
        for j in range(len(files)): #iterate through all files and compare every image to every other image; NOTE: change this for loop for more efficiency by never repeating comparisons
            for k in range(len(files)):
                im = Image.open("overlap/" + files[j])
                im2 = Image.open("overlap/" + files[k])
                result = match(im, im2) #run match function on two images
                print(result)
                if(result == 1):
                    img_dir.append(files[j] + "  " + files[k]) # add container image name + label image name to a list
                
                
                print(files[j], files[k]) #prints two current images to be compared
                print(img_dir) #prints current list of images that have been compared and a match has been found

    # for i in range(len(img_dir) - 1):
    #     print(match(img_dir[i], img_dir[i+1]))


    #iterate over JSON directory
    for ann_path in ann_list:
        print(ann_path)
        with open(ann_path,'r') as f:
            annotations = json.load(f)

main()





#['ckb9l8t9x13rh0yd1dluf8y5x.png  ckb9l8t9x13rh0yd1dluf8y5x.png', 'ckb9l8t9x13rh0yd1dluf8y5x.png  ckb9mofv500270yeg7or7d9vl.png', 'ckb9l8t9x13rh0yd1dluf8y5x.png  ckb9mmzok16kp0yejgwly0tz5.png', 'ckb9l8t9x13rh0yd1dluf8y5x.png  ckb9lafog00d90ycqarsxdvyh.png', 'ckb9l8t9x13rh0yd1dluf8y5x.png  ckb9l711v00bo0ycqfrmq6wf1.png', 'ckb9l8t9x13rh0yd1dluf8y5x.png  ckb9l5kf1127n0yd8eymzhe9x.png', 'ckb9l8t9x13rh0yd1dluf8y5x.png  ckb9l7tpa15q00yej6ebedo8y.png', 'ckb9iynvu14cb0yejd2wi8bjn.png  ckb9iynvu14cb0yejd2wi8bjn.png', 'ckb9iynvu14cb0yejd2wi8bjn.png  ckb9iy95614bn0yej5c8tb167.png', 'ckb9iynvu14cb0yejd2wi8bjn.png  ckb9mevf714ja0yd18i807unp.png', 'ckb9iynvu14cb0yejd2wi8bjn.png  ckb9iz7mo10sc0yd8auey7bmw.png', 'ckb9iynvu14cb0yejd2wi8bjn.png  ckb9j6qbu14ii0yej85q86pqr.png', 'ckb9iynvu14cb0yejd2wi8bjn.png  ckb9mc3gw00f50yeh44qeaoj2.png', 'ckb9rzxk901rz0y4tefxgf0da.png  ckb9rzxk901rz0y4tefxgf0da.png', 'ckb9rzxk901rz0y4tefxgf0da.png  ckb9m9q8p00dm0yeh8kjv46yp.png', 'ckb9rzxk901rz0y4tefxgf0da.png  ckb9jkimd13dj0yd25h3pc5oj.png', 'ckb9rzxk901rz0y4tefxgf0da.png  ckb9jgic812j10yd12pmmea8n.png', 'ckb9rzxk901rz0y4tefxgf0da.png  ckb9jfp4212ip0yd1h8yxdjxd.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9j5z0o112v0ydgdhbyaa9x.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9me4bp14is0yd13nr8a2ap.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9j72bn113r0ydghbnn9hio.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9j8i9b10yw0yd8d7xq0f58.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9mevf714ja0yd18i807unp.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9mfiv3152c0yd2bjlqgxtt.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9iz7mo10sc0yd8auey7bmw.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9j6e75113c0ydgfq8qcwyz.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9j6qbu14ii0yej85q86pqr.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9mc3gw00f50yeh44qeaoj2.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9mhum516ia0yejbw3eci70.png', 'ckb9j5z0o112v0ydgdhbyaa9x.png  ckb9j43g900au0yci96pw6i1p.png', 'ckb9lvjyw148f0yd14xla09bp.png  ckb9lvjyw148f0yd14xla09bp.png', 'ckb9lvjyw148f0yd14xla09bp.png  ckb9s5q6z01ub0y4t0slrd5b0.png', 'ckb9lvjyw148f0yd14xla09bp.png  ckb9lwfle004h0yehhjcmajd4.png', 'ckb9lvjyw148f0yd14xla09bp.png  ckb9lulwp14sc0yd24vuu85at.png', 'ckb9m9q8p00dm0yeh8kjv46yp.png  ckb9rzxk901rz0y4tefxgf0da.png', 'ckb9m9q8p00dm0yeh8kjv46yp.png  ckb9m9q8p00dm0yeh8kjv46yp.png', 'ckb9m9q8p00dm0yeh8kjv46yp.png  ckb9jkimd13dj0yd25h3pc5oj.png', 'ckb9m9q8p00dm0yeh8kjv46yp.png  ckb9jgic812j10yd12pmmea8n.png', 'ckb9m9q8p00dm0yeh8kjv46yp.png  ckb9jel6600ga0ycih5zuef9f.png', 'ckb9m9q8p00dm0yeh8kjv46yp.png  ckb9jjtwv00jd0yci5uzl1jfw.png', 'ckb9m9q8p00dm0yeh8kjv46yp.png  ckb9jfp4212ip0yd1h8yxdjxd.png']

