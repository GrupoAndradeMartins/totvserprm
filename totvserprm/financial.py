# -*- coding: utf-8 -*-
from datetime import datetime
from baseapi import BaseApi
from totvserprm.utils import number_doc

class Client(BaseApi):
    dataservername = 'FinCFODataBR'
    def create(self,**kwargs):
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
                    'CEP': kwargs.get('cep'),
                    'CODETD': kwargs.get('estado'),
                    'CIDADE': kwargs.get('cidade'),
                    'CODMUNICIPIO': kwargs.get('codigo_municipio'),
                    'PAIS': kwargs.get('cod_pais'),
                    'DTNASCIMENTO': '{:%Y-%m-%d}T03:00:00.000'.format(kwargs.get('data_nascimento')),
                    'NOME': kwargs.get('nome'),
                    'NOMEFANTASIA': kwargs.get('nome'),
                    'PAGREC': kwargs.get('classificacao'),
                    'PESSOAFISOUJUR': kwargs.get('categoria'),
                }
            }
        }, 'CODCOLIGADA={}'.format(kwargs.get('codcoligada')))


class Billet(BaseApi):
    dataservername = 'FinLanBoletoData'
    def create(self,**kwargs):
        return super(Billet, self).create({
            'FinLAN': {
                'FLAN': {
                    'CODCOLIGADA': kwargs.get('codcoligada'),
                    'IDLAN': -1,
                    'NUMERODOCUMENTO': number_doc(),
                    'NFOUDUP': 0,
                    'CLASSIFICACAO': 0,
                    'PAGREC': 1,
                    'STATUSLAN': 0,
                    'CODTDO': kwargs.get('tipo_documento'),
                    'DATAVENCIMENTO': kwargs.get('data_vencimento'),
                    'DATAEMISSAO': "{:%d/%m/%Y %H:%M:%S}".format(datetime.now()),
                    'VALORORIGINAL': kwargs.get('valor'),
                    'CODCOLCFO': 1,
                    'CODCFO': kwargs.get('codcliente'),
                    'CODFILIAL': kwargs.get('codfilial'),
                    'SERIEDOCUMENTO': '@@@',
                    'CODCXA': kwargs.get('conta'),
                    'CODMOEVALORORIGINAL': 'R$',
                    'NUMLOTECONTABIL': 0,
                    'NUMEROCONTABIL': 0,
                    'NUMCONTABILBX': 0,
                    'TIPOCONTABILLAN': 0,
                    'FILIALCONTABIL': 1,
                    'HISTORICO': kwargs.get('historico'),
                    'CODCCUSTO': kwargs.get('centro_custo'),
                },
            }
        }, 'CODCOLIGADA={}'.format(kwargs.get('codcoligada')))
