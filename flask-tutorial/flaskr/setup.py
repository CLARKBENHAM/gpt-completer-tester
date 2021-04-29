# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:00:03 2020

@author: student
"""
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)


