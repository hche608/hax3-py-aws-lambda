#!/usr/bin/env python
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="basicLambda",
    version="0.0.1",
    author="Hao Chen",
    description="An example of how to set up pytest.",
    license="GNU",
    keywords="example pytest",
    packages=['basicLambda', 'tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Alpha",
    ], install_requires=['requests', 'mockito']
)
