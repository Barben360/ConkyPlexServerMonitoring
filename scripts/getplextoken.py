#!/usr/bin/env python3
import plexstatereader
import sys
import argparse

parser = argparse.ArgumentParser(description='Get Plex Server token')
parser.add_argument('plexcred', metavar='P', help='Credentials file')
args = parser.parse_args()
credentials = plexstatereader.readCredFile(args.plexcred)
token = plexstatereader.getToken(credentials)

sys.stdout.write(token)
sys.stdout.flush()
