# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.47.dev3
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from feersum_nlu.api_client import ApiClient


class Lr4LanguageRecognisersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def lr4_language_recogniser_retrieve(self, instance_name, text_input, **kwargs):  # noqa: E501
        """Recognise the language the text is written in.  # noqa: E501

        Recognise the language the text is written in. Returns the list of scored language codes (ISO 639-3).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lr4_language_recogniser_retrieve(instance_name, text_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param TextInput text_input: The input text. (required)
        :param str x_caller:
        :return: list[ScoredLabel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lr4_language_recogniser_retrieve_with_http_info(instance_name, text_input, **kwargs)  # noqa: E501
        else:
            (data) = self.lr4_language_recogniser_retrieve_with_http_info(instance_name, text_input, **kwargs)  # noqa: E501
            return data

    def lr4_language_recogniser_retrieve_with_http_info(self, instance_name, text_input, **kwargs):  # noqa: E501
        """Recognise the language the text is written in.  # noqa: E501

        Recognise the language the text is written in. Returns the list of scored language codes (ISO 639-3).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lr4_language_recogniser_retrieve_with_http_info(instance_name, text_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param TextInput text_input: The input text. (required)
        :param str x_caller:
        :return: list[ScoredLabel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'text_input', 'x_caller']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lr4_language_recogniser_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `lr4_language_recogniser_retrieve`")  # noqa: E501
        # verify the required parameter 'text_input' is set
        if ('text_input' not in params or
                params['text_input'] is None):
            raise ValueError("Missing the required parameter `text_input` when calling `lr4_language_recogniser_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_caller' in params:
            header_params['X-CALLER'] = params['x_caller']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'text_input' in params:
            body_params = params['text_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/nlu/v2/lr4_language_recognisers/{instance_name}/retrieve', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ScoredLabel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
