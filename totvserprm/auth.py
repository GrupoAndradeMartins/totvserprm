# -*- coding: utf-8 -*-
from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

def create_service(server, username, password):
    session = Session()
    session.auth = HTTPBasicAuth(username,password)
    client = Client(wsdl='http://{}/wsDataServer/MEX?wsdl'.format(server), transport=Transport(session=session))
    return client.create_service('{http://www.totvs.com/}RM_IwsDataServer', 'http://{}/wsDataServer/IwsDataServer'.format(server))

def create_service_sql(server, username, password):
    session = Session()
    session.auth = HTTPBasicAuth(username,password)
    client = Client(wsdl='http://{}/wsConsultaSQL/MEX?wsdl'.format(server), transport=Transport(session=session))
    return client.create_service('{http://www.totvs.com/}RM_IwsConsultaSQL', 'http://{}/wsConsultaSQL/IwsConsultaSQL'.format(server))
