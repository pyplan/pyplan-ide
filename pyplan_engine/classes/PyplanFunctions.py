import pandas as pd


class PyplanFunctions(object):

    @staticmethod
    def register(local):
        local["selector"] = Selector


class Selector(object):
    """ Class to manage UI Pyplan selectors.
    """

    SERIALIZABLE_PROPERTIES = ['options', 'selected', 'multiselect']

    def __init__(self, options, selected, multiselect=False):
        """ Create UI Pyplan selector for desicion nodes
        Params:
            options: List or pd.Index with available values that can be selected 
            selected: current selected index value's
            multiselect: True to allow multiple selection
        """
        self._options = options
        self._multiselect = multiselect
        self.selected = selected

    @property
    def value(self):
        if self.multiselect:
            return [self.options[i] for i in self.selected]
        else:
            return self.options[self.selected]

    @property
    def options(self):
        return self._options

    @property
    def multiselect(self):
        return self._multiselect

    @property
    def selected(self):
        res = None
        if self.multiselect:
            res = []
            for nn in self._selected:
                if nn < len(self._options):
                    res.append(nn)
            if len(res) == 0:
                res = list(range(len(self._options)))
        else:
            res = self._selected if self._selected < len(self._options) else 0

        return res

    @selected.setter
    def selected(self, value):
        if self.multiselect:
            if value is None:
                self._selected = []
            elif isinstance(value, list):
                self._selected = value
            else:
                self._selected = [value]
        else:
            if isinstance(value, list):
                self._selected = value[0]
            else:
                self._selected = value

    def toObj(self):
        res = dict()
        for k in Selector.SERIALIZABLE_PROPERTIES:
            if hasattr(self, k):
                if k == "options" and isinstance(getattr(self, k), pd.Index):
                    res[k] = getattr(self, k).tolist()
                else:
                    res[k] = getattr(self, k)
        return res
