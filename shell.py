#!/usr/bin/env python3

import os
import shutil
from subprocess import call

'''
    Module to provide shell-like commands
'''
def copy(source, dest):
    shutil.copy(source, dest)

def get_home():
    return os.path.expanduser('~')
