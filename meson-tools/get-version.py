#!/usr/bin/env python3

import subprocess
import pathlib

pwd = str(pathlib.Path(__file__).parent.resolve())

try:
    g = subprocess.run(['git', 'describe', '--dirty'], check=True, stdout=subprocess.PIPE).stdout.strip()
    print(g[1:].decode('utf8').replace('-', '.'))
except subprocess.CalledProcessError:
    print('what.even.is.versioning.lmfao')

