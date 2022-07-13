"""
A file-operation library.
It control files and dirs (but not link).
"""

import os
import shutil
import stat
import sys
import typing
import datetime
from os import path
from typing import IO

from PIL import Image

ACCEPT_OPEN_MODE = [
    "r+", "+r", "rt+", "r+t", "+rt", "tr+", "t+r", "+tr",
    "w+", "+w", "wt+", "w+t", "+wt", "tw+", "t+w", "+tw",
    "a+", "+a", "at+", "a+t", "+at", "ta+", "t+a", "+ta",
    "x+", "+x", "xt+", "x+t", "+xt", "tx+", "t+x", "+tx",
    "w", "wt", "tw", "a", "at", "ta", "x", "xt", "tx",
    "r", "rt", "tr", "rb+", "+rb", "r+b", "br+", "b+r",
    "+br", "wb+", "w+b", "+wb", "bw+", "b+w", "+bw", "ab+",
    "a+b", "+ab", "ba+", "b+a", "+ba", "xb+", "x+b", "+xb",
    "bx+", "b+x", "+bx", "wb", "bw", "ab", "ba", "xb",
    "bx", "rb", "br"]
"""Accepted file mode"""

openFile = open
"""
# OpenFile function
Open a file.
Returns a file object.
## Params:
- `name` - The name of the file, it will be a string(path).
- `mode` - The open mode, it will be a string and it must in the `ACCEPT_OPEN_MODE`
- `encoding` is the encoding of a text file, defult `gbk`.
- `buffering` is a number that to set the buffer area, defult `0`
- `errors` is a string that to procces errors, defult `strict`, 
must in `strict` `ignore` `replace` `surrogateescape` `backslashreplace` `namereplace`.
- `newlines` (deprecated!)
- `closefd` The underlying file descriptor will be kept open when the file  (yes/no).
- `opener` The opener of the function.
"""


changeFileMode = os.chmod
"""
# ChangeFileMode function
Change the file (not link) modes and propoties.
No returns.
## Params:
- `path` The path of the file.
- `mode` The mode or propoty-type that you want to change, must be a octonary integer.
"""


def getFileInfo(filename: str) -> typing.Dict[str, typing.Any]:
    prop = os.stat(filename)
    return {
        "mode": oct(prop.st_mode),
        "ino": prop.st_ino
    }


def openImage(name: str) -> Image.Image:
    """
    # OpenImage function
    Open a image file ( just for read ).
    Returns a file object.
    ## Params:
    - `name` - The name of the image file, it will be a string(path).
    """
    return Image.open(name)


def newFile(name: str, bytefile: bool = False, getfile: bool = False) -> typing.Union[None, IO]:
    """
    # NewFile function
    Create a file
    Returns a file object or None.
    ## Params:
    - `name` - The name of the file, it will be a string(path).
    - `bytefile` - Create a byte file (yes/no), it will be a boolean, defalt `False`.
    - `getfile` - Get the newed file (yes/no), it will be a boolean, defalt `False`.
    """
    file = openFile(name, "wb") if bytefile else openFile(name, "w")
    if not getfile:
        file.close()
        return None
    else:
        return file


def delFile(name: str) -> typing.NoReturn:
    """
    # DelFile function
    Delete a file.
    No returns.
    ## Params:
    - `name` - The name of the file, it will be a string(path).
    """
    if not path.exists(name):
        raise FileNotFoundError(f"The file {name} is not exists!")
    os.remove(name)


def newFolder(dir_: str, exists_ok: bool = False) -> typing.NoReturn:
    """
    # NewFolder function
    Create a folder.
    No returns.
    ## Params:
    - `dir` - The dir of the folder, it will be a string(path).
    - `exists_ok` - Recreate the folder (yes/no), it will be a boolean, defult `False`.
    """
    if path.exists(dir_) and not exists_ok:
        raise FileExistsError(f"The dir {dir_} is exists!")
    os.makedirs(dir_, exist_ok=exists_ok)


def delFolder(dir_: str) -> typing.NoReturn:
    """
    # DelFolder function
    Delete a folder.
    No returns.
    ## Params:
    - `dir` - The dir of the folder, it will be a string(path).
    """
    if not path.exists(dir_):
        raise FileNotFoundError(f"The dir {dir_} is not exists!")
    os.removedirs(dir_)


