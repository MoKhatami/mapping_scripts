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
directories = "mapping_scripts/piconha2_jpg"

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
    

def main():
    #create directory
    files = []
    path = 'mapping_scripts/labelBox'

    #iterate over JSONS and print filenames
    for filename in glob.glob(os.path.join(path, '*.json')): #only process .JSON files in folder.]\
        print(filename)

        #open each JSON file
        with open(filename, encoding='utf-8', mode='r') as currentFile:
            data = json.load(currentFile)
            for ann in data:
                for obj in ann['Label']['objects']:
                    mask_id = obj['featureId']  #this is the featureId of this object
                    if('container' in obj['title']): #if the object is a container then add it to the container list
                        containers = []
                        containers.append(obj['featureId'])
                        print(containers)
            currentFile.close() #close the file 

  


main()




   





#6700 191812 76
#6700 21876 264
#6700 5024 132
#30080 35140 580
#38112 204612 1208
#38112 9944 132
#38112 69856 384
#72932 131672 516
#72932 20980 708
#75076 115124 904
#75076 2545448 75076