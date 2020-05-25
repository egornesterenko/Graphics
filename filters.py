from PIL import Image
import scipy.ndimage.filters as flt
import numpy as np


def get_noisy_images(noisy, kernel_grayscale):
    minimum = flt.minimum_filter(noisy, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
    maximum = flt.maximum_filter(noisy, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
    median = flt.median_filter(noisy, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)

    minimum_noisy = Image.fromarray(minimum)
    maximum_noisy = Image.fromarray(maximum)
    median_noisy = Image.fromarray(median)
    kernel_noisy = Image.fromarray(flt.convolve(noisy, kernel_grayscale))
    return minimum_noisy, maximum_noisy, median_noisy, kernel_noisy


def show(*images):
    for img in images:
        img.show()


def main(color_file, noisy_file):
    img_color = Image.open(f'images/{color_file}')

    img_grayscale = img_color.convert('L')

    kernel_color = np.ones((5, 5, 1)) / 25
    kernel_grayscale = np.ones((5, 5)) / 25

    filtered_color = flt.convolve(img_color, kernel_color)
    filtered_grayscale = flt.convolve(img_grayscale, kernel_grayscale)

    filtered_color_img = Image.fromarray(filtered_color)
    filtered_grayscale_img = Image.fromarray(filtered_grayscale)

    noisy = Image.open(f'images/{noisy_file}').convert('L')

    minimum_noisy, maximum_noisy, median_noisy, kernel_noisy = get_noisy_images(noisy, kernel_grayscale)

    show(filtered_color_img, filtered_grayscale_img, noisy, minimum_noisy, maximum_noisy, median_noisy, kernel_noisy)


if __name__ == '__main__':
    main('img1.jpg', 'img3.png')
