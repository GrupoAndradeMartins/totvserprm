# -*- coding: utf-8 -*-
from auth import create_service
from dicttoxml import dicttoxml
from lxml import objectify


class Student:
    def __init__(self, server, username, password):
        self.service = create_service(server, username, password)

    def create(self, codcoligada, codtipocurso, data_nascimento, estado_natal, naturalidade, nome, ra):
        aluno = dicttoxml({
            'NewDataSet':{
              'SAluno':{
                'CODCOLIGADA': codcoligada,
                'CODTIPOCURSO': codtipocurso,
                'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000',
                'ESTADONATAL': estado_natal,
                'NATURALIDADE': naturalidade,
                'NOME': nome,
                'RA':ra,
                }
            }
        },attr_type=False)

        return self.service.SaveRecord(DataServerName='EduAlunoData', XML=aluno, Contexto='')

    def get(self, codcoligada, ra):
        primary_key = '{};{}'.format(codcoligada, ra)
        aluno = self.service.ReadRecord(DataServerName='EduAlunoData', PrimaryKey=primary_key, Contexto='')
        return objectify.fromstring(aluno)
