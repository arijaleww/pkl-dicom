from pydicom.uid import ImplicitVRLittleEndian
import PIL.Image
import cv2
from pydicom import dcmread
from pydicom.encaps import encapsulate
from pydicom.uid import JPEG2000

import matplotlib.pyplot as plt

PIL.Image.MAX_IMAGE_PIXELS = None
im_source = 'MicroDicomimage-00000.tif'
im_name = im_source.replace('.tif' , '')
im = PIL.Image.open(im_source)
im.save(im_name + '.j2k', irreversible=False) 

# Template file or whatever
ds = dcmread('CT_small.dcm')
with open((im_name + '.j2k'), 'rb') as f:
    # Image is only a single frame
    ds.PixelData = encapsulate([f.read()])

img = cv2.imread(im_source)
arr = img

ds.file_meta.TransferSyntaxUID = ImplicitVRLittleEndian
ds.Rows, ds.Columns, dummy = arr.shape
ds.PhotometricInterpretation = "MONOCHROME1"
ds.SamplesPerPixel = 1
ds.BitsStored = 8
ds.BitsAllocated = 8
ds.HighBit = 7
ds.PixelRepresentation = 0
ds.save_as(im_name + '_tifresult.dcm')

# plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
# plt.show()