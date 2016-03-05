# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='greenhouse',
    version=version,
    description='Custom app for managing the data entry, tracking and reporting for the Foxtrot Greenhouse. Will track greenhouse variables, water testing and nutrient/additive tracking.',
    author='Brandon Fox, Foxtrot',
    author_email='bfox@foxtrot.email',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
