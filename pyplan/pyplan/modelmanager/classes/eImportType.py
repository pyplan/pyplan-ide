from enum import Enum

class eImportType(Enum):
    MERGE = 0
    APPEND = 1
    SWITCH = 2

    def __str__(self):
        return self.value
