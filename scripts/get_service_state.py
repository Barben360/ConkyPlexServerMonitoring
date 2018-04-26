#!/usr/bin/env python3
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(description='Prints service state')
parser.add_argument('servicename', metavar='name', help='service name')
args = parser.parse_args()

service_state = subprocess.run(["systemctl", "status", args.servicename], stdout=subprocess.PIPE)

search_res = service_state.stdout.find(b"active (running)")

if search_res >= 0:
	search_res = "Running"
else:
	search_res = "Off"

sys.stdout.write(search_res)
sys.stdout.flush()
