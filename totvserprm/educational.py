# -*- coding: utf-8 -*-
from totvserprm.baseapi import BaseApi


class Student(BaseApi):
    dataservername = 'EduAlunoData'

    def create(self, **kwargs):
        return super(Student, self).create({
            'NewDataSet': {
                'SAluno': {
                    'CODCOLIGADA': kwargs.get('codcoligada'),
                    'CODTIPOCURSO': kwargs.get('codtipocurso'),
                    'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000'.format(
                        kwargs.get('data_nascimento')),
                    'ESTADONATAL': kwargs.get('estado_natal'),
                    'NATURALIDADE': kwargs.get('naturalidade'),
                    'NOME': kwargs.get('nome'),
                    'RA': kwargs.get('ra'),
                    'CODCFO': kwargs.get('codcliente'),
                    'CODCOLCFO': kwargs.get('codcoligada_cliente')
                }
            }
        }, 'CODCOLIGADA={}'.format(kwargs.get('codcoligada')))
