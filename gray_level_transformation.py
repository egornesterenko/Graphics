from PIL import Image
from pylab import *
import numpy as np
from numpy import array


def negative(img_arr):
    img = 255 - img_arr
    return img


def clamp(img, start_end):
    min_, max_ = start_end
    range_ = max_ - min_
    img = np.asarray(range_ / 255 * img + min_).astype(np.uint8)
    return img


def main(file):
    img = array(Image.open(f'images/{file}'))
    negative_image = Image.fromarray(negative(img))
    clamp_image = Image.fromarray(clamp(img, (100, 200)))
    negative_image.show()
    clamp_image.show()


if __name__ == '__main__':
    main('img1.jpg')
