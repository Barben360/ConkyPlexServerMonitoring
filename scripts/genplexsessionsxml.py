#!/usr/bin/env python3
import plexstatereader
import argparse

parser = argparse.ArgumentParser(description='Generate Plex Sessions XML')
parser.add_argument('plexcred', metavar='C', help='Plex credentials')
parser.add_argument('xmlfile', metavar='X', help='Temp Plex XML file path')
args = parser.parse_args()

credentials = plexstatereader.readCredFile(args.plexcred)
token = plexstatereader.getToken(credentials)
plexstatereader.genXML(credentials, token, args.xmlfile)