def copyFile(f1: str, f2: str) -> typing.NoReturn:
    """
    # CopyFile function
    Copy a file.
    No returns.
    If the file is readonly, system will cancel the readonly propoty of the file.
    ## Params:
    - `f1` - The name of the first file, it will be a string(path).
    - `f2` - The name of the second file, it will be a string(path).
    """
    if f1 == f2:
        raise IOError("The file names is same!")
    if not path.exists(f1):
        raise FileNotFoundError(f"The file {f1} is not exists!")
    if not (path.isfile(f1) and path.isfile(f2)):
        raise IOError(f"The {f1} or {f2} is not a file!")
    try:
        os.chmod(f1, stat.S_IWRITE)
        shutil.copyfile(f1, f2)
    except Exception as e:
        raise Exception(f"Unable to copy file: {e}!")


def copyFolder(d1: str, d2: str) -> typing.NoReturn:
    """
    # CopyFolder function
    Copy a folder.
    No returns.
    ## Params:
    - `d1` - The name of the first dir of the folder, it will be a string(path).
    - `d2` - The name of the second dir of the folder, it will be a string(path).
    """
    if d1 == d2:
        raise IOError("The dir names is same!")
    if not path.exists(d1):
        raise FileNotFoundError(f"The dir {d1} is not exists!")
    if not (path.isdir(d1) and path.isdir(d2)):
        raise OSError(f"The {d1} or {d2} is not a dir!")
    try:
        shutil.copytree(d1, d2)
    except Exception as e:
        raise Exception(f"Unable to copy folder: {e}!")


def getDirs(dir_: str = "./") -> typing.List[str]:
    """
    # GetDirs function
    Get the dir names and file names from a dir ( just in the top of the dir ).
    Returns a list of the file names and dir names.
    ## Params:
    - `dir` The dir that you want to see files, default `./` (this dir).
    """
    return os.listdir(dir_)


def getAllDirs(dir_: str = "./", listname: list = []) -> typing.List[str]:
    """
    # GetAllDirs function
    Get the dir names and file names from a dir.
    Returns a list of the file names and dir names.
    ## Params:
    - `dir` The dir that you want to see files, default `./` (this dir).
    - `listname` The list to return, default a blank list.
    """
    for file in os.listdir(dir_):
        file_path = path.join(dir_, file)
        if path.isdir(file_path):
            getAllDirs(file_path, listname)
        else:
            listname.append(file_path)
    return listname


def getFiles(dir_: str = "./", listname: list = []) -> typing.List[str]:
    """
    # GetFiles function
    Get the file names from a dir.
    Returns a list of the file names and dir names.
    ## Params:
    - `dir` The dir that you want to see files, default `./` (this dir).
    - `listname` The list to return, default a blank list.
    """
    for file in os.listdir(dir_):
        file_path = path.join(dir_, file)
        if path.isdir(file_path):
            getAllDirs(file_path, listname)
        elif path.isfile(file):
            listname.append(file_path)
    return listname


if sys.platform == "win32":
    def readTempFiles(tmp: str = "*", dirreturn: bool = True) -> typing.List[str]:
        """
        # ReadTempFiles function
        Read file names from a temp ( just for Windows ).
        Returns a list of the file names (dir names) in the a temp.
        ## Params:
        - `tmp` The dir of the temp, it will be a string, default `*` (all).
        - `dirreturn` It will be a boolean, if it is `True`, 
        if it is `True`, system will returns dir names and file names,
        if it is `False`, system will just returns the file names.
        """
        tmp_path = path.join("%TEMP%", tmp) if tmp != "*" else "%TEMP%"
        if dirreturn:
            return getAllDirs(tmp_path)
        else:
            return getFiles(tmp_path)

    def clearTempFiles(tmp: str = "*") -> typing.NoReturn:
        """
        # ClearTempFiles function
        Clear file names from a temp ( just for Windows ).
        ## Params:
        - `tmp` The dir of the temp, it will be a string, default `*` (top dir).
        """
        tmp_path = path.join("%TEMP%", tmp) if tmp != "*" else "%TEMP%"
        if path.isfile(tmp_path):
            delFile(tmp_path)
        elif path.isdir(tmp_path):
            delFolder(tmp_path)
        else:
            raise IOError("The type of the file is not in [file, dir]")

    def writeToTemp(tmp: str, filename: str, content: bytes) -> typing.NoReturn:
        """
        # ClearTempFiles function
        Clear file names from a temp ( just for Windows ).
        ## Params:
        - `tmp` The dir of the temp, it will be a string, default `*` (top dir).
        - `filename` The file name of the file name.
        - `content` The byte content that will write into the file.
        """
        tmp_path = path.join("%TEMP%", tmp, filename) if tmp != "*" else "%TEMP%"
        if not path.exists(tmp_path):
            tmp_top_path = "\\".join(tmp_path.split("\\")[:-1])
            newFolder(tmp_top_path)
        with newFile(tmp_path, True, True) as file:
            file: typing.BinaryIO
            file.write(content)
