import albumentations as A
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tools import getAugmentedImage
import pathlib

i = 14

img_path = sorted(list(pathlib.Path("lavender_dataset/lavender_images").glob("*.jpg")))
mask_path = sorted(list(pathlib.Path("lavender_dataset/lavender_masks").glob("*.png")))

for img, mask in zip(img_path, mask_path):
    getAugmentedImage(img, mask, n=10)
    print(i)
    i += 1