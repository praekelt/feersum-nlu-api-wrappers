# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.45
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from feersum_nlu.api_client import ApiClient


class HealthApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def health_get_status(self, **kwargs):  # noqa: E501
        """An endpoint to check if the service is alice and well.  # noqa: E501

        Check if the service is alice and well.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.health_get_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_caller:
        :param str origin:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.health_get_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.health_get_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def health_get_status_with_http_info(self, **kwargs):  # noqa: E501
        """An endpoint to check if the service is alice and well.  # noqa: E501

        Check if the service is alice and well.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.health_get_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_caller:
        :param str origin:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_caller', 'origin']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method health_get_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_caller' in params:
            header_params['X-CALLER'] = params['x_caller']  # noqa: E501
        if 'origin' in params:
            header_params['Origin'] = params['origin']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/health', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
