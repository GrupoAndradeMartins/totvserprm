# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='totvserprmgam',
    version='1.0.15',
    description='API para webservices do TOTVS ERP RM',
    url='https://github.com/grupoandrademartins/totvserprm',
    author='Rafael G. Winter, Túlio Cesar Martins',
    author_email='totvs-erp-rm-python@googlegroups.com',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
      'dicttoxml',
      'lxml',
      'requests',
      'zeep'
    ],
    keywords='totvs webservice erp rm soap api',
    long_description=long_description
)
