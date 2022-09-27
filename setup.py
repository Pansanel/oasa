#! /usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

setup(
    name='oasa',
    version = '0.14.0',
    description = "OASA is a free cheminformatics library written in Python",
    author = "Beda Kosata",
    author_email = "beda@zirael.org",
    url = "http://bkchem.zirael.org/oasa_en.html",
    license = "GNU GPL",
    long_description = "OASA is a free cheminformatics library written in Python",
    packages=[ 'oasa', 'oasa/graph'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry'
    ],
)
