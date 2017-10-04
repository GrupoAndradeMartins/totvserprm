# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='totvserprm',
      version='1.0.5',
      description='API para webservices do TOTVS ERP RM.',
      url='http://github.com/grupoandrademartins/totvserprm',
      contributors=[
       ['Rafael G. Winter', 'rafael@rafaelgontijo.com', 'author'],
       ['Túlio Cesar Martins', 'funroll.loops@gmail.com', 'author'],
      ],
      license='MIT',
      packages=['totvserprm'],
      install_requires=[
          'dicttoxml',
          'lxml',
          'requests',
          'zeep'
      ],
      keywords='totvs webservice erp rm soap',
      zip_safe=False)
