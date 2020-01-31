# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='gfdemo',
    version='0.1.0',
    description='Sample package for gitflow demo',
    long_description=readme,
    author='xxxxx',
    author_email='xxxxx@yahoo.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

