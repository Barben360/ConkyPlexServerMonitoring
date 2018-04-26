#!/usr/bin/env python3
import plexstatereader
import sys
import argparse
import time

parser = argparse.ArgumentParser(description='Get Video Percentage Elapsed')
parser.add_argument('index', metavar='P', help='Index')
parser.add_argument('xmlfile', metavar='X', help='Temp Plex XML file path')
args = parser.parse_args()

time.sleep(2)

tree = plexstatereader.getCurrentSessions(args.xmlfile)
info = plexstatereader.getSessionsInfo(tree)
if int(args.index) < len(info["Videos"]):
    ems = float(info["Videos"][int(args.index)]['Elapsed time ms'])
    tms = float(info["Videos"][int(args.index)]['Total time ms'])
    perc = ems/tms*100.0
else:
    perc = 0.0


sys.stdout.write(str(perc))
sys.stdout.flush()
