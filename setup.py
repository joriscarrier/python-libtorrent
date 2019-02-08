#!/usr/bin/env python

from distutils.core import setup
from distutils.dir_util import copy_tree

import os
import platform
import shutil

try:
    os.mkdir('build')
except BaseException:
    pass
try:
    shutil.rmtree('build/lib')
except BaseException:
    pass
try:
    os.mkdir('build/lib')
except BaseException:
    pass
try:
    os.mkdir('libtorrent')
except BaseException:
    pass

copy_tree(platform.system(), 'build/lib')

setup(
    name='python-libtorrent',
    version='1.1.12',
    author='Arvid Norberg',
    author_email='arvid@libtorrent.org',
    description='Python bindings for libtorrent-rasterbar',
    long_description='Python bindings for libtorrent-rasterbar',
    url='http://libtorrent.org',
    platforms=[platform.system() + '-' + platform.machine()],
    license='BSD',
    packages=['libtorrent'],
    ext_modules=None
)
