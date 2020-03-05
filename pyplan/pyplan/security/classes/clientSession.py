from datetime import datetime

from pyplan.pyplan.modelmanager.classes.modelInfo import ModelInfo


class ClientSession(object):

    def __init__(self):
        self.session_key = ""
        self.userId = ""
        self.userFullName = ""
        self.userFirstName = ""
        self.userLastName = ""
        self.userName = ""
        self.userCompanyId = -1
        self.userIsSuperUser = False
        self.companyId = -1
        self.company_code = ""
        self.companyName = ""
        self.process = []
        self.modelInfo = ModelInfo()
        self.imageUrl = ""
        self.loginModule = ""
        self.autoopenUri = ""
        self.decimalSep = "."
        self.thousandSep = ","
        self.copyDecimalSep = "."
        self.companySettingFile = ""
        self.loginAction = None
        self.created_at = datetime.now()
        self.departments = []
        self.my_uuid = None
        self.my_username = None
