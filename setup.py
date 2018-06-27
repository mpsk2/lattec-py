#!/usr/bin/env python3

from distutils.core import setup
import setuptools

setup_requires = [
    'pytest-runner',
]

tests_require = [
    'pytest',
]

setup(
    name='lattec',
    version='0.1dev',
    packages=['lattec'],
    package_dir={'':'src'},
    long_description=open('README.rst').read(),
    setup_requires=setup_requires,
    tests_require=tests_require,
)

