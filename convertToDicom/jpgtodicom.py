from pydicom.uid import ImplicitVRLittleEndian
from pydicom.dataset import Dataset, FileDataset
import cv2
import datetime
import matplotlib.pyplot as plt

# Create the metadata for the dataset
file_meta = Dataset()
file_meta.TransferSyntaxUID = ImplicitVRLittleEndian
file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2'
file_meta.MediaStorageSOPInstanceUID = '1.2.3'
file_meta.ImplementationClassUID = '1.2.3.4'

# Create the dataset
ds = FileDataset("image-00000.dcm", {}, file_meta=file_meta, preamble=b'\x00'*128)

# Add some of the data elements
ds.PatientName = "Dicom^Anony"
ds.PatientID = "123456"

# Set the transfer syntax
ds.is_little_endian = True
ds.is_implicit_VR = True

# Set creation date/time
dt = datetime.datetime.now()
ds.ContentDate = dt.strftime('%Y%m%d')
timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
ds.ContentTime = timeStr

# Read in the JPG file
img_source = "MicroDicomimage-00000.jpg"
img_name = img_source.replace('.jpg' , '')
img = cv2.imread(img_source)

# Get the numpy array
arr = img
print(arr.shape)

# (8-bit pixels, black and white)
ds.Rows, ds.Columns, dummy = arr.shape
ds.PhotometricInterpretation = "MONOCHROME1"
ds.SamplesPerPixel = 1
ds.BitsStored = 8
ds.BitsAllocated = 8
ds.HighBit = 7
ds.PixelRepresentation = 0

# Reassign back to the image data
ds.PixelData = arr.tobytes()

# Save DICOM

ds.save_as(img_name + "_jpgresult.dcm")

plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
plt.show()