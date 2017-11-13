# -*- coding: utf-8 -*-
class ApiError(Exception):
    """ Exception of api """
    def __init__(self, message):
        super(ApiError, self).__init__(message)


class ApiObjectDoesNotExist(Exception):
    """ Exception does not exist in api """
    def __init__(self, message):
        super(ApiObjectDoesNotExist, self).__init__(message)
