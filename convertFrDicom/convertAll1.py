#using matplotlib
import matplotlib.pyplot as plt
import pydicom as dicom
from pydicom.pixel_data_handlers import util
import os, cv2, numpy as np
import png
import PIL # optional

# choose image format
print('1. JPG \n2. PNG \n3. TIFF ')
choose = eval(input('Pilihan Format = '))

# Specify the .dcm folder path
folder_path = "stage_1_test_images"

# Specify the output jpg/png/tiff folder path
jpg_path = "JPG_test"
png_path = "PNG_test"
tiff_path = "TIFF_test"
images_path = os.listdir(folder_path)

for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    arr = ds.pixel_array
    if choose == 1:
        image = image.replace('.dcm', '.jpg')
        # apply modality
        arr = util.apply_modality_lut(arr, ds)
        arr = util.apply_voi_lut(arr, ds, index=0)

        cv2.imwrite(os.path.join(jpg_path, image), arr)

    elif choose == 2:
        image = image.replace('.dcm', '.png')
        shape = ds.pixel_array.shape

        # Convert to float to avoid overflow or underflow losses.
        image_2d = ds.pixel_array.astype(float)

        # Rescaling grey scale between 0-255
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0

        # Convert to uint
        image_2d_scaled = np.uint8(image_2d_scaled)

        # Write the PNG file
        with open(os.path.join(png_path,image), 'wb') as png_file:
            w = png.Writer(shape[1], shape[0], greyscale=True)
            w.write(png_file, image_2d_scaled)
        #cv2.imwrite(os.path.join(png_folder_path, image), pixel_array_numpy)
    elif choose == 3:
        image = image.replace('.dcm', '.tiff')
        
        cv2.imwrite(os.path.join(tiff_path, image), arr)
    
print('{} image converted'.format(n+1))