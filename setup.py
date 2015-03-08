#!/usr/bin/env python

import sys
import os
from distutils.core import setup

setup(name='pidfile',
      version='0.1.1',
      description='A Pidfile Context Manager compatible with python-daemon\'s DaemonContext()',
      author="Brian Hatfield",
      author_email='bmhatfield@gmail.com',
      url='https://github.com/bmhatfield/python-pidfile.git',
      license='MIT',
      py_modules=['pidfile'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
      ]
     )
