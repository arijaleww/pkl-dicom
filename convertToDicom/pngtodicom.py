from PIL import Image
import numpy as np
import pydicom
import matplotlib.pyplot as plt

ds = pydicom.dcmread('CT_small.dcm') # pre-existing dicom file for data acquisition
im_source = 'MicroDicomimage-00000.png'
im_name = im_source.replace('.png', '')
im_frame = Image.open(im_source) # the PNG file to be replace

if im_frame.mode == 'L':
    # (8-bit pixels, black and white)
    np_frame = np.array(im_frame.getdata(),dtype=np.uint8)
    ds.Rows = im_frame.height
    ds.Columns = im_frame.width
    ds.PhotometricInterpretation = "MONOCHROME1"
    ds.SamplesPerPixel = 1
    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7
    ds.PixelRepresentation = 0
    ds.PixelData = np_frame.tobytes()
    ds.save_as(im_name + '_pngresult_bw.dcm')
elif im_frame.mode == 'RGBA':
    # RGBA (4x8-bit pixels, true colour with transparency mask)
    np_frame = np.array(im_frame.getdata(), dtype=np.uint8)[:,:3]
    ds.Rows = im_frame.height
    ds.Columns = im_frame.width
    ds.PhotometricInterpretation = "RGB"
    ds.SamplesPerPixel = 3
    ds.BitsStored = 8
    ds.BitsAllocated = 8
    ds.HighBit = 7
    ds.PixelRepresentation = 0
    ds.PixelData = np_frame.tobytes()
    ds.save_as(im_name + '_pngresult_rgb.dcm')

# plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
# plt.show()