from enum import Enum


class eNodeProperty(Enum):
    IDENTIFIER = "identifier"
    ORIGINAL_ID = "originalId"
    TITLE = "title"
    DEFINITION = "definition"
    UNITS = "units"
    CLASS = "nodeClass"
    DESCRIPTION = "description"
    NUMBER_FORMAT = "numberFormat"
    PICTURE = "picture"
    RESULT = "result"

    def __str__(self):
        return self.value
