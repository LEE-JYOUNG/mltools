"""
A toolkit for operations that images releated,
such as cropping, reading, exchanging etc.
"""

import numpy as np

TYPE_PYTHON_LIST = 0
TYPE_NUMPY_LIST = 1

def convert_to_grayscale(source_image=None, target_image=None, save_format=None, save_path=None):
    """
    To conver a colorful image to grayscale image.

    @param source_image: original image which need to be converted. type[PIL Image].

    @param target_image: target image file path, type[string].

    @param save_format: optional param, if not set up, to be same with original image. type[string].

    @param save_path: optional param, if it's setted up with a path string, save the new image according the path. type[string].

    @return: void.
    """
    # TO BE IMPLEMENTED.


def crop_image(source_image=None, shape=None, save_format=None, save_path=None):
    """
    To crop an image as the defined size(shape).

    @param source_image: original image which need to be cropped. type[PIL Image].

    @param shape: what size you want to execute in cropping. it's a tuple format like this : (left, top, right, bottom).
                    after cropped, the new image size is (width:(right - left), height:(bottom - top)).
                    type[tutple].

    @param save_format: optional param, if not set up, to be same with original image. type[string].

    @param save_path: optional param, if it's setted up with a path string, save the new image according the path. type[string].

    @return: cropped image. type[PIL Image].
    """
    # TO BE IMPLEMENTED.

def convert_images_to_nparray_by_PIL(source_images=[], dtype=np.int64, flatten=True):
    """
    To conver the pixels of image to a numpy array.

    @param source_images: an array which contains some PIL datas.
                            FOR EXAMPLE:
                            pic1 = Image.open("...")
                            pic2 = Image.open("...")

                            data1 = pic1.load()
                            data2 = pic2.load()

                            nparray_pixels = convert_images_to_nparray_by_PIL([data1, data2], dtype=np.int64, flatten=True)

                            @return : [[pixel1_R, pixel1_G, pixel1_B, pixel2_R, pixel2_G, pixel2_B, ... pixel_last_R, pixel_last_G, pixel_last_B], #data1
                                       [pixel1_R, pixel1_G, pixel1_B, pixel2_R, pixel2_G, pixel2_B, ... pixel_last_R, pixel_last_G, pixel_last_B]  #data2 ]

    @param dtype: numpy type of the array for returning.

    @param flatten: whether flatten the array, if False the result will likes this
                    [[[pixel1_R, pixel1_G, pixel1_B],
                     ...
                     [pixel_last_R, pixel_last_G, pixel_last_B]],
                     # data1
                     [[pixel1_R, pixel1_G, pixel1_B],
                     ...
                     [pixel_last_R, pixel_last_G, pixel_last_B]]
                     data2
                    ]
                    and the shape is [2, (image_width * image_heigh), 3] (if bands is 'RGB').


    @return : a numpy array that contains all the pixels data.
    """
    # TO BE IMPLEMENTED.

def convert_images_to_nparray_by_filenames(source_images=[], dtype=np.int64, flatten=True):
    """
    To conver the pixels of images to a numpy array.

    to see details pls checkout the 'imagetools.convert_images_to_nparray_by_PIL'

    @param source_images: an array which contains some image file paths.
    """
    # TO BE IMPLEMENTED.