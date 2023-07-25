import albumentations as A
import cv2
import numpy as np
import matplotlib.pyplot as plt

def transform(image, mask):
    transform = A.Compose([
        A.ShiftScaleRotate(shift_limit=0.2, scale_limit=0.3, rotate_limit=50, p=0.5),
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.2),
    ])

    transformed = transform(image=image, mask=mask)
    transformed_image = transformed["image"]
    transformed_mask = transformed["mask"]

    return transformed_image, transformed_mask


def getAugmentedImage(img_path, mask_path, n=5):
    img = cv2.imread(str(img_path))
    mask = cv2.imread(str(mask_path))
    img_name = img_path.stem
    mask_name = mask_path.stem

    for i in range(n):
        transformed_image, transformed_mask = transform(image=img, mask=mask)
        
        cv2.imwrite(f"augmented_images/images/{img_name}_{i}.jpg", transformed_image)
        cv2.imwrite(f"augmented_images/masks/{mask_name}_{i}.png", transformed_mask)
