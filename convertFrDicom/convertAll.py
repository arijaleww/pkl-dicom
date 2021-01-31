import pydicom as dicom
import os
import cv2
import PIL # optional
# choose image format
print('1. PNG \n2. JPG \n3. TIFF ')
choose = eval(input('Pilihan Format = '))
# Specify the .dcm folder path
folder_path = "stage_1_test_images"
# Specify the output jpg/png folder path
jpg_folder_path = "JPG_test"
png_folder_path = "PNG_test"
tiff_folder_path = "TIFF_test"
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    if choose == 1:
        image = image.replace('.dcm', '.jpg')
        cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    elif choose == 2:
        image = image.replace('.dcm', '.png')
        cv2.imwrite(os.path.join(png_folder_path, image), pixel_array_numpy)
    elif choose == 3:
        image = image.replace('.dcm', '.tiff')
        cv2.imwrite(os.path.join(tiff_folder_path, image), pixel_array_numpy)
    
    if n % 50 == 0:
        print('{} image converted'.format(n))