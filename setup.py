#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Pong19',
    version='0.1',
    author="Yann Michel Le Coz",
    author_email='yann.lecoz@ynov.com',
    description="Cette application permet de jouer au jeu d'arcade Pong.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Zocel/Pong19',
    packages=find_packages(),
    license="GNU General Public License v3",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Natural Language :: French",
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
