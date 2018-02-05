# -*- coding: utf-8 -*-
from totvserprmgam.baseapi import BaseApi


class EnablingStudent(BaseApi):
    dataservername = 'EduHabilitacaoAlunoData'

    def create(self, **kwargs):
        return super(EnablingStudent, self).create({
            'SHabilitacaoAluno': {
                'CODHABILITACAO': 1, 
                'CODCOLIGADA': kwargs.get('codcoligada'), 
                'RA': kwargs.get('ra'), 
                'CODFILIAL': 1, 
                'CODCAMPUS': kwargs.get('codcampus'), 
                'IDHABILITACAOFILIAL': kwargs.get('idhabilitacaofilial'), 
                'CODSTATUS': kwargs.get('codstatus'), 
                'CODCURSO': kwargs.get('codcurso'), 
                'CODGRADE': 1
            }, 
            'SHabilitacaoAlunoCompl': {
                'IDHABILITACAOFILIAL': kwargs.get('idhabilitacaofilial'), 
                'CODCOLIGADA': kwargs.get('codcoligada'), 
                'RA': kwargs.get('ra')
            }
        }, 'CODCOLIGADA={0};IDHABILITACAOFILIAL={1};RA={2}'.format(kwargs.get('codcoligada'), kwargs.get('idhabilitacaofilial'), kwargs.get('ra')))






        