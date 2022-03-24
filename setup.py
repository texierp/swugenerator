# SWUGenerator, SWU Package Generator for SWUpdate
#
# Copyright (C) 2022 Stefano Babic
#
# SPDX-License-Identifier: GPLv3

from setuptools import setup, find_packages

setup(
    name='swugenerator',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/swugenerator',
    license='GPLv3',
    author='Stefano Babic',
    author_email='stefano.babic@babic.homelinux.org',
    description='SWU Package generator for SWUpdate',
    entry_points={
        'console_scripts': [
            'swugenerator=swugenerator.main:main',
        ],
    },

    install_requires=[
        'libconf~=2.0.1',
        'setuptools~=57.0.0',
        'crypto~=1.4.1',
    ],

    python_requires='>=3.6',
)