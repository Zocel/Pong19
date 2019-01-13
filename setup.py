#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    author="Yann Michel Le Coz",
    author_email='yann.lecoz@ynov.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Natural Language :: French",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Cette application permet de jouer au jeu d'arcade Pong.",
    license="GNU General Public License v3",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='Pong19',
    name='Pong19',
    packages=find_packages(),
    url='https://github.com/Zocel/Pong19',
    version = '0.1.2',
    zip_safe=False,
)
