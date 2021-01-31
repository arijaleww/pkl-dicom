import PIL.Image
import cv2
from pydicom import dcmread
from pydicom.encaps import encapsulate
from pydicom.uid import JPEG2000

import matplotlib.pyplot as plt

PIL.Image.MAX_IMAGE_PIXELS = None
im = PIL.Image.open('image-00001.tiff')
im.save('image-00001.j2k', irreversible=False) 

# Template file or whatever
ds = dcmread('CT_small.dcm')
with open('image-00001.j2k', 'rb') as f:
    # Image is only a single frame
    ds.PixelData = encapsulate([f.read()])

img = cv2.imread("image-00001.j2k")
arr = img
ds.Rows, ds.Columns, dummy = arr.shape
ds.file_meta.TransferSyntaxUID = JPEG2000
# Set other image pixel module elements as required
ds.save_as('image-00001.dcm')

plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
plt.show()