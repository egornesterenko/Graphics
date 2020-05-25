import cv2
from skimage import img_as_int, img_as_ubyte
from PIL import Image
import scipy.ndimage.filters as flt
import numpy as np


def show(*images):
    for img in images:
        img.show()


def main(file):
    img_gray = img_as_int(cv2.imread(f'images/{file}', 0))

    prewitt_vertical = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])
    prewitt_horizontal = prewitt_vertical.swapaxes(0, 1)

    prewitt_vertical_img = Image.fromarray(flt.convolve(img_gray, prewitt_vertical))
    prewitt_horizontal_img = Image.fromarray(flt.convolve(img_gray, prewitt_horizontal))

    show(prewitt_vertical_img, prewitt_horizontal_img)


if __name__ == '__main__':
    main('img2.jpg')
