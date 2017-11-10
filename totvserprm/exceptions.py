# -*- coding: utf-8 -*-
class ApiError(Exception):
    """ Exception of validations in api """
    def __init__(self, message):
        super(ApiError, self).__init__(message)
