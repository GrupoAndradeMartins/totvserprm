# -*- coding: utf-8 -*-
from auth import create_service_sql
from dicttoxml import dicttoxml
from lxml import objectify


class ConsultSQL(object):
    def __init__(self, server, username, password):
        self.service = create_service_sql(server, username, password)

    def get(self, codcoligada, codsistema, codsentenca, parameters):
        parameters = u";".join(["=".join([key, str(val)]) for key, val in parameters.items()])
        return_from_api = self.service.RealizarConsultaSQL(
            codColigada=codcoligada, codSistema=codsistema, codSentenca=codsentenca, parameters=parameters)
        return_from_api = objectify.fromstring(return_from_api)
        return return_from_api.Resultado if hasattr(return_from_api, 'Resultado') else []
