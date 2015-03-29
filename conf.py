import os
import re
__author__ = 'vladymyr'


def getUrlPath():
    dir = os.path.dirname(__file__)
    urlsPath = (os.path.join(dir, 'source/urls_uk.xml')).replace("\\", "/")
    # print("path of url file: ", urlsPath)
    return urlsPath

def getResultPath():
    dir = os.path.dirname(__file__)
    Path = (os.path.join(dir, 'source/result.xml')).replace("\\", "/")
    return Path

def getInfoPath():
    dir = os.path.dirname(__file__)
    return (os.path.join(dir, 'gns/data_uk.txt')).replace("\\", "/")


def getInfoList():
    with open(getInfoPath(), "r") as infoFile:
        data = infoFile.read()
    return re.findall(r"[\w']+", data.decode('utf8'), re.U)
