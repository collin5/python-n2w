#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="n2w",
    version="0.1.1",
    description="Python library to convert numbers to words",
    long_description="Python library to covnert numbers to words",
    kewords='library numbers algorithim words convert',
    author="Collins Abitekaniza",
    author_email="abtcolns@gmail.com",
    url="https://github.com/collin5/python-n2w",
    packages=['n2w'],
    install_requires=[
        'markdown'
    ],
    include_package_data=True,
    zip_safe=False
)
