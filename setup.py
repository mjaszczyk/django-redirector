#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='django_redirector',
      version='1',
      description='Django Redirector',
      packages=find_packages(),
      install_requires=[
          'django>=1.3',
          'south==0.7.6',
      ])
