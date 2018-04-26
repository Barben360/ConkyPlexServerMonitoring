#!/usr/bin/env python3
import plexstatereader
import sys
import argparse
import time

parser = argparse.ArgumentParser(description='Get Video User')
parser.add_argument('index', metavar='P', help='Index')
parser.add_argument('xmlfile', metavar='X', help='Temp Plex XML file path')
args = parser.parse_args()

time.sleep(2)

tree = plexstatereader.getCurrentSessions(args.xmlfile)
info = plexstatereader.getSessionsInfo(tree)
if int(args.index) < len(info["Videos"]):
    user = info["Videos"][int(args.index)]['User']
else:
    user = 'no user'


sys.stdout.write(user)
sys.stdout.flush()

