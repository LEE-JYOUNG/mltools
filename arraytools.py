"""
Array tools for develpoment convinience. By TCL @Raven
"""

import numpy as np

# type constants
TYPE_INVALID = -1
TYPE_PYTHON_LIST = 0
TYPE_NUMPY_LIST = 1

def cast_to_onehot(labels=None, target_type=np.float32):
    """
    This function is used for conver a normal array or numpy.ndarray to
    an 'one hot' numpy.ndarray.

    @param labels: an array represent the labels, should be considered start
                    from 1 to a bigger number. for example: [2, 4, 1, 5, 3].
                    not from 0, for example: [1, 3, 0, 4, 2](wrong labels).

    @param target_type: for our usage, it is only be numpy.float32 or numpy.float64.

    @return a numpy.ndarray with the 'onehot' structure. FOR EXAMPLE:
            input: [2, 3, 1, 2, 4]
            output:
                    [[0., 1., 0., 0.],
                     [0., 0., 1., 0.],
                     [1., 0., 0., 0.],
                     [0., 1., 0., 0.],
                     [0., 0., 0., 1.]]
    """
    if labels == None:
        print "find a none array."
        return None

    param_type = type(labels)
    param_type_i = TYPE_INVALID
    if param_type == list:
        param_type_i = TYPE_PYTHON_LIST
    elif param_type == np.ndarray:
        param_type_i = TYPE_NUMPY_LIST
    else:
        print "error with param type(not a list or numpy.ndarray)."
        return None

    try:
        if param_type_i == TYPE_PYTHON_LIST:
            labels = np.asarray(labels, dtype=target_type)

        if len(labels.shape) > 1:
            print "labels should be an one dimension array."
            return None

        target_row = len(labels)
        target_column_index = np.argmax(labels)
        target_column = int(labels[target_column_index])

        target = np.zeros([target_row, target_column], dtype=target_type)

        index = 0
        min_element = labels[np.argmin(labels)]

        if (min_element < 1):
            print "labels should be considered as an array which start from 1 to a bigger number, not start from 0."
            return None

        labels_ = labels - 1

        for e in target:
            e[int(labels_[index])] = 1.0
            index += 1

        return target
    except:
        print "error occured. pls check the param, should be a number array."
        return None


def cast_strlabels_to_intlabels(labels=None, categories=None):
    """
    To cast a string list(represent a category list) to an int list, for example:
    input: ["flower", "tree", "dog", "cat", "tree"], output: [1, 2, 3, 4, 2].
    after this operation, you would use the function 'cast_to_onehot' to cast the
    int labels to an 'one hot' array. for Machine Learning.

    @param labels: a string array as a python list or numpy.str.

    @param categories: if the labels contain all the categories, there's no neccessary
                        to use this param, if not, you should provide an all possibilities
                        categories in this param, in often, the param 'categories' should
                        be a string array as a python list or numpy.str.

    @return: the function will return two results, @first is the int list that converted by string list.
                @second is all the possibilities included from labels or categories, it's dictionary type.

    FOR EXAMPLE:
        param1 = ["cate1", "cate3", "cate2", "cate5"], param2 = ["cate1", "cate2", "cate3", "cate4", "cate5"],
        param2 has all categories and the count of the elements is more than param1.

        ilabels, cats = cast_strlabels_to_intlabels(param1, param2)
        ilabels = [1, 3, 2, 5]
        param2 = {1:"cate1", 2:"cate2", 3:"cate3", 4:"cate4", 5:"cate5"}
    """
    if (labels == None):
        print "invalid labels, maybe a none param."
        return None, None

    labels_type = type(labels)
    param_type = TYPE_INVALID
    if (labels_type == list):
        param_type = TYPE_PYTHON_LIST
    elif (labels_type == np.ndarray):
        param_type = TYPE_NUMPY_LIST
    else:
        print "invalid type of first param 'labels'."
        return None, None

    if (categories == None):
        categories = drop_repeat_in_list(labels)
    else:
        categories = drop_repeat_in_list(categories)

    categories_with_index = {}
    intlabels = []

    for i in range(1, len(categories) + 1):
        categories_with_index[i] = categories[i-1]

    for i in labels:
        intlabels.append((categories_with_index.keys())[(categories_with_index.values()).index(i)])

    return intlabels, categories_with_index



def drop_repeat_in_list(source=None, sort=False):
    """
    To drop the repeat element in an list.
    the type of list could be a python list or numpy.ndarray.

    @param1 source: which list you want to be handled.

    @param2 sort: whether to handle the list by sort.

    @return: a handled list.
    """
    if (source == None):
        print "invalid param 'source'."
        return None

    source_type = type(source)
    param_type = TYPE_INVALID
    if (source_type == list):
        param_type = TYPE_PYTHON_LIST
    elif (source_type == np.ndarray):
        param_type = TYPE_NUMPY_LIST
    else:
        print "invalid type of first param 'source'."
        return None

    if (param_type == TYPE_NUMPY_LIST):
        source = source.tolist()

    target = []
    for i in source:
        try:
            index = target.index(i)
        except:
            target.append(i)

    if (sort == True):
        target.sort()

    return target