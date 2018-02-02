#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Tim Yao'


'''
JSON API definition.
'''

import json, logging, inspect, functools


'''
the base APIError which contains error(required), data(optional) and message(optional).
'''


class APIError(Exception):
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


'''
Indicate the input value has error or invalid. The data specifies the error field of input form.
'''


class APIValueError(APIError):

    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)


class APIResourceNotFoundError(APIError):
    # Indicate the resource was not found. The data specifies the resource name.
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)


class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)