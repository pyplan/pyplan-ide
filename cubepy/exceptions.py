class AxisAlignError(ValueError):
    """
    This error is raised when axis A is being aligned to axis B and:
    - A is Series:
      if any value on axis A does not equal to the corresponding value on axis B (order is significant)
      note that it does not matter if B is Index or Series
    - A is Index and B is Series:
      if B contains a value which is not contained in A
    - A and B are both Index objects and one of them contains a value which is not in the other one 
      (this is also the case when they have different lengths); 
      note that the order of the values can be arbitrary      
    """
    pass


class InvalidAxisLengthError(ValueError):
    pass


class NonUniqueDimNamesError(ValueError):
    pass
