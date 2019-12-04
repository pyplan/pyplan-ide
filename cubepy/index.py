import numpy as np

from cubepy.axis import Axis


class Index(Axis):
    """A named sequence of unique indexed values. Can be used as indexable axis in Cube.
    Name is a string. Values are stored in one-dimensional numpy array.
    """

    def __init__(self, name, values):
        """Initialize a new Index object. The values must be unique, otherwise ValueError is raised.
        :param name: str
        :param values: sequence of values (must be unique), 
                        sequence of cubepy.Index 
        :raise: ValueError if there are duplicate values
        """

        if isinstance(values,list) and len(values)>0 and isinstance(values[0],self.__class__):
            nn=0
            for idx in values:
                if nn==0:
                    fullValues = np.copy(idx.values)
                else:
                    fullValues = np.concatenate( (fullValues ,idx.values), axis=0)
                nn+=1
            values = np.unique(fullValues)

        super(Index, self).__init__(name, values)

        # create dictionary
        self._indices = {x: i for i, x in enumerate(self._values)}

        # values must not be change once the index has been created
        self._values.flags.writeable = False
        
        if len(self._indices) != len(self._values):
            raise ValueError('Index cannot have duplicate values')
        
        self._vectorized_index = np.vectorize(self._indices.__getitem__, otypes=[np.int])
        self._vectorized_contains = np.vectorize(self._indices.__contains__, otypes=[np.bool])

    def __contains__(self, item):
        """Implementation of 'in' operator.
        :param item: a value to be looked up whether exists
        :return: bool
        """
        return item in self._indices

    def contains(self, item):
        """Tests whether item or items exist among values.
        If item is single value, then return a single boolean value.
        If item is a sequence, then return numpy array of booleans.
        :param item: a single value or a sequence of values
        :return: bool or numpy array of bools
        """
        v = self._vectorized_contains(item)
        if v.ndim > 0:
            return v
        return v.item()

    def indexof(self, item):
        """If item is single value, then return a single integer value.
        If item is a sequence, then return numpy array of integers.
        :param item: a single value or a sequence of values
        :return: int or numpy array of ints
        :raise: KeyError if value does not exist
        """
        v = self._vectorized_index(item)
        if v.ndim > 0:
            return v
        return v.item()

    @property
    def pos(self):
        from cubepy.cube import Cube
        return Cube([self],range(len(self)))   
 

