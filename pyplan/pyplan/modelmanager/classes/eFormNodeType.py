from enum import Enum

class eFormNodeType(Enum):
    CHECKBOX = 0
    COMBOBOX = 1
    SCALARINPUT = 2
    BUTTON = 3

    def __str__(self):
        return self.value
