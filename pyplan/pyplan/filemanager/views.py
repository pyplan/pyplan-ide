import coreapi
import coreschema
from django import forms
from django.contrib.auth.decorators import permission_required
from django.http import FileResponse
from django.shortcuts import render
from rest_framework import exceptions, parsers, permissions, status
from rest_framework.decorators import (api_view, authentication_classes,
                                       parser_classes, permission_classes,
                                       schema)
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.urls import url

from pyplan.pyplan.auth.custom_authentication import \
    QueryStringTokenAuthentication

from .serializers import (CopyFileOrFolderSerializer, CreateFolderSerializer,
                          DeleteFilesSerializer, FileEntrySerializer,
                          GetFoldersAndFilesSerializer, SourcesListSerializer,
                          UnzipFileSerializer, UploadFilesSerializer)
from .service import FileManagerService


class FileManagerView(object):
    """
    FileManager View.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """

    @staticmethod
    def register():
        return [
            url(r'^fileManager/getMainFolders/$', FileManagerView.getMainFolders),
            url(r'^fileManager/getFiles/$', FileManagerView.getFoldersAndFiles),
            url(r'^fileManager/createFolder/$', FileManagerView.createFolder),
            url(r'^fileManager/copyFileOrFolder/$', FileManagerView.copyFileOrFolder),
            url(r'^fileManager/renameFile/$', FileManagerView.renameFile),
            url(r'^fileManager/duplicateFiles/$', FileManagerView.duplicateFiles),
            url(r'^fileManager/moveFiles/$', FileManagerView.moveFiles),
            url(r'^fileManager/copyFiles/$', FileManagerView.copyFiles),
            url(r'^fileManager/copyToMyWorkspace/$', FileManagerView.copyToMyWorkspace),
            url(r'^fileManager/deleteFiles/$', FileManagerView.deleteFiles),
            url(r'^fileManager/upload/$', FileManagerView.upload),
            url(r'^fileManager/download/$', FileManagerView.download),
            url(r'^fileManager/unzipFile/$', FileManagerView.unzipFile),
            url(r'^fileManager/zipFiles/$', FileManagerView.zipFiles),
            url(r'^fileManager/getHome/', FileManagerView.getHome),
            url(r'^fileManager/optimizeTemplates/$', FileManagerView.optimizeTemplates),
        ]

    @staticmethod
    @api_view(['GET'])
    @permission_required('pyplan.list_folders', raise_exception=True)
    def getMainFolders(request, *args, **kargs):
        """
        list:
        Return a list of all folders.
        """
        try:
            service = FileManagerService(request)
            folders = service.getMainFolders()
            serializer = FileEntrySerializer(folders, many=True, context={
                                             'client_session': service.client_session})
            return Response(serializer.data)
        except FileNotFoundError:
            raise exceptions.NotFound('Folder Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['GET'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field('folder', required=False, location='query', description='folder name'),
    ]))
    @permission_required('pyplan.list_folders', raise_exception=True)
    def getFoldersAndFiles(request, *args, **kargs):
        """
        list:
        Return a list of all folders and files.
        """
        serializer = GetFoldersAndFilesSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        folder = request.query_params.get('folder', '')
        try:
            service = FileManagerService(request)
            files = service.getFoldersAndFiles(folder)
            serializer = FileEntrySerializer(files, many=True, context={
                                             'client_session': service.client_session})
            return Response(serializer.data)
        except FileNotFoundError:
            raise exceptions.NotFound('Folder Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['POST'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field(
            "data",
            required=True,
            location="body",
            description='{"folder_path":str, "folder_name":str}',
            schema=coreschema.Object()
        ),
    ]))
    @permission_required('pyplan.add_folder', raise_exception=True)
    def createFolder(request, *args, **kargs):
        """
        create:
        Creates a folder inside provided path.
        """
        serializer = CreateFolderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            folder_path = serializer['folder_path'].value
            folder_name = serializer['folder_name'].value

            path = FileManagerService().createFolder(folder_path, folder_name)
            return Response({'path': path})
        except FileNotFoundError:
            raise exceptions.NotFound('Folder Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['POST'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field(
            "data",
            required=True,
            location="body",
            description='{"folder_path":str, "folder_name":str}',
            schema=coreschema.Object()
        ),
    ]))
    @permission_required('pyplan.copy_file_or_folder', raise_exception=True)
    def copyFileOrFolder(request, *args, **kargs):
        """
        create:
        Duplicate file or Folder.
        """
        serializer = CopyFileOrFolderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            source = serializer['source'].value
            destination = serializer['destination'].value
            result = FileManagerService().copyFileOrFolder(source, destination)

            return Response({'path': result})
        except FileNotFoundError:
            raise exceptions.NotFound('Folder Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['GET'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("source", required=True, location="query"),
        coreapi.Field("newName", required=True, location="query"),
    ]))
    @permission_required('pyplan.copy_file_or_folder', raise_exception=True)
    def renameFile(request, *args, **kargs):
        """
        Rename File
        """
        source = request.query_params.get('source', None)
        new_name = request.query_params.get('newName', None)

        try:
            result = FileManagerService().renameFile(source, new_name)
            return Response({'path': result})
        except FileNotFoundError:
            raise exceptions.NotFound('Folder or File Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['GET'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("sources", required=True, location="query"),
    ]))
    @permission_required('pyplan.copy_file_or_folder', raise_exception=True)
    def duplicateFiles(request, *args, **kargs):
        """
        Duplicate Files
        """
        sources = request.query_params.getlist('sources', [])

        try:
            if len(sources) > 0:
                result = FileManagerService().duplicateFiles(sources)
                return Response({'path': result})
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FileNotFoundError:
            raise exceptions.NotFound('Folder or File Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['GET'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("sources", required=True, location="query"),
        coreapi.Field("target", required=True, location="query"),
    ]))
    @permission_required('pyplan.copy_file_or_folder', raise_exception=True)
    def moveFiles(request, *args, **kargs):
        """
        Move Files
        """
        sources = request.query_params.getlist('sources', [])
        target = request.query_params.get('target', None)

        try:
            if len(sources) > 0 and target:
                result = FileManagerService().moveFiles(sources, target)
                return Response()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FileNotFoundError:
            raise exceptions.NotFound('Folder or File Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['GET'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("sources", required=True, location="query"),
        coreapi.Field("target", required=True, location="query"),
    ]))
    @permission_required('pyplan.copy_file_or_folder', raise_exception=True)
    def copyFiles(request, *args, **kargs):
        """
        Copy Files
        """
        sources = request.query_params.getlist('sources', [])
        target = request.query_params.get('target', None)

        try:
            if len(sources) > 0 and target:
                result = FileManagerService().copyFiles(sources, target)
                return Response()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FileNotFoundError:
            raise exceptions.NotFound('Folder or File Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['GET'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("source", required=True, location="query"),
    ]))
    @permission_required('pyplan.copy_file_or_folder', raise_exception=True)
    def copyToMyWorkspace(request, *args, **kargs):
        """
        Copy to My Workspace
        """
        source = request.query_params.get('source', None)

        try:
            if source:
                result = FileManagerService(request).copyToMyWorkspace(source)
                return Response(result)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except FileNotFoundError:
            raise exceptions.NotFound('Folder or File Not Found')
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['DELETE'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("sources", required=True, location="query"),
    ]))
    @permission_required('pyplan.delete_files', raise_exception=True)
    def deleteFiles(request, *args, **kargs):
        """
        create:
        Duplicate file or Folder.
        """
        serializer = DeleteFilesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            sources = serializer['sources'].value
            result = FileManagerService().deleteFiles(sources)

            return Response(status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @parser_classes((parsers.MultiPartParser, parsers.FormParser,))
    def upload(request, *args, **kargs):
        """
        uploads multiple files
        """
        serializer = UploadFilesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            service = FileManagerService(request)
            service.createFile(
                request.FILES["files"],
                serializer.data.get("folder_path"),
                serializer.data.get("name"),
                serializer.data.get("chunk")
            )
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @api_view(['GET'])
    @authentication_classes((QueryStringTokenAuthentication,))
    @permission_required('pyplan.download_files', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("sources", required=True, location="query", schema=coreschema.Array()),
        coreapi.Field("auth_token", required=True, location="query", schema=coreschema.String()),
    ]))
    def download(request, *args, **kargs):
        """
        download multiple files
        """
        serializer = SourcesListSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        try:
            service = FileManagerService(request)
            file_stream, file_name = service.download(
                serializer.data.get('sources'),
            )
            return FileResponse(file_stream, as_attachment=True, filename=file_name)
        except Exception as ex:
            raise exceptions.NotAcceptable(detail=ex)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("source", required=True, location="query"),
        coreapi.Field("targetFolder", required=True, location="query"),
    ]))
    def unzipFile(request, *args, **kargs):
        """
        unzip file
        """
        serializer = UnzipFileSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        try:
            service = FileManagerService(request)
            service.unzipFile(
                serializer.data.get("source"),
                serializer.data.get("targetFolder")
            )
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("sources", required=True, location="query", schema=coreschema.Array()),
    ]))
    def zipFiles(request, *args, **kargs):
        """
        zip files
        """
        serializer = SourcesListSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        try:
            service = FileManagerService(request)
            service.zipFiles(
                serializer.data.get("sources")
            )
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    def getHome(request, *args, **kargs):
        """
        Return home json definition of the current company
        """
        service = FileManagerService(request)
        return Response(service.getHome())

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("sources", required=True, location="query", schema=coreschema.Array()),
    ]))
    def optimizeTemplates(request, *args, **kargs):
        """
        Optimice templates for speed up future reads
        """
        serializer = SourcesListSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        try:
            service = FileManagerService(request)
            service.optimizeTemplates(
                serializer.data.get("sources"),
            )
        except Exception as ex:
            return Response(str(ex), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_200_OK)
