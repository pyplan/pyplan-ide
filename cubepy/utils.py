"""Utility functions imported by cubepy.cube and cubepy.axes.
Do not import these in order to avoid circular imports.
"""

import cubepy.axis
import cubepy.index
from cubepy.exceptions import AxisAlignError

import numpy as np


def is_axis(obj):
    return isinstance(obj, cubepy.axis.Axis)


def is_indexed(axis):
    return hasattr(axis, "indexof")


def make_axis_collection(axes):
    """Creates a list of axes if a single axis is passed in."""
    if isinstance(axes, int) or isinstance(axes, str) or is_axis(axes):
        return [axes]
    else:
        return axes


def align_arrays(axis1, axis2, axis_index1, axis_index2, values1, values2):
    """
    :param axis1:
    :param axis2:
    :param axis_index1:
    :param axis_index2:
    :param values1:
    :param values2:
    :return: tuple (axis, values1, values2)
    """
    if axis1 is axis2:
        # if self alignment, then do nothing
        return axis1, None, None
    elif is_indexed(axis2):
        # align second axis to first axis
        value_indices = axis2.indexof(axis1.values)
        return axis1, values1, values2.take(value_indices, axis_index2)
    elif is_indexed(axis1):
        # align first axis to second axis
        value_indices = axis1.indexof(axis2.values)
        return axis2, values1.take(value_indices, axis_index1), values2
    else:  # both are non-indexed
        if not np.array_equal(axis1.values, axis2.values):
            raise AxisAlignError("cannot align axes '{}' with unequal values".format(axis1.name))
        return axis1, values1, values2


def broadcast_array(values, old_axes, new_axes):
    """Add new virtual axes (length is 1) to a numpy array to correspond to the new axes."""
    new_values = values
    transpose_indices = []
    for axis in new_axes:
        try:
            axis_index = old_axes.index(axis.name)
        except LookupError:
            # if axis is not present in the cube, add virtual axis at the end
            axis_index = new_values.ndim
            new_values = np.expand_dims(new_values, axis=axis_index)
        transpose_indices.append(axis_index)

    # handle the trailing axes
    if new_values.ndim != len(new_axes):
        raise ValueError("cube broadcasting axis mismatch")

    # transpose the result
    return new_values.transpose(transpose_indices)


def unique_axes_from_cubes(cubes):
    """Creates common axis space for a collection of cubes. The following rules are observed:
    1) axes are identified only by their name, values are ignored
    2) axes are listed as they are listed in the cube collection
    3) non-indexable axes have priority over the indexable with the same name
    4) axes are not aligned by values, values are ignored
    """
    unique_axes_list = list()
    unique_axes_dict = dict()

    for cube in cubes:
        for axis in cube.axes:
            try:
                base_axis_index = unique_axes_dict[axis.name]
            except KeyError:
                # add new axis
                unique_axes_dict[axis.name] = len(unique_axes_list)
                unique_axes_list.append(axis)
            else:
                # axis with the same name was found
                base_axis = unique_axes_list[base_axis_index]
                if not is_indexed(axis) and is_indexed(base_axis):
                    # replace indexed axis with fixed axis
                    unique_axes_list[base_axis_index] = axis

    return unique_axes_list
