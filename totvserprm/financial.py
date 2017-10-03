# -*- coding: utf-8 -*-
from auth import create_service
from dicttoxml import dicttoxml
from lxml import objectify


class Client:
    def __init__(self, server, username, password):
        self.service = create_service(server, username, password)

    def create(self, codexterno, codcoligada, codcfo, data_nascimento, idcfo, nome, pagrec):
        client_xml = dicttoxml({
            'NewDataSet': {
                'FCFO': {
                    'CODEXTERNO': codexterno,
                    'CODCOLIGADA': codcoligada,
                    'CODCFO': codcfo,
                    'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000',
                    'NOME': nome,
                    'NOMEFANTASIA': nome,
                    'PAGREC': pagrec,
                    'ATIVO': True,
                    'PESSOAFISOUJUR': 'f',
                    'IDCFO': idcfo
                }
            }
        }, attr_type=False)

        return self.service.SaveRecord(DataServerName='FinCFODataBR', XML=client_xml, Contexto='')

    def get(self, codcoligada, codcfo):
        primary_key = '{};{}'.format(codcoligada, codcfo)
        client = self.service.ReadRecord(
            DataServerName='FinCFODataBR', PrimaryKey=primary_key, Contexto='')
        return objectify.fromstring(client)
