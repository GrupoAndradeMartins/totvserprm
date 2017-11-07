# -*- coding: utf-8 -*-
from datetime import datetime
from baseapi import BaseApi


class Client(BaseApi):
    dataservername = 'FinCFODataBR'
    def create(self,**kwargs):
        return super(Client, self).create({
            'NewDataSet': {
                'FCFO': {
                    'ATIVO': kwargs.get('ativo'),
                    'CODCFO': -1,
                    'IDCFO': -1,
                    'CODEXTERNO': kwargs.get('codexterno'),
                    'CODCOLIGADA': kwargs.get('codcoligada'),
                    'CODCOLTCF': kwargs.get('codcoligada'),
                    'CGCCFO': kwargs.get('cpf_cnpj'),
                    'TIPORUA': kwargs.get('tipo_rua'),
                    'TIPOBAIRRO': kwargs.get('tipo_bairro'),
                    'BAIRRO': kwargs.get('bairro'),
                    'RUA': kwargs.get('rua'),
                    'NUMERO': kwargs.get('numero'),
                    'CEP': kwargs.get('cep'),
                    'CODETD': kwargs.get('estado'),
                    'CIDADE': kwargs.get('cidade'),
                    'CODMUNICIPIO': kwargs.get('codigo_municipio'),
                    'PAIS': kwargs.get('cod_pais'),
                    'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000'.format(kwargs.get('data_nascimento')),
                    'NOME': kwargs.get('nome'),
                    'EMAIL': kwargs.get('email'),
                    'NOMEFANTASIA': kwargs.get('nome'),
                    'PAGREC': kwargs.get('classificacao'),
                    'PESSOAFISOUJUR': kwargs.get('categoria'),
                    'CODTCF': kwargs.get('tipo_cliente'),
                }
            }
        }, 'CODCOLIGADA={}'.format(kwargs.get('codcoligada_contexto')))


class Billet(BaseApi):
    dataservername = 'FinLanBoletoData'
    def create(self,**kwargs):
        return super(Billet, self).create({
            'FinLAN': {
                'FLAN': {
                    'CODCOLIGADA': kwargs.get('codcoligada'),
                    'IDLAN': -1,
                    'PAGREC': kwargs.get('classificacao'),
                    'CODTDO': kwargs.get('tipo_documento'),
                    'DATAVENCIMENTO': kwargs.get('data_vencimento'),
                    'DATAEMISSAO': "{:%d/%m/%Y %H:%M:%S}".format(datetime.now()),
                    'VALORORIGINAL': kwargs.get('valor'),
                    'CODCOLCFO': kwargs.get('codcoligada_cfo'),
                    'CODCFO': kwargs.get('codcliente'),
                    'CODFILIAL': kwargs.get('codfilial'),
                    'SERIEDOCUMENTO': '@@@',
                    'CODMOEVALORORIGINAL': 'R$',
                    'HISTORICO': kwargs.get('historico'),
                    'CODCCUSTO': kwargs.get('centro_custo'),
                },
                'FLANCOMPL':{
                    'CODCOLIGADA': kwargs.get('codcoligada'),
                    'IDLAN': -1,
                    'IDVENDEDOR': kwargs.get('id_vendedor')
                },
                'FLANRATCCU':{
                    'IDRATCCU': -1,
                    'CODCOLIGADA': kwargs.get('codcoligada'),
                    'IDLAN': -1,
                    'CODCCUSTO': kwargs.get('centro_custo'),
                    'VALOR': kwargs.get('valor'),
                    'CODCOLNATFINANCEIRA': kwargs.get('codcoligada_fin'),
                    'CODNATFINANCEIRA': kwargs.get('codnatfinanceira'),
                }
            }
        }, 'CODCOLIGADA={}'.format(kwargs.get('codcoligada_contexto')))


class CostCenter(BaseApi):
    dataservername = 'CtbCCustoData'
