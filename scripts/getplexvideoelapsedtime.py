#!/usr/bin/env python3
import plexstatereader
import sys
import argparse
import time

parser = argparse.ArgumentParser(description='Get Video Elapsed Time')
parser.add_argument('index', metavar='P', help='Index')
parser.add_argument('xmlfile', metavar='X', help='Temp Plex XML file path')
args = parser.parse_args()

time.sleep(2)

tree = plexstatereader.getCurrentSessions(args.xmlfile)
info = plexstatereader.getSessionsInfo(tree)
if int(args.index) < len(info["Videos"]):
    h, m, s = plexstatereader.mstohours(int(info["Videos"][int(args.index)]['Elapsed time ms']))
    etime = ('%.1d' % h) + ':' + ('%.2d' % m) + ':' + ('%.2d' % s)
else:
    etime = '--'

sys.stdout.write(etime)
sys.stdout.flush()
