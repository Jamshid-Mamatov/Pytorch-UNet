import rasterio
import matplotlib.pyplot as plt
import numpy as np
from skimage import exposure
import pathlib
import cv2

def readImg(path):

    for img_path in path.glob("*.tiff"):
        # get name and siffix
        name = img_path.stem
        suffix = img_path.suffix
        print(name, suffix)
        with rasterio.open(str(img_path)) as dataset:
            image_data = dataset.read()
        
        rgb_bands = [3, 2, 1]
        rgb_image = image_data[rgb_bands, :, : ]
        rgb_image = rgb_image.transpose(1, 2, 0)

        rgb_image = exposure.rescale_intensity(rgb_image)
 
        plt.imsave("lavender_dataset/lavender_image/{}.jpg".format(name), rgb_image)

path = pathlib.Path("lavender_dataset/lavender_images")
print(readImg(path))



    
# # Iterate over the files in the directory
# for filename in os.listdir(give the directory path):
# if filename.endswith(".tiff") or filename.endswith(".tif"):
# # Construct the full file path
# file_path = os.path.join(give the directory path, filename)

# # Open the TIF file using rasterio
# with http://rasterio.open(file_path) as dataset:
# # Read all bands of the TIF image
# image_data = http://dataset.read()

# # Choose the bands for the RGB image (e.g., bands 4, 3, and 2)
# rgb_bands = [4, 3, 2]
# rgb_image = image_data[rgb_bands, :, : ]

# # Transpose the image data to have the shape (height, width, bands)
# rgb_image = rgb_image.transpose(1, 2, 0)

# # Apply contrast stretching
# rgb_image_stretched = exposure.rescale_intensity(rgb_image)

# # Display the contrast-stretched RGB image
# plt.imshow(rgb_image_stretched)
# plt.title('Contrast-Stretched RGB Image - {}'.format(filename))
# plt.axis('off')
# plt.show()