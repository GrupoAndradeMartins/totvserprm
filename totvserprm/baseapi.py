# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from auth import create_service
from dicttoxml import dicttoxml
from lxml import objectify
from totvserprm.utils import ClassFactory, normalize_xml
from totvserprm.exceptions import ApiError

class BaseApi(object):
    dataservername = ''

    def __init__(self, server, username, password):
        self.service = create_service(server, username, password)

    def create(self, dict, context):
        xml = dicttoxml(dict, attr_type=False)
        response = self.service.SaveRecord(DataServerName=self.dataservername, XML=xml, Contexto=context)
        if len(response.split(';')) == 2:
            codcoligada = response.split(';')[0]
            element_id = response.split(';')[1]
            custom_class = ClassFactory(self.__class__.__name__, ['codcoligada', 'id'])
            return custom_class(codcoligada=codcoligada, id=element_id)
        else:
            raise ApiError('Error trying to create {}:\n{}'.format(self.__class__.__name__, response))

    def get(self, codcoligada, id):
        primary_key = '{};{}'.format(codcoligada, id)
        return_from_api = self.service.ReadRecord(
            DataServerName=self.dataservername, PrimaryKey=primary_key, Contexto='CODCOLIGADA={}'.format(codcoligada))
        return_from_api = normalize_xml(return_from_api)
        return objectify.fromstring(return_from_api)

    def all(self, codcoligada):
        return_from_api = self.service.ReadView(
            DataServerName=self.dataservername, Filtro='CODCOLIGADA={}'.format(
            codcoligada), Contexto='CODCOLIGADA={}'.format(codcoligada))
        return_from_api = normalize_xml(return_from_api)
        return objectify.fromstring(return_from_api)
