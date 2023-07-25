import pathlib
import matplotlib.pyplot as plt
import cv2
import numpy as np

# lavender_dataset/lavender_images
# lavender_dataset/lavender_masks

img_path = sorted(list(pathlib.Path("lavender_dataset/lavender_images").glob("*.jpg")))
mask_path = sorted(list(pathlib.Path("lavender_dataset/lavender_masks").glob("*.png")))

for img, mask in zip(img_path, mask_path):
    img_path = img.stem
    img_suffix = img.suffix
    mask_path = mask.stem
    mask_suffix = mask.suffix

    img = cv2.imread(str(img))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mask = cv2.imread(str(mask))
    # gray
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # save with matplitlib img_name = f"lavender_dataset/lavender_images/{img_path}{img_suffix}" mask_name = f"lavender_dataset/lavender_masks/{mask_path}{mask_suffix}" 
    img_name = f"lavender_dataset/lavender_images/{img_path}{img_suffix}"
    mask_name = f"lavender_dataset/lavender_masks/{mask_path}{mask_suffix}"
    plt.imsave(img_name, img)
    plt.imsave(mask_name, mask, cmap="gray")
