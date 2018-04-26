#!/usr/bin/env python3
from plexapi.myplex import MyPlexAccount
import urllib.request
import urllib.parse
import os
from lxml import etree as ET


def readCredFile(credfile):
    cred = dict()
    with open(credfile, 'r') as file_in:
        cred["username"] = file_in.readline().strip()
        cred["password"] = file_in.readline().strip()
        cred["baseurl"] = file_in.readline().strip()
        return cred


def getToken(cred):
    account = MyPlexAccount(cred["username"],cred["password"])
    return account._token


def genXML(cred, token, filename):
    response = urllib.request.urlopen(urllib.parse.urljoin(cred["baseurl"], "status/sessions?X-Plex-Token=" + token))
    data = response.read().decode("UTF-8")
    with open(filename, "w") as file_out:
        file_out.write(data)


def getCurrentSessions(filename):
    if os.path.exists(filename):
        tree = ET.parse(filename)
    else:
        foostr = '<MediaContainer size="0"></MediaContainer>'
        tree = ET.fromstring(foostr)
    return tree


def getNumberOfCurrentSessions(tree):
    tmp = tree.xpath("/MediaContainer")
    if not tmp:
        ret = 0
    else:
        ret = int(tmp[0].attrib['size'])
    return ret

def getSessionsInfo(tree):
    info = dict()
    info["Videos"] = []
    info["Photos"] = []
    videos = tree.xpath("/MediaContainer/Video")
    photos = tree.xpath("/MediaContainer/Photo")
    for elt in videos:
        eltTmp = dict()
        eltTmp["Type"] = "Video"
        eltTmp["User"] = elt.xpath("User")[0].attrib['title']
        eltTmp["Title"] = elt.attrib['title']
        eltTmp["Total time ms"] = elt.attrib['duration']
        eltTmp["Elapsed time ms"] = elt.attrib['viewOffset']
        info["Videos"].append(eltTmp)
    for elt in photos:
        eltTmp = dict()
        eltTmp["Type"] = "Photo"
        eltTmp["User"] = elt.xpath("User")[0].attrib['title']
        info["Photos"].append(eltTmp)
    return info


#utils
def mstohours(ms):
    s = ms/1000
    m, s = divmod(s, 60)
    h, m = divmod(m,60)
    return h, m, s

