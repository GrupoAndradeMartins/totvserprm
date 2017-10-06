# -*- coding: utf-8 -*-
from baseapi import BaseApi


class Client(BaseApi):
    dataservername = 'FinCFODataBR'
    def create(self,**kwargs):
        # codigo de coligada para o contexto, diferente do dataset
        codcoligada_contexto = kwargs.get('codcoligada_contexto')
        if not codcoligada_contexto:
            codcoligada_contexto =  kwargs.get('codcoligada')

        return super(Client, self).create({
            'NewDataSet': {
                'FCFO': {
                    'ATIVO': kwargs.get('ativo'),
                    # enviar -1 para que sejá criado de forma incremental
                    'CODCFO': -1,
                    'IDCFO': -1,
                    'CODEXTERNO': kwargs.get('codexterno'),
                    'CODCOLIGADA': kwargs.get('codcoligada'),
                    'CGCCFO': kwargs.get('cpf_cnpj'),
                    'TIPORUA': kwargs.get('tipo_rua'),
                    'TIPOBAIRRO': kwargs.get('tipo_bairro'),
                    'BAIRRO': kwargs.get('bairro'),
                    'RUA': kwargs.get('rua'),
                    'NUMERO': kwargs.get('numero'),
                    'ESTADO': kwargs.get('estado'),
                    'CODMUNICIPIO': kwargs.get('codigo_municipio'),
                    'PAIS': kwargs.get('cod_pais'),
                    'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000'.format(kwargs.get('data_nascimento')),
                    'NOME': kwargs.get('nome'),
                    'NOMEFANTASIA': kwargs.get('nome'),
                    'PAGREC': kwargs.get('classificacao'),
                    'PESSOAFISOUJUR': kwargs.get('categoria'),
                }
            }
        }, 'CODCOLIGADA={}'.format(codcoligada_contexto))
