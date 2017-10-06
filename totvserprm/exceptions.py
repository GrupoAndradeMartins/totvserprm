# -*- coding: utf-8 -*-
class ValidationError(Exception):
    """ Exception of validations in api """
    def __init__(self, message):
        super(BoletoException, self).__init__(message)
