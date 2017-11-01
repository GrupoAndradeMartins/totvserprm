# -*- coding: utf-8 -*-
from auth import create_service
from dicttoxml import dicttoxml
from lxml import objectify
from totvserprm.utils import normalize_xml


class BaseApi(object):
    dataservername = ''

    def __init__(self, server, username, password):
        self.service = create_service(server, username, password)

    def create(self, dict, context):
        xml = dicttoxml(dict, attr_type=False)
        return self.service.SaveRecord(DataServerName=self.dataservername, XML=xml, Contexto=context)

    def get(self, codcoligada, id):
        primary_key = '{};{}'.format(codcoligada, id)
        return_from_api = self.service.ReadRecord(
            DataServerName=self.dataservername, PrimaryKey=primary_key, Contexto='CODCOLIGADA={}'.format(codcoligada))
        return_from_api = normalize_xml(return_from_api)
        return objectify.fromstring(return_from_api)
