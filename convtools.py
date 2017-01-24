"""
A toolkit for figuring out some problems when doing thing with NN.
NN in tensorflow, maybe is unfit to other NN libs(such as Caffe etc.).

(Nerual Network) By TCL @Raven & @Lee

"""

import numpy as np
import math as mt

PADDING_TYPE_SAME = "same"
"""
the 'same' type of zero padding which add zeros so that the all pixels of Input-image can be pooled or convoluted by their filter, 
when padding zero is odd, the top side always smaller than the bottom side and the left side always smaller than the right side.
"""
PADDING_TYPE_VALID = "valid"
"""
the 'valid' type of zero padding which drops the right-most columns or bottom rows in case of these columns cannot pooled or convoluted by their filter
"""

def width_and_height_after_conv_image(input_width=None, input_height=None, filter_width=1, filter_height=1, hstride=1, vstride=1, padding_type=PADDING_TYPE_SAME):
    """
    To figure out Featrue Map's width and height after once convloution,
    it is helpful for design a suitable CNN

    @param input_width: Input Image's width
    @param input_height: Input Image's height
    @param filter_width: filter's width
    @param filter_height: filter's height
    @param hstride: horizontal stride
    @param vertical stride
    @param padding_type: the type of zero padding

    @return: when the padding_type is same, the function will return four results, @first is the output image's width,
        @second is the output image's height, @third is the padding zero width, @fourth is the padding zero height.
        when the padding_type is valid ,the function will return two results, @first is the output image's width, 
        @second is the output image's height. (padding_along_width == padding_along_height == 0)

    FOR EXAMPLE:
        params = (input_width = 5, input_height = 5, filter_width = 3, filter_height = 3, hstride = 2, vstride = 2, padding_type = PADDING_TYPE_SAME)
        labels = ([out_width = 3, out_height = 3], [padding_along_width = 2, padding_along_height = 2])
    """
    if (input_width == None or input_height == None):
        print "invalid width/height, pls have a check."
        return None

    if (padding_type == PADDING_TYPE_SAME):
        out_width = mt.ceil(float(input_width) / float(hstride))
        out_height = mt.ceil(float(input_height) / float(vstride))

        padding_along_width = ((out_width - 1) * hstride + filter_width - input_width)
        padding_along_height = ((out_height - 1) * vstride + filter_height - input_height)

        print ("out_width:%-8d out_height:%-8d padding_along_width:%-8d padding_along_height:%8d"%(out_width, out_height, padding_along_width, padding_along_height))
        return ([out_width, out_height], [padding_along_width, padding_along_height])
    else:
        print "I DON'T KNOW. SORRY."
        return None


    if(padding_type == PADDING_TYPE_VALID):
        out_width = ceil(float(input_width - filter_width + 1) / float(hstride))
        out_height = ceil(float(input_height - filter_height + 1) / float(vstride))

        print ("out_width:%-8d out_height:%-8d "%(out_width, out_height))
        return ([out_width, out_height])

    else:
        print "I DON'T KNOW. SORRY."
        return None
