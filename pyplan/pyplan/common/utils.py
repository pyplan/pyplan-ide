import os
import zipfile
from uuid import uuid4
from shlex import split
from subprocess import PIPE, Popen

from django.conf import settings
from rest_framework import exceptions


def _linuxRemove(src):
    src_path = src.replace(' ', '\ ')

    # -f, --force
    # Ignore nonexistant files, and never prompt before removing.
    # -i
    # Prompt before every removal.
    # -I
    # Prompt once before removing more than three files, or when removing recursively. This option is less intrusive than -i, but still gives protection against most mistakes.
    # --interactive[=WHEN]
    # Prompt according to WHEN: never, once (-I), or always (-i). If WHEN is not specified, then prompt always.
    # --one-file-system
    # When removing a hierarchy recursively, skip any directory that is on a file system different from that of the corresponding command line argument
    # --no-preserve-root
    # Do not treat "/" (the root directory) in any special way.
    # --preserve-root
    # Do not remove "/" (the root directory), which is the default behavior.
    # -r, -R, --recursive
    # Remove directories and their contents recursively.
    # -d, --dir
    # Remove empty directories. This option permits you to remove a directory without specifying -r/-R/--recursive, provided that the directory is empty. In other words, rm -d is equivalent to using rmdir.
    # -v, --verbose
    # Verbose mode; explain at all times what is being done.

    cmd = f'rm -rf {src_path}'
    popen = Popen(split(cmd), stdout=PIPE, universal_newlines=True)

    stdout, stderr = popen.communicate()
    if stderr:
        raise exceptions.NotAcceptable(stderr)

    return True


def _linuxCopy(src, dest):
    src_path = src.replace(' ', '\ ')
    dest_path = dest.replace(' ', '\ ')

    # -R, -r, --recursive
    #   copy directories recursively
    # -u, --update
    #   copy only when the SOURCE file is newer
    #   than the destination file or when the
    #   destination file is missing
    # -v, --verbose
    #   explain what is being done

    cmd = f'cp -ruv {src_path} {dest_path}'
    popen = Popen(split(cmd), stdout=PIPE, universal_newlines=True)

    stdout, stderr = popen.communicate()
    if stderr:
        raise exceptions.NotAcceptable(stderr)

    return True


def _uploadFile(action, my_file, folder_path, name, chunk, overwrite=False):

    file_path = os.path.join(
        settings.MEDIA_ROOT, folder_path if action == 'publishItems' else 'tmp', name)

    while chunk is 0 and os.path.isfile(file_path):
        if overwrite:
            # delete old file
            os.remove(file_path)
        else:
            # generate new file
            tempName = name.split('.')
            name = f'{tempName[0]}_copy.{tempName[1]}'
            file_path = os.path.join(settings.MEDIA_ROOT, 'tmp', name)

    # Appends all chunks of this request (chunks of chunks)
    # UI sends multiple requests with multiple chunks each per file
    with open(file_path, 'ab+') as temp_file:
        for chunk in my_file.chunks():
            temp_file.write(chunk)

    return file_path


def _zipFiles(sources, sources_folder, target_file, overwrite=False, denied_folders=None):

    # check if target_file is a path or a temporary file
    if(isinstance(target_file, str)):
        if os.path.isfile(target_file):
            if overwrite:
                # delete file
                os.remove(target_file)
            else:
                # generate new file
                file_name, file_extension = os.path.splitext(target_file)
                target_file = f'{file_name}_{uuid4().hex}{file_extension}'

    with zipfile.ZipFile(target_file, 'w', zipfile.ZIP_DEFLATED) as zfobj:
        for source in sources:
            src = os.path.join(sources_folder, source)
            if os.path.isfile(src):
                zfobj.write(src, os.path.relpath(src, os.path.join(src, '..')))
            else:
                _zipdir(src, zfobj, denied_folders)
        for zfile in zfobj.filelist:
            zfile.create_system = 0

    return target_file


def _zipdir(path, ziph, denied_folders):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        # check if folder is not in any department denied folders
        if not denied_folders or not any(list(map(lambda item: item in denied_folders, root.rsplit(os.path.sep)))):
            for file in files:
                ziph.write(os.path.join(root, file), os.path.relpath(
                    os.path.join(root, file), os.path.join(path, '..')))


def _unzipFile(source_file, target_folder):
    # Unzip the file, creating subdirectories as needed
    zfobj = zipfile.ZipFile(source_file)
    zfobj.extractall(target_folder)
