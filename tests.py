#! /usr/bin/python3
#-*-coding:utf8

import os
import sys
 
dossier = os.path.dirname(os.path.abspath(__file__))

# print(dossier)

while not dossier.endswith('Workspace'):
    dossier = os.path.dirname(dossier)
    # print(dossier)

 
dossier = os.path.dirname(dossier)

if dossier not in sys.path:
    sys.path.append(dossier)

