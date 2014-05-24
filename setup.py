#!/usr/bin/env python

import os
import sys
from glob import glob

sys.path.insert(0, os.path.abspath('src'))
from githubflow import __version__, __author__
try:
    from setuptools import setup
except ImportError:
    print "githubflow now needs setuptools in order to build. " + \
          "Install it using your package manager (usually python-setuptools) or via pip (pip install setuptools)."
    sys.exit(1)


from setuptools import find_packages

with open('README.md') as file:
    long_description = file.read()



setup(
    name='githubflow',
    author=__author__,
    author_email='steve@stevemorin.com',
    version=__version__,
    url='http://github.com/Demandcube/github-flow',
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ghf=githubflow.runner:cli
    ''',
    # py_modules=['runner'],
    package_dir = {'':'src'},
    packages=find_packages('src'),
    description='A command line interface to github'
                'uses the github apis commandline.',
    classifiers=[
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Bug Tracking',
    ],
    long_description=long_description,
)



