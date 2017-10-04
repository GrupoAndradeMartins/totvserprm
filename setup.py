# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='totvserprm',
      version='1.0.4',
      description='API para webservices do TOTVS ERP RM.',
      url='http://github.com/grupoandrademartins/totvserprm',
      author='Rafael G. Winter, Túlio Cesar Martins',
      author_email='gontijobh@gmail.com, funroll.loops@gmail.com',
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
