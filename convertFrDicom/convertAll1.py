#using matplotlib
import matplotlib.pyplot as plt
import pydicom as dicom
from pydicom.pixel_data_handlers import util
import os, cv2, numpy as np
import png
import PIL # optional

# choose image format
# print('1. JPG \n2. PNG \n3. TIFF ')
# choose = eval(input('Pilihan Format = '))

# Specify the .dcm folder path
folder_path = "stage_1_test_images"

# Specify the output jpg/png/tiff folder path
jpg_path = "JPG_test"
png_path = "PNG_test"
tiff_path = "TIFF_test"
images_path = "CT_small.dcm"


ds = dicom.dcmread(images_path)
arr = ds.pixel_array
plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
plt.show()
