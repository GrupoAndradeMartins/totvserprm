# -*- coding: utf-8 -*-
from baseapi import BaseApi


class Student(BaseApi):
    dataservername = 'EduAlunoData'
    def create(self, codcoligada, codtipocurso, data_nascimento, estado_natal, naturalidade, nome, ra):
        return super(Student, self).create({
            'NewDataSet': {
                'SAluno': {
                    'CODCOLIGADA': codcoligada,
                    'CODTIPOCURSO': codtipocurso,
                    'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000',
                    'ESTADONATAL': estado_natal,
                    'NATURALIDADE': naturalidade,
                    'NOME': nome,
                    'RA': ra,
                }
            }
        }, 'CODCOLIGADA={}'.format(codcoligada))
