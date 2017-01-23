"""
A toolkit for figuring out some problems when doing thing with NN.
NN in tensorflow, maybe is unfit to other NN libs(such as Caffe etc.).
(Nerual Network) By TCL @Raven
"""

import numpy as np
import math as mt

PADDING_TYPE_SAME = "same"
PADDING_TYPE_VALID = "valid"

def width_and_height_after_conv_image(input_width=None, input_height=None, filter_width=1, filter_height=1, hstride=1, vstride=1, padding_type=PADDING_TYPE_SAME):
    """
    """
    if (input_width == None or input_height == None):
        print "invalid width/height, pls have a check."
        return None

    if (padding_type == PADDING_TYPE_SAME):
        out_width = mt.ceil(float(input_width) / float(hstride))
        out_height = mt.ceil(float(input_height) / float(vstride))

        padding_along_width = ((out_width - 1) * hstride + filter_width - input_width)
        padding_along_height = ((out_height - 1) * vstride + filter_height - input_height)

        return ([out_width, out_height], [padding_along_width, padding_along_height])
    else:
        print "I DON'T KNOW. SORRY."
        return None