#!-*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()
CHANGES = open(os.path.join(here, 'CHANGELOG')).read()

setup(
    name='pytimecode',
    version='0.2.0',
    description="SMPTE Time Code Manipulation Library",
    long_description='%s\n\n%s' % (README, CHANGES),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    author=['Joshua Banton', 'Erkan Ozgur Yilmaz'],
    author_email=['bantonj@gmail.com', 'eoyilmaz@gmail.com'],
    url='http://bantonj.wordpress.com/software/open-source/',
    keywords=['video', 'timecode', 'smpte'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
)
