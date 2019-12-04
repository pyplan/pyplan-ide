from datetime import datetime
from enum import Enum

class eSpecialFolder(Enum):
    NOTHING = 0
    MY_FOLDER = 1
    PUBLIC = 2
    COMPANY = 3
    MODELS_PATH = 4
    SHARED_WITH_ME = 5

class eSpecialFileType(Enum):
    FILE = 0
    MODEL = 1
    ZIP = 2

class FileEntryData(object):

    def __init__(
            self,
            fullPath=None,
            fileSize=0.0,
            extension=None,
            specialFolderType=eSpecialFolder.NOTHING,
            specialFileType=eSpecialFileType.FILE,
            isShared=False,
            sharedBy=None,
            lastUpdateTime=datetime.now(),
            hasDenied=False,
    ):
        self.fullPath = fullPath
        self.fileSize = fileSize
        self.extension = extension
        self.specialFolderType = specialFolderType.value
        self.specialFileType = specialFileType.value
        self.isShared = isShared
        self.sharedBy = sharedBy
        self.lastUpdateTime = lastUpdateTime
        self.hasDenied = hasDenied
