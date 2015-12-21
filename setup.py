#!/usr/bin/env python

from setuptools import setup, find_packages


install_requires = [
    'urwid',
    'requests'
]


scripts = [
    'scripts/cif-menu.py'
]


setup(
    name="cif_menu",
    version="0.1",
    packages=find_packages(),
    install_requires=install_requires,
    scripts=scripts,
)
