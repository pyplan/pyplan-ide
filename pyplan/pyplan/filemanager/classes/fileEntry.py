from enum import Enum
from .fileEntryData import FileEntryData

class eFileTypes(Enum):
    NOTHING = 0
    MY_FOLDER = 1
    PUBLIC = 2
    COMPANY = 3
    MODELS_PATH = 4
    SHARED_WITH_ME = 5


class FileEntry(object):
    def __init__(self, show=True, text="", type=eFileTypes.NOTHING, data=FileEntryData()):
        self.show = show
        self.text = text
        self.type = type.value
        self.data = data
