import numpy as np

from cubepy.exceptions import NonUniqueDimNamesError
from cubepy.utils import is_axis


class Axes(object):
    """Axes is an internal helper class allowing easier manipulation with cube axes.
    It is not intended to be accessed by users of cubepy package.

    Get axis name of an axis of given index:
    ax_name = cube.axes[0].name
    
    Get index of axis of a given name:
    ax_index = cube.axes.index('a')
    
    Axes can be indexed using integer or string index:
    ax1 = cube.axes[0]
    ax_a = cube.axes['a']
    
    Axes can be used as iterables:
    axes_list = list(cube.axes)  
    # the above is better than [axis for axis in cube.axes]
    axes_dict = dict(name: axis for name, axis in enumerate(cube.axes))"""

    def __init__(self, axes):
        """If for non-unique axes are found, ValueError is raised.
        If axis has invalid type, TypeError is raised.
        :param axes: Axis or a collection of Axis objects (incl. another Axes object)
        """
        # special case with zero axes
        if axes is None:
            self.axes = tuple()
            self.dims = tuple()
            return

        # special case with a single axis
        if is_axis(axes):
            axes = [axes]

        unique_names = set()
        for axis in axes:
            # test correct types
            if not is_axis(axis):
                raise TypeError("axis must be an instance of Axis")
            # test unique names - report the name of the first axis which is not unique
            if axis.name in unique_names:
                raise NonUniqueDimNamesError("multiple axes with name '{}'".format(axis.name))
            unique_names.add(axis.name)

        # the sequence of axes must be immutable
        self.axes = tuple(axes)
        self.dims = tuple(a.name for a in axes)

    def __repr__(self):
        axes = [str(a) for a in self.axes]
        return "Axes(" + ', '.join(axes) + ")"

    def __len__(self):
        return len(self.axes)

    def __getitem__(self, index):
        """Return an axis given by its index.
        :param index: int
        :return: an Axis object
        :raise: IndexError if not found
        """
        return self.axes[index]

    def axis_by_index(self, index):
        return self.axes[index]

    def axis_by_name(self, name):
        """Returns None if not found.
        """
        return next((axis for axis in self.axes if axis.name == name), None)

    def axis_and_index(self, axis):
        index = self.index(axis)
        return self[index], index

    def is_unique_subset(self, axes):
        """Tests whether all axes are contained in the Axes object and whether they are unique.
        """
        raise NotImplementedError
        
    def complement(self, axes):
        """Return a tuple of indices of axes from Axes object which are not
        contained in the specified collection of axes.
        :param axes: collection of axes specified by axis name or index
        :return: tuple of int
        """
        if isinstance(axes, str) or isinstance(axes, int):
            axes = (axes,)
        indices = set(self.index(a) for a in axes)
        if len(indices) != len(axes):
            raise ValueError("axes are not unique")
        return tuple(i for i in range(len(self)) if i not in indices)
        
    def index(self, axis):
        """Find axis index by name, by index, or by axis object.
         :param axis: int, str or Axis
         :return: int
         :raise: LookupError if not found
         """
        # find by numeric index, normalize negative numbers
        if isinstance(axis, int):
            axis_count = len(self.axes)
            if 0 <= axis < axis_count:
                return axis
            if -axis_count <= axis < 0:
                # negative index is counted from the last axis backward
                return axis_count + axis
            raise LookupError("invalid axis index: {}".format(axis))
        
        # find by name
        if isinstance(axis, str):
            for i, a in enumerate(self.axes):
                if a.name == axis:
                    return i
            raise LookupError("invalid axis name: '{}'".format(axis))
        
        # find by object identity
        if is_axis(axis):
            for i, a in enumerate(self.axes):
                if a is axis:
                    return i
            #try by name
            return self.index(axis.name)
            #raise LookupError("axis not found: {}".format(axis))

        raise TypeError("invalid axis identification type")

    def contains(self, axis):
        """Returns True/False indicating whether the axis is contained in the Axes object.
        Axis can be specified by name (str), by index (int) or by Axis object.
        """
        try:
            self.index(axis)
            return True
        except LookupError:
            return False

    def transposed_indices(self, front, back):
        """Reorder axes by specified names or indices. Return a list of axis
        indices which correspond to the new order of axes.
        """
        if isinstance(front, str) or isinstance(front, int) or is_axis(front):
            front = [front]

        if isinstance(back, str) or isinstance(back, int) or is_axis(back):
            back = [back]

        front_axes = list()
        back_axes = list()
        temp_axes = list(self.axes)
        for axis_id in front:
            index = self.index(axis_id)
            front_axes.append(index)
            if temp_axes[index] is None:
                raise ValueError("duplicate axes in transpose")
            temp_axes[index] = None

        for axis_id in back:
            index = self.index(axis_id)
            back_axes.append(index)
            if temp_axes[index] is None:
                raise ValueError("duplicate axes in transpose")
            temp_axes[index] = None

        middle_axes = [index for index, axis in enumerate(temp_axes) if axis is not None]
        return front_axes + middle_axes + back_axes

    def insert(self, axis, index=0):
        """Insert a new axis at the specified position and return the new Axes object.
        :param axis: the new axis to be inserted
        :param index: the index of the new axis
        :return: new Axes object
        """
        axis_list = list(self.axes)
        # need to correctly handle negative values
        # for example: index -1 means that the new axis should be the last axis after the insertion
        if index < 0:
            index = len(axis_list) + 1 - index
        axis_list.insert(index, axis)
        return Axes(axis_list)

    def remove(self, axis_id):
        """Remove axis or axes with a given index or name.
        Return new Axes object.
        """
        axis_index = self.index(axis_id)
        return self._remove(axis_index)

    def _remove(self, axis_index):
        new_axes = list(self.axes)
        del new_axes[axis_index]
        return Axes(new_axes)

    def rename(self, old_axis_id, new_axis_name):
        """Return an Axes object with a renamed axis.
        :param old_axis_id: axis index (int) or name (str)
        :param new_axis_name: the name of the new axis (str)
        :return: new Axes object
        """
        old_axis, old_axis_index = self.axis_and_index(old_axis_id)
        new_axis = old_axis.rename(new_axis_name)
        return self._replace(old_axis_index, new_axis)

    def replace(self, old_axis_id, new_axis):
        """Replace an existing axis with a new axis and return the new Axes object.
        The new axes collection is checked for duplicate names.
        The old and new axes are NOT checked for equal lengths.
        :param old_axis_id: axis index (int) or name (str)
        :param new_axis: Series or Index object
        :return: new Axes object
        """
        old_axis_index = self.index(old_axis_id)
        return self._replace(old_axis_index, new_axis)

    def _replace(self, old_axis_index, new_axis):
        new_axes = list(self.axes)
        new_axes[old_axis_index] = new_axis
        return Axes(new_axes)

    def swap(self, axis_id1, axis_id2):
        """Return a new Axes object with two axes swapped.
        :param axis_id1: name or index of the first axis
        :param axis_id2: name or index of the second axis
        :return: new Axes object
        """
        index1 = self.index(axis_id1)
        index2 = self.index(axis_id2)
        new_axes = list(self)
        new_axes[index1], new_axes[index2] = new_axes[index2], new_axes[index1]
        return Axes(new_axes)


def intersect(axes1, axes2):
    """Return the space intersect of the common axes. The order of values on each axis correspond to the order on
    the corresponding axis on axes1. The result can be used for inner join operations.
    :param axes1: Axes object
    :param axes2: Axes object
    :return: Axes
    """
    common_axes = []
    for axis1 in axes1:
        axis2 = axes2.axis_by_name(axis1.name)
        if axis2 is None:
            continue

        if axis1 is axes2:
            axis = axis1
        else:
            indices = np.in1d(axis1.values, axis2.values)  # TODO: assume_unique=True ?
            axis = axis1[indices]

        common_axes.append(axis)

    return Axes(common_axes)


def make_axes(axes):
    """Creates an Axes object from a collection of axes."""
    if not isinstance(axes, Axes):
        return Axes(axes)
    else:
        return axes
