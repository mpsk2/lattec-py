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

pkg = __import__('lattec')

setup(
    name='lattec',
    author=pkg.__author__,
    author_email=pkg.__author_email__,
    version=pkg.__version__,
    packages=setuptools.find_packages(),
    long_description=open('README.rst').read(),
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Compilers',
    ],
)