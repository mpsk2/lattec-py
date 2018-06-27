#!/usr/bin/env python3

from distutils.core import setup
import setuptools

setup_requires = [
    'antlr4-python3-runtime',
    'pytest-runner',
]

tests_require = [
    'pytest',
    'pytest-cov',
]

setup(
    name='lattec',
    version='0.1dev',
    packages=setuptools.find_packages('src'),
    package_dir={'':'src'},
    long_description=open('README.rst').read(),
    setup_requires=setup_requires,
    tests_require=tests_require,
)

