# -*- coding: utf-8 -*-
from baseapi import BaseApi


class Client(BaseApi):
    dataservername = 'FinCFODataBR'
    def create(self,**kwargs):
        codcoligada_contexto = kwargs.get('codcoligada_contexto')
        if not codcoligada_contexto:
            codcoligada_contexto =  kwargs.get('codcoligada')

        return super(Client, self).create({
            'NewDataSet': {
                'FCFO': {
                    'CODEXTERNO': kwargs.get('codexterno'),
                    'CODCOLIGADA': kwargs.get('codcoligada'),
                    'CODCFO': -1,
                    'CLASSIFICACAO', kwargs.get('classificacao'),
                    'CATEGORIA', kwargs.get('categoria'),
                    'CGCCFO': kwargs.get('cpf'),
                    'TIPORUA': kwargs.get('tipo_rua'),
                    'TIPOBAIRRO': kwargs.get('tipo_bairro'),
                    'BAIRRO': kwargs.get('bairro'),
                    'RUA': kwargs.get('rua'),
                    'NUMERO': kwargs.get('numero'),
                    'ESTADO': kwargs.get('estado'),
                    'CODMUNICIPIO': kwargs.get('codigo_municipio'),
                    'PAIS': 1,
                    'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000'.format(kwargs.get('data_nascimento'),
                    'NOME': kwargs.get('nome'),
                    'NOMEFANTASIA': kwargs.get('nome'),
                    'PAGREC': kwargs.get('pagrec'),
                    'ATIVO': True,
                    'PESSOAFISOUJUR': 'f',
                    'IDCFO': -1
                }
            }
        }, 'CODCOLIGADA={}'.format(codcoligada_contexto))
