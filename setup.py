# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='totvserprm',
      version='1.0.6',
      description='API para webservices do TOTVS ERP RM.',
      url='http://github.com/grupoandrademartins/totvserprm',
      authors=[
        'Rafael G. Winter <rafael@rafaelgontijo.com>',
        'Túlio Cesar Martins <funroll.loops@gmail.com>'
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
