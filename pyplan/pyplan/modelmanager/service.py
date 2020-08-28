import base64
import datetime
import os
import random
import re
import sys
import tempfile
import threading
import unicodedata
import zipfile
from itertools import chain
from numbers import Number
from os.path import join

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework import exceptions

from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.common.calcEngine import CalcEngine
from pyplan.pyplan.common.utils import _uploadFile
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.filemanager.classes.fileEntry import FileEntry, eFileTypes
from pyplan.pyplan.filemanager.classes.fileEntryData import (FileEntryData,
                                                             eSpecialFileType,
                                                             eSpecialFolder)
from pyplan.pyplan.modelmanager.classes.eImportType import eImportType
from pyplan.pyplan.modelmanager.classes.modelInfo import ModelInfo
from pyplan.pyplan.modelmanager.classes.modelPreference import ModelPreference
from pyplan.pyplan.security.functions import _getAllSessions
from pyplan.pyplan.ws import sysMsg, ws_settings


class ModelManagerService(BaseService):

    # model related methods
    def openModel(self, file, forceSingleInstance=False):
        """Open model"""
        res = None

        found = False
        if not forceSingleInstance:

            my_sessions = _getAllSessions(self, onlyMySessions=True)
            for item_session in my_sessions:
                if item_session.currentModelFile == file:
                    found = True
                    res = ModelInfo()
                    res.name = item_session.currentModelName
                    res.uri = item_session.currentModelFile
                    res.modelId = item_session.currentModel
                    res.new_session_key = item_session.session_key
                    break

        if not found:
            current_session = self.getSession()
            calcEngine = CalcEngine.tryLoadFromAppPool(current_session, file)

            res = current_session.modelInfo
            res.name = calcEngine.getModelName()
            res.uri = file
            # TODO: ver cuando tengamos licenciamiento
            res.daysToExpire = 365
            _modelPreferences = calcEngine.getModelPreferences()
            res.modelId = _modelPreferences["identifier"] if "identifier" in _modelPreferences else ""
            res.onOpenModel = _modelPreferences["onOpenModel"] if "onOpenModel" in _modelPreferences else ""
            res.onOpenDashId = _modelPreferences["onOpenDashId"] if "onOpenDashId" in _modelPreferences else ""
            if not calcEngine.from_app_pool:
                res.engineUID = calcEngine.getEngineUID()
                res.engineURI = calcEngine.getEngineURI()
                res.engineParams = calcEngine.getEngineParams()

            self.saveSession()
            calcEngine = None

        if not res is None:
            is_public = False
            can_edit = False
            if "/public/" in file.lower():
                is_public = True
            if self.current_user.has_perm("pyplan.change_model") \
                    and not is_public or self.current_user.has_perm("pyplan.change_public_model") \
                    and is_public:
                can_edit = True

            res.canEdit = can_edit
            res.readonly = not can_edit
            # check for other session for mark as readonly
            try:
                for db_session in self.session_store.get_model_class().objects.all():
                    _decoded = db_session.get_decoded()
                    if "data" in _decoded and "modelInfo" in _decoded["data"] \
                            and _decoded["data"]["modelInfo"]["uri"] == file \
                            and int(_decoded["data"]["userCompanyId"]) != self.getSession().userCompanyId \
                            and not _decoded["data"]["modelInfo"]["readonly"]:
                        res.readonly = True
                        res.readOnlyReason = f"The model is being used by '{_decoded['data']['userFullName']}'. The model will be opened in read-only mode."
                        break
            except Exception as ex:
                print(
                    f"Error checking other session for mark as readonly: {str(ex)}")
            self.saveSession()
        return res

    def getModelInfo(self):
        """Navigate Diagram"""
        session = self.client_session
        if not session is None:
            modelInfo = session.modelInfo

            storage = FileSystemStorage()
            file_path = join(settings.MEDIA_ROOT, "models", modelInfo.uri)
            file_size = storage.size(file_path)
            if file_size > 1e+6:
                file_size = f"{round(file_size / 1024 / 1024, 2)} MB"
            else:
                if file_size > 1e+3:
                    file_size = f"{round(file_size / 1024, 2)} kB"
                else:
                    file_size = f"{file_size} B"
            created_time = storage.get_created_time(file_path)
            modified_time = storage.get_modified_time(file_path)

            modelInfo.uri
            res = [
                {"Key": "modelinfo_model_id", "Value": modelInfo.modelId},
                {"Key": "modelinfo_model_name", "Value": modelInfo.name},
                {"Key": "modelinfo_model_file", "Value": modelInfo.uri},
                {"Key": "modelinfo_file_size", "Value": file_size},
                {"Key": "modelinfo_created_date",
                    "Value": f"{created_time.strftime('%Y-%m-%d %H:%M')} hs."},
                {"Key": "modelinfo_updated_date",
                    "Value": f"{modified_time.strftime('%Y-%m-%d %H:%M')} hs."},
            ]
            return res
        else:
            raise exceptions.NotAcceptable("Can't find session")

    def saveModel(self):
        """Saves Model"""
        calcEngine = CalcEngine.factory(self.client_session)
        file_path = join(settings.MEDIA_ROOT, "models",
                         self.client_session.modelInfo.uri)
        return calcEngine.saveModel(file_path)

    def saveModelAs(self, modelName):
        """Saves Model With New Name"""
        if self.checkModelOpen():
            currentPath = self.client_session.modelInfo.uri
            folderPath = currentPath[:currentPath.rfind(os.path.sep)+1]
            file_path = join(folderPath, f'{modelName}.ppl')
            storage = FileSystemStorage(join(settings.MEDIA_ROOT, 'models'))
            if not storage.exists(file_path):
                calcEngine = CalcEngine.factory(self.client_session)
                try:
                    fullPath = join(storage.base_location, file_path)
                    newModel = calcEngine.saveModel(fullPath)
                    current_session = self.getSession()
                    res = current_session.modelInfo
                    res.uri = file_path
                    self.saveSession()
                    calcEngine = None
                    return res
                except Exception as ex:
                    raise exceptions.ErrorDetail(
                        f'Error when saving the model: {str(ex)}')
            raise exceptions.NotAcceptable(
                "The file name you provide already exists")
        raise exceptions.NotAcceptable("There's no currentModel")

    def navigateDiagram(self, module_id, include_arrows):
        """Navigate Diagram"""
        calcEngine = CalcEngine.factory(self.client_session)
        res = None
        if module_id:
            res = calcEngine.getDiagram(module_id)
        else:
            res = calcEngine.getDiagram()
        return res

    def getArrows(self, module_id):
        """Get Diagram Arrows"""
        calcEngine = CalcEngine.factory(self.client_session)

        if not module_id:
            current_session = self.getSession()
            module_id = current_session.modelInfo.modelId

        return {
            "arrows": calcEngine.getArrows(module_id),
            "module_id": module_id
        }

    def createNewModel(self, modelName):
        """Creates a new model """
        try:
            storage = FileSystemStorage(join(settings.MEDIA_ROOT, 'models'))

            folderSufix = 1
            new_model_name = modelName
            while storage.exists(join(storage.base_location, new_model_name)):
                folderSufix += 1
                new_model_name = f'{modelName}_{folderSufix}'

            model_path = join(new_model_name, f'{new_model_name}.ppl')
            full_path = join(storage.base_location, model_path)
            folder_path = join(storage.base_location, new_model_name)

            if not storage.exists(folder_path):
                os.mkdir(folder_path)

            calcEngine = CalcEngine.factory(self.client_session)
            if calcEngine.createNewModel(full_path, new_model_name):
                self.closeModel()
                return self.openModel(full_path), model_path
        except Exception as ex:
            raise ex

    def getModelPreferences(self):
        """Get Model Preferences"""
        calcEngine = CalcEngine.factory(self.client_session)
        engineResponse = calcEngine.getModelPreferences()
        # fill default preferences
        engineResponse["modelId"] = engineResponse["identifier"]
        if not "changeIdentifier" in engineResponse:
            engineResponse["changeIdentifier"] = "1"
        return engineResponse

    def changeToOtherModelSession(self, new_session_key):
        """Change to other model of the current user session
        """
        if self.existSession(new_session_key):
            new_session = self.getSessionByKey(new_session_key)
            if self.getSession().userCompanyId == new_session.userCompanyId:
                uri = new_session.modelInfo.uri
                return self.openModel(uri)
            else:
                raise exceptions.PermissionDenied()
        else:
            raise exceptions.PermissionDenied()

    def setModelPreferences(self, modelPreferences):
        """Set  model preferences"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.setModelProperties(modelPreferences)
        if result.text == 'ok':
            model_pref = ModelPreference(**modelPreferences)
            if model_pref.identifier or model_pref.title:
                self.client_session.modelInfo.modelId = model_pref.identifier
                self.client_session.modelInfo.name = model_pref.title
                self.saveSession()
            return self.client_session
        return False

    def closeModel(self):
        """Close current model"""
        if self.checkModelOpen():
            calcEngine = CalcEngine.factory(self.client_session)

            if calcEngine.closeModel():
                current_session = self.getSession()
                current_session.modelInfo = ModelInfo()
                self.saveSession()
            else:
                return False
        return True

    # node related methods
    def getNodeProperties(self, node_id, properties):
        """Get Node Properties"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.getNodeProperties(node_id, properties)
        return result

    def setNodeProperties(self, node_id, properties):
        """Set Node Properties"""
        # map same properties
        if node_id and len(properties) > 0:
            for prop in properties:
                if prop["name"] and prop["name"].lower() == "picture":
                    if not prop["value"]:
                        prop["value"] = None
                    else:
                        file_extension = prop["value"].rsplit(".").pop()
                        file_path = join(settings.MEDIA_ROOT, 'tmp', prop['value'])
                        with open(file_path, "rb") as image_file:
                            prop["value"] = f'data:image/{file_extension};base64,{str(base64.b64encode(image_file.read()), "utf-8")}'

                        try:
                            os.remove(file_path)
                        except Exception as ex:
                            raise exceptions.NotAcceptable(
                                f'There was an error deleting the tempfile:{str(ex)}')

        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.setNodeProperties(node_id, properties)
        return result

    def getNodeInputs(self, node_id):
        """Get Node Inputs"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.getNodeInputs(node_id)
        return result

    def getNodeOutputs(self, node_id):
        """Get Node Outputs"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.getNodeOutputs(node_id)
        return result

    def searchNodes(self, text, module_id, node_class, extra_classes, fill_detail):
        """Search Nodes"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.searchNodes(
            text, module_id, node_class, extra_classes, fill_detail)

        return result

    def searchForAutocomplete(self, text):
        """Search for autocomplete definition"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.searchNodes(text, None, None, [], True)

        return result

    def previewNode(self, node, debugMode=""):
        """Evaluate and return node result preview"""
        self.checkModelOpen()
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.previewNode(node, debugMode)

    def evaluate(self, definition):
        """Evaluate definition and return result"""
        self.checkModelOpen()
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.evaluate(definition)

    def callFunction(self, nodeId, params):
        """Call node function"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.callFunction(nodeId, params)

    def setNodesSize(self, values):
        """Set nodes size"""
        calcEngine = CalcEngine.factory(self.client_session)
        try:
            for value in values:
                # ToDo: return an array of engine responses
                calcEngine.setNodeProperties(value["id"], [
                    {"name": "x", "value": value["x"]},
                    {"name": "y", "value": value["y"]},
                    {"name": "w", "value": value["w"]},
                    {"name": "h", "value": value["h"]},
                ])
            return True
        except Exception as ex:
            raise ex

    def setNodesPosition(self, values):
        """Set nodes position"""
        calcEngine = CalcEngine.factory(self.client_session)
        try:
            for value in values:
                # ToDo: return an array of engine responses
                calcEngine.setNodeProperties(value["id"], [
                    {"name": "x", "value": value["x"]},
                    {"name": "y", "value": value["y"]},
                    {"name": "w", "value": value["w"]},
                    {"name": "h", "value": value["h"]},
                ])
            return True
        except Exception as ex:
            raise ex

    def getNodeProfile(self, node_id):
        """Get Node Profile"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.profileNode(node_id)

    def createNode(self, node):
        """create Node"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.createNode(node)

    def deleteNodes(self, node_ids):
        """delete Nodes"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.deleteNodes(node_ids)

    def createAlias(self, node_ids):
        """create Alias"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.createAlias(node_ids)

    def createInputNode(self, node_ids):
        """create Input Node"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.createInputNode(node_ids)

    def copyNodes(self, nodes):
        """copy  Nodes"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.copyNodes(nodes)

    def copyAsValues(self, params):
        """copy  Nodes as values"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.copyAsValues(params)

    def moveNodes(self, nodes):
        """move Nodes"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.moveNodes(nodes)

    def stop(self):
        """Try to stop current process"""
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.stop()

    def setNodeZ(self, nodes):
        """Sets the Z position of a node"""
        newZ = 1
        for node in nodes:
            newZ = node.z
            try:
                self.setNodeProperties(node.id, [{"name": "z", "value": newZ}])
                return True
            except Exception as ex:
                raise exceptions.NotAcceptable(
                    f"Error trying to set the node z property:{str(ex)}")

    def setNodeIdFromTitle(self, node_id):
        """Sets the nodeId from its title"""
        calcEngine = CalcEngine.factory(self.client_session)
        new_id = calcEngine.setNodeIdFromTitle(node_id)
        return new_id["node_id"]

    def executeForRefresh(self):
        """Executes a node from the refresh button"""
        value = random.randint(1, 10000000)
        calcEngine = CalcEngine.factory(self.client_session)
        calcEngine.setNodeProperties(
            "pyplan_refresh", [{"name": "definition", "value": "result = " + str(value)}])
        return calcEngine.setNodeProperties("cub_refresh", [{"name": "definition", "value": "result = " + str(value)}])

    def exportFlatNode(self, exportData):
        """Export flat node to file"""
        file_path = join(
            settings.MEDIA_ROOT, 'tmp', f'{exportData.nodeId}.{exportData.fileFormat.lower()}')
        identifier = self.getNodeProperties(
            exportData.nodeId, [{"name": "identifier", "value": ""}])
        original = identifier['properties'][0]['value']
        calcEngine = CalcEngine.factory(self.client_session)
        response = calcEngine.exportFlatNode(
            original,
            exportData.numberFormat,
            exportData.columnFormat,
            file_path
        )
        if response == 1:
            if exportData.compressed == "1":
                temp = tempfile.SpooledTemporaryFile()
                with zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) as zfobj:
                    zfobj.write(file_path)
                    for zfile in zfobj.filelist:
                        zfile.create_system = 0
                temp.seek(0)
                return temp, f'{file_path[file_path.rfind(os.path.sep)+1:file_path.rfind(".")]}.zip'
            return open(file_path, 'rb'), file_path[file_path.rfind(os.path.sep)+1:]
        raise exceptions.NotAcceptable("Engine couldn't create file")

    def exportCurrentNode(self, exportData, dashboardManagerService):
        """Export node (current table) to file"""
        file_path = join(
            settings.MEDIA_ROOT, 'tmp', f'{exportData.nodeId}.{exportData.fileFormat.lower()}')
        identifier = self.getNodeProperties(
            exportData.nodeId, [{"name": "identifier", "value": ""}])
        original = identifier['properties'][0]['value']

        decimalSep = "."

        if exportData.columnFormat == 'tab':
            exportData.columnFormat = '\t'

        if exportData.numberFormat == 'TSPDSC':
            decimalSep = ","

        # ToDo: Don't call a service from a service
        data = dashboardManagerService._evaluateNode(
            original,
            exportData.nodeQuery.dims,
            exportData.nodeQuery.rows,
            exportData.nodeQuery.columns,
            exportData.nodeQuery.summaryBy,
            0,
            sys.maxsize,
            exportData.nodeQuery.bottomTotal,
            exportData.nodeQuery.rightTotal,
            exportData.nodeQuery.hideEmpty
        )

        with open(file_path, 'w') as f:
            # first row
            f.write(data.indexOnRow)
            # column names
            for cat in data.columns.categories:
                f.write(exportData.columnFormat)
                f.write(cat)
            f.write('\n')
            # data
            for item in data.series:
                f.write(str(item.name))
                f.write(exportData.columnFormat)
                for d in item.data:
                    f.write(str(d).replace(".", decimalSep) if isinstance(d, Number) else str(d))
                    f.write(exportData.columnFormat)
                f.write('\n')

        if exportData.compressed == "1":
            temp = tempfile.SpooledTemporaryFile()
            with zipfile.ZipFile(temp, 'w', zipfile.ZIP_DEFLATED) as zfobj:
                zfobj.write(file_path)
                for zfile in zfobj.filelist:
                    zfile.create_system = 0
            temp.seek(0)
            return temp, f'{file_path[file_path.rfind(os.path.sep)+1:file_path.rfind(".")]}.zip'
        return open(file_path, 'rb'), file_path[file_path.rfind(os.path.sep)+1:]

    def exportModuleToFile(self, exportData):
        """Export module to file"""
        calcEngine = CalcEngine.factory(self.client_session)
        file_path = join(settings.MEDIA_ROOT, 'tmp', f'{exportData.moduleId}.ppl')
        if exportData.exportType != "1":
            storage = FileSystemStorage(
                join(settings.MEDIA_ROOT, 'models'))
            currentPath = self.client_session.modelInfo.uri
            folderPath = currentPath[:currentPath.rfind(os.path.sep)+1]
            file_path = join(
                storage.base_location, folderPath, f'{exportData.moduleId}.ppl')
        response = calcEngine.exportModule(exportData.moduleId, file_path)
        if response == 1:
            return open(file_path, 'rb'), file_path[file_path.rfind(os.path.sep)+1:]
        raise exceptions.NotAcceptable("Engine couldn't create file")

    def importModuleFromFile(self, importModuleData):
        """Import module from file"""
        storage = FileSystemStorage(join(settings.MEDIA_ROOT, 'models'))
        currentPath = self.client_session.modelInfo.uri
        importModuleData.currentModelPath = join(storage.base_location, currentPath)
        fullFileName = join(settings.MEDIA_ROOT, 'tmp', importModuleData.moduleFile)
        if not importModuleData.fromTemp:
            fullFileName = join(storage.base_location, importModuleData.moduleFile)

        if (importModuleData.importType.name == eImportType(0).name) or (importModuleData.importType.name == eImportType(2).name):
            calcEngine = CalcEngine.factory(self.client_session)
            result = calcEngine.importModule(importModuleData.parentModelId,
                                             fullFileName, str(importModuleData.importType.value))
            if result:
                importModuleData.importType = importModuleData.importType.value
                if importModuleData.fromTemp:
                    os.remove(fullFileName)
                return importModuleData
            raise exceptions.NotAcceptable("Error importing module")
        # TODO: implement eImportType(1).name (APPEND) case
        raise exceptions.NotAcceptable("Import Type 'APPEND' not implemented")

    def getFilesForImportWizard(self, extension):
        """
        Get files for use in import wizard 
        """
        storage = FileSystemStorage(join(settings.MEDIA_ROOT, 'models'))
        folderPath = self.client_session.modelInfo.uri[:self.client_session.modelInfo.uri.rfind(
            os.path.sep)+1]
        fullFolderPath = join(storage.base_location, folderPath)
        return self._findFilesEntriesInFolderByExtension(fullFolderPath, f'.{extension}', True, [])

    def callWizard(self, wizardRequest):
        """
        Call wizard
        """
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.callWizard(wizardRequest)

    def executeButton(self, nodeId):
        """
        Execute script of button
        """
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.executeButton(nodeId)

    def getSelector(self, node):
        """Return selector object definition"""
        self.checkModelOpen()
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.getSelector(node)

    # helper functions

    def uploadFile(self, action, my_file, folder_path, name, chunk):
        return _uploadFile(action, my_file, folder_path, name, chunk, False)

    def _removeDiacritics(self, text):
        """Removes all diacritic marks from the given string"""
        norm_txt = unicodedata.normalize('NFD', text)
        shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
        # remove accents and other diacritics, replace spaces with "_" because identifiers can't have spaces
        no_spaces = unicodedata.normalize(
            'NFC', shaved).lower().replace(" ", "_")
        final_text = no_spaces
        # only allow [a-z], [0-9] and _
        p = re.compile('[a-z0-9_]+')
        for i in range(0, len(no_spaces)):
            if not (p.match(no_spaces[i])):
                final_text = final_text[:i] + '_' + final_text[i+1:]
        # i the first char is not a-z then replaceit (all identifiers must start with a letter)
        p2 = re.compile('[a-z]+')
        if not p2.match(final_text[0]):
            final_text = 'a' + final_text[1:]
        return final_text

    def _findFilesEntriesInFolderByExtension(self, path, extension, subFolders=True, pathList=[]):
        """  Recursive function to find all files of an extension type in a folder (and optionally in all subfolders too) and returns them as file entries
        path:        Base directory to find files
        pathList:    A list that stores all paths
        extension:   File extension to find (example = txt)
        subFolders:  Bool.  If True, find files in all subfolders under path. If False, only searches files in the specified folder
        """
        try:
            for entry in os.scandir(path):
                if entry.is_file() and entry.path.endswith(extension):
                    fileStats = os.stat(entry.path)
                    # TODO: Revisar que siempre devuleve specialfolder type 0 aunque se trate de public o my folder etc.
                    # Esto estaba asi en .net pero es para revisar
                    fileEntry = FileEntry(
                        text=str(entry.path[entry.path.rfind(os.path.sep)+1:]),
                        type=eFileTypes.NOTHING,
                        data=FileEntryData(
                            # fullPath=entry.path,
                            fullPath=str(entry.path[entry.path.rfind(os.path.sep)+1:]),
                            fileSize=fileStats.st_size,
                            lastUpdateTime=datetime.datetime.fromtimestamp(
                                fileStats.st_mtime).isoformat()
                        )
                    )
                    pathList.append(fileEntry)
                elif entry.is_dir() and subFolders:   # if its a directory, then repeat process as a nested function
                    pathList = self._findFilesEntriesInFolderByExtension(
                        entry.path, extension, subFolders, pathList)
        except OSError:
            print('Cannot access ' + path + '. Probably a permissions error')

        return pathList

    def installLibrary(self, lib):
        """Install python library"""
        calcEngine = CalcEngine.factory(self.client_session)

        pos = self.client_session.modelInfo.uri.find("/", self.client_session.modelInfo.uri.find("/", 1)+1)
        current_path = self.client_session.modelInfo.uri[:pos]
        target_path = join(settings.MEDIA_ROOT, 'models', current_path)
        result = calcEngine.installLibrary(lib, target_path)
        return result

    def listInstalledLibraries(self):
        """List python installed libraries"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.listInstalledLibraries()
        return result

    def uninstallLibrary(self, lib, target):
        """Uninstall python library"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.uninstallLibrary(lib, target)
        return result

    def getInstallProgress(self, from_line):
        """Get install python library progress"""
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.getInstallProgress(from_line)
        return result
