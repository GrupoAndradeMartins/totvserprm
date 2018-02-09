# -*- coding: utf-8 -*-
from totvserprmgam.baseapi import BaseApi


class Student(BaseApi):
    dataservername = 'EduAlunoData'

    def create(self, **kwargs):
        
        if kwargs.get('codpessoa') == -1:
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
                        'CPF': kwargs.get('cpf'),
                        'RA': 0,
                        'CODCFO': kwargs.get('codcliente'),
                        'CODCOLCFO': kwargs.get('codcoligada_cliente'),
                        'CODTIPORUA': kwargs.get('tipo_rua'),
                        'CODTIPOBAIRRO': kwargs.get('tipo_bairro'),
                        'BAIRRO': kwargs.get('bairro'),
                        'RUA': kwargs.get('rua'),
                        'NUMERO': kwargs.get('numero'),
                        'CEP': kwargs.get('cep'),
                        'ESTADO': kwargs.get('estado'),
                        'CIDADE': kwargs.get('cidade'),
                        'CODMUNICIPIO': kwargs.get('codigo_municipio'),
                        'PAIS': kwargs.get('pais'),
                        'SEXO': kwargs.get('sexo'),
                        'CODTIPOALUNO': '10',
                        'EMAIL': kwargs.get('email'),
                        'TELEFONE1': kwargs.get('telefone1'),
                        'TELEFONE2': kwargs.get('telefone2'),
                        'TELEFONE3': kwargs.get('telefone3'),
                        'CODPESSOA': kwargs.get('codpessoa'),
                    },
                    'SAlunoCompl': {
                        'CODCOLIGADA': kwargs.get('codcoligada'),
                        'RA': 0,
                        'PLANOPGTO': kwargs.get('planopagamento'),
                        'OBSFINANCEIRO': kwargs.get('obsfinanceiro')
                    }
                    # 'SHabilitacaoAluno': {
                    #     'CODCOLIGADA': kwargs.get('codcoligada'),
                    #     'IDHABILITACAOFILIAL': 383,
                    #     'RA': -1,
                    #     'CODCURSO': kwargs.get('codcurso'),
                    #     'CODHABILITACAO': 1,
                    #     'CODGRADE': 1
                    # }
                }
            }, 'CODCOLIGADA={}'.format(kwargs.get('codcoligada')))
        else:
            return super(Student, self).create({
                'NewDataSet': {
                    'SAluno': {
                        'CODCOLIGADA': kwargs.get('codcoligada'),
                        'CODTIPOCURSO': kwargs.get('codtipocurso'),
                        'NOME': kwargs.get('nome'),
                        'RA': 0,
                        'CODCFO': kwargs.get('codcliente'),
                        'CODCOLCFO': kwargs.get('codcoligada_cliente'),
                        'CODIGO': kwargs.get('codpessoa')
                    },
                    'SAlunoCompl': {
                        'CODCOLIGADA': kwargs.get('codcoligada'),
                        'RA': 0,
                        'PLANOPGTO': kwargs.get('planopagamento'),
                        'OBSFINANCEIRO': kwargs.get('obsfinanceiro')
                    },
                    # 'SHabilitacaoAluno': {
                    #     'CODCOLIGADA': kwargs.get('codcoligada'),
                    #     'IDHABILITACAOFILIAL': 383,
                    #     'RA': -1,
                    #     'CODCURSO': kwargs.get('codcurso'),
                    #     'CODHABILITACAO': 1,
                    #     'CODGRADE': 1
                    # }
                }
            }, 'CODCOLIGADA={}'.format(kwargs.get('codcoligada')))