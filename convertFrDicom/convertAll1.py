#using matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pydicom as dicom

# Specify the output jpg/png/tiff folder path
images_path = "image-00000.dcm"

ds = dicom.dcmread(images_path)

plt.axis('off')
plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
# image_show = mpimg.imread(images_path)
# plt.imshow(image_show)
plt.show()

plt.savefig('plt-image-00000.png', bbox_inches='tight', pad_inches=0)
plt.savefig('plt-image-00000.jpg', bbox_inches='tight', pad_inches=0)
plt.savefig('plt-image-00000.tiff', bbox_inches='tight', pad_inches=0)

