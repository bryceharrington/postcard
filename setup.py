#!/usr/bin/python

from distutils.core import setup
from distutils.command.install_data import install_data
from subprocess import call

import glob
import os
import re

setup(
    name             = 'postcard',
    version          = '0.1',
    url              = 'none',
    author           = 'Bryce Harrington',
    author_email     = 'bryce@ubuntu.com',
    description      = 'Inserts data to Trello.com boards',
    long_description = open('README.md', 'rt').read(),
    platforms        = ['any'],
    requires         = ['argparse', 'ruamel'],
    packages         = [
        'postcard'
        ],
    package_data     = { },
    data_files       = [ ],
    scripts          = [ "bin/postcard" ],
)
