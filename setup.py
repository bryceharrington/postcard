#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name             = 'postcard',
    version          = '0.1',
    url              = 'none',
    author           = 'Bryce Harrington',
    author_email     = 'bryce@bryceharrington.org',
    description      = 'Inserts data to Trello.com boards',
    long_description = open('README.md', 'rt').read(),
    platforms        = ['any'],
    requires         = ['argparse',
                        'ruamel',
                        'requests',
                        'requests_oauthlib'],
    packages         = ['postcard'],
    package_data     = { },
    data_files       = [ ],
    scripts          = ['scripts/postcard'],

    tests_require    = ['pytest'],
)
