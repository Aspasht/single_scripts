#!/usr/bin/python3

'''
This script takes as file and execute dirhunt tool. Must have dirhunt preinstalled.
'''

import sys
import os


def tester(*args):
    cmd = "dirhunt {0}".format(*args)
    print(cmd)


urls = []
with open(sys.argv[1], 'r') as f:
    for url in f:
        url=url.strip()
        urls.append(url)


cmd = os.system("'dirhunt' '{0}' --to-file out_dirhunt.json".format(*urls))

print(cmd)
