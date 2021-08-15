#!/usr/bin/python3
import sys
import os
import re
from os import listdir
from os.path import splitext, join

def fnNodeParser(filePath):


try:
    varCmplDir = sys.argv[1]
    tplInfoFiles = ("info_cmd_node.log", "info_cmd_node_ncore_flattened.log", "info_cmd_node_tile_flattened.log")
    dictInfoFiles = { tplInfoFiles[0]: tplInfoFiles[0] in listdir(varCmplDir),
                      tplInfoFiles[1]: tplInfoFiles[1] in listdir(varCmplDir),
                      tplInfoFiles[2]: tplInfoFiles[2] in listdir(varCmplDir)
                    }

except:




