from tkinter.filedialog import askopenfilename

import cv2
import imageio
import numpy as np
from scipy.ndimage.filters import gaussian_filter as gf


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
    # It is a 2D array formula to convert image to gray scale


def dodge(front, back):
    final_sketch = front * 255 / (255 - back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    return final_sketch.astype("uint8")


img = askopenfilename()

img = imageio.v2.imread(img)  # To read the image
gray = rgb2gray(img)  # Convert to gray scale
i = 255 - gray
blur = gf(i, sigma=15)  # Convert to blur image
r = dodge(blur, gray)  # Convert to sketch

cv2.imwrite("sketch.png", r)
