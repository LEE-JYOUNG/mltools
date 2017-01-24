"""
A toolkit for operations that images releated,
such as cropping, reading, exchanging etc.
"""


def convert_to_gray_image(source_image=None, target_image=None):
    """
    To conver a colorful image to gray image.

    @param source_image: original image which need to be converted. type[PIL Image].

    @param target_image: target image file path, type[string].

    @return: void.
    """
    # TO BE IMPLEMENTED.


def crop_image(source_image=None, shape=None, save_path=None):
    """
    To crop an image as the defined size(shape).

    @param source_image: original image which need to be cropped. type[PIL Image].

    @param shape: what size you want to execute in cropping. it's a tuple format like this : (left, top, right, bottom).
                    after cropped, the new image size is (width:(right - left), height:(bottom - top)).
                    type[tutple].

    @param save_path: optional param, if it's setted up with a path string, save the new image according the path. type[string].

    @return: cropped image. type[PIL Image].
    """