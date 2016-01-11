#!/usr/bin/env python

from setuptools import setup, find_packages


install_requires = [
    'python2-pythondialog',
    'requests',
]


scripts = [
    'scripts/anansi-menu.py',
    'scripts/anansi-fetchconfig.py',
]


setup(
    name="anansi_menu",
    version="0.10",
    packages=find_packages(),
    install_requires=install_requires,
    scripts=scripts,
)
