# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.45.post5
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from feersum_nlu.api_client import ApiClient


class DashboardApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def dashboard_get_details(self, **kwargs):  # noqa: E501
        """Your service dashboard. Same as POST endpoint, but doesn't allow params to be supplied to the operation.  # noqa: E501

        Get your list of loaded model instances, the API version, etc. Same as POST endpoint, but doesn't allow params to be supplied to the operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dashboard_get_details(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_caller:
        :return: DashboardDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dashboard_get_details_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.dashboard_get_details_with_http_info(**kwargs)  # noqa: E501
            return data

    def dashboard_get_details_with_http_info(self, **kwargs):  # noqa: E501
        """Your service dashboard. Same as POST endpoint, but doesn't allow params to be supplied to the operation.  # noqa: E501

        Get your list of loaded model instances, the API version, etc. Same as POST endpoint, but doesn't allow params to be supplied to the operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dashboard_get_details_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_caller:
        :return: DashboardDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_caller']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboard_get_details" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_caller' in params:
            header_params['X-CALLER'] = params['x_caller']  # noqa: E501

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
            '/dashboard', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DashboardDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def dashboard_get_details_with_params(self, params, **kwargs):  # noqa: E501
        """Your service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.  # noqa: E501

        Get your list of loaded model instances, the API version, etc. Same as GET endpoint, but allows params to be supplied to the operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dashboard_get_details_with_params(params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DashboardParams params: Params like 'show_data_objects' that influence the dashboard's response. (required)
        :param str x_caller:
        :return: DashboardDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.dashboard_get_details_with_params_with_http_info(params, **kwargs)  # noqa: E501
        else:
            (data) = self.dashboard_get_details_with_params_with_http_info(params, **kwargs)  # noqa: E501
            return data

    def dashboard_get_details_with_params_with_http_info(self, params, **kwargs):  # noqa: E501
        """Your service dashboard. Same as GET endpoint, but allows params to be supplied to the operation.  # noqa: E501

        Get your list of loaded model instances, the API version, etc. Same as GET endpoint, but allows params to be supplied to the operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.dashboard_get_details_with_params_with_http_info(params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DashboardParams params: Params like 'show_data_objects' that influence the dashboard's response. (required)
        :param str x_caller:
        :return: DashboardDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['params', 'x_caller']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method dashboard_get_details_with_params" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'params' is set
        if ('params' not in params or
                params['params'] is None):
            raise ValueError("Missing the required parameter `params` when calling `dashboard_get_details_with_params`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_caller' in params:
            header_params['X-CALLER'] = params['x_caller']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'params' in params:
            body_params = params['params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/dashboard', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DashboardDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
