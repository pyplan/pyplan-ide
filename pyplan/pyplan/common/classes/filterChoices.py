from enum import Enum


class filterChoices(Enum):
    CONTAINS = 'contains'
    NOT_CONTAINS = 'notcontains'
    EQUAL = 'equal'
    NOT_EQUAL = 'notequal'
    GREATER_THAN = 'greater_than'
    GREATER_THAN_EQUAL_TO = 'greater_than_equal_to'
    LESS_THAN = 'less_than'
    LESS_THAN_EQUAL_TO = 'less_than_equal_to'
    BEGIN_WITH = 'begin_with'
    NOT_BEGIN_WITH = 'not_begin_with'
    END_WITH = 'end_with'
    NOT_END_WITH = 'not_end_with'
    EARLIEST = 'earliest'
    LATEST = 'latest'
    BETWEEN = 'between'
    NOT_BETWEEN = 'notbetween'

    def __str__(self):
        return self.value
