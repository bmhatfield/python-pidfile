#!/usr/bin/env python

import sys
import os
from distutils.core import setup

setup(name='pidfile',
      version='0.1.0',
      description='A Pidfile Context Manager compatible with python-daemon\'s DaemonContext()',
      author="Brian Hatfield",
      author_email='bmhatfield@gmail.com',
      url='https://github.com/bmhatfield/python-pidfile.git',
      py_modules=['pidfile'],
      license='MIT'
     )



