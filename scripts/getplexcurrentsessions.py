#!/usr/bin/env python3
import plexstatereader
import argparse
import sys
import time

parser = argparse.ArgumentParser(description='Get Plex Server current sessions')
parser.add_argument('xmlfile', metavar='X', help='Temp Plex XML file path')
args = parser.parse_args()

time.sleep(2)

tree = plexstatereader.getCurrentSessions(args.xmlfile)
count = plexstatereader.getNumberOfCurrentSessions(tree)

sys.stdout.write(str(count))
sys.stdout.flush()
