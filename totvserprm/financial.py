# -*- coding: utf-8 -*-
from baseapi import BaseApi

class Client(BaseApi):
    dataservername = 'FinCFODataBR'
    def create(self, codexterno, codcoligada, data_nascimento, nome, pagrec, codcoligada_contexto=None):
        if not codcoligada_contexto:
            codcoligada_contexto = codcoligada
        return super(Student, self).create({
            'NewDataSet': {
                'FCFO': {
                    'CODEXTERNO': codexterno,
                    'CODCOLIGADA': codcoligada,
                    'CODCFO': -1,
                    'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000',
                    'NOME': nome,
                    'NOMEFANTASIA': nome,
                    'PAGREC': pagrec,
                    'ATIVO': True,
                    'PESSOAFISOUJUR': 'f',
                    'IDCFO': -1
                }
            }
        }, 'CODCOLIGADA={}'.format(codcoligada_contexto))
