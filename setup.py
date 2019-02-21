from distutils.core import setup
from setuptools import find_packages

setup(name='chainside-webpos-sdk',
      version='1.0.0',
      packages=find_packages(),
      install_requires=['moveax-sdk-boilerplate'],
      )
