# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.

    OpenAPI spec version: 2.0.2
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class RegexEntityExtractorsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def regex_entity_extractor_create(self, regex_ent_create_details, **kwargs):
        """
        Create a regular expression entity extractor.
        Create a new regular expression entity extractor or load one from the store.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.regex_entity_extractor_create(regex_ent_create_details, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RegexEntCreateDetails regex_ent_create_details: The details of the instance to create. (required)
        :return: RegexInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.regex_entity_extractor_create_with_http_info(regex_ent_create_details, **kwargs)
        else:
            (data) = self.regex_entity_extractor_create_with_http_info(regex_ent_create_details, **kwargs)
            return data

    def regex_entity_extractor_create_with_http_info(self, regex_ent_create_details, **kwargs):
        """
        Create a regular expression entity extractor.
        Create a new regular expression entity extractor or load one from the store.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.regex_entity_extractor_create_with_http_info(regex_ent_create_details, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param RegexEntCreateDetails regex_ent_create_details: The details of the instance to create. (required)
        :return: RegexInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['regex_ent_create_details']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'regex_ent_create_details' is set
        if ('regex_ent_create_details' not in params) or (params['regex_ent_create_details'] is None):
            raise ValueError("Missing the required parameter `regex_ent_create_details` when calling `regex_entity_extractor_create`")


        collection_formats = {}

        resource_path = '/regex_entity_extractors'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'regex_ent_create_details' in params:
            body_params = params['regex_ent_create_details']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RegexInstanceDetail',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def regex_entity_extractor_get_details(self, instance_name, **kwargs):
        """
        Get details of named instance.
        Get the details of the named regular expression entity extractor instance.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.regex_entity_extractor_get_details(instance_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instance_name: The name of the model instance. (required)
        :return: RegexInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.regex_entity_extractor_get_details_with_http_info(instance_name, **kwargs)
        else:
            (data) = self.regex_entity_extractor_get_details_with_http_info(instance_name, **kwargs)
            return data

    def regex_entity_extractor_get_details_with_http_info(self, instance_name, **kwargs):
        """
        Get details of named instance.
        Get the details of the named regular expression entity extractor instance.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.regex_entity_extractor_get_details_with_http_info(instance_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instance_name: The name of the model instance. (required)
        :return: RegexInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_get_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params) or (params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `regex_entity_extractor_get_details`")


        collection_formats = {}

        resource_path = '/regex_entity_extractors/{instance_name}'.replace('{format}', 'json')
        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RegexInstanceDetail',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def regex_entity_extractor_get_details_all(self, **kwargs):
        """
        Get list of loaded regular expression entity extractors.
        Get the list of loaded regular expression entity extractors.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.regex_entity_extractor_get_details_all(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: RegexInstanceDetailList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.regex_entity_extractor_get_details_all_with_http_info(**kwargs)
        else:
            (data) = self.regex_entity_extractor_get_details_all_with_http_info(**kwargs)
            return data

    def regex_entity_extractor_get_details_all_with_http_info(self, **kwargs):
        """
        Get list of loaded regular expression entity extractors.
        Get the list of loaded regular expression entity extractors.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.regex_entity_extractor_get_details_all_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: RegexInstanceDetailList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_get_details_all" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/regex_entity_extractors'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='RegexInstanceDetailList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def regex_entity_extractor_retrieve(self, instance_name, text_input, **kwargs):
        """
        Extract information based on the regular expression.
        Extract the entities matching the regular expression.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.regex_entity_extractor_retrieve(instance_name, text_input, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instance_name: The name of the model instance. (required)
        :param TextInput text_input: The input text. (required)
        :return: EntityList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, **kwargs)
        else:
            (data) = self.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, **kwargs)
            return data

    def regex_entity_extractor_retrieve_with_http_info(self, instance_name, text_input, **kwargs):
        """
        Extract information based on the regular expression.
        Extract the entities matching the regular expression.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instance_name: The name of the model instance. (required)
        :param TextInput text_input: The input text. (required)
        :return: EntityList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'text_input']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params) or (params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `regex_entity_extractor_retrieve`")
        # verify the required parameter 'text_input' is set
        if ('text_input' not in params) or (params['text_input'] is None):
            raise ValueError("Missing the required parameter `text_input` when calling `regex_entity_extractor_retrieve`")


        collection_formats = {}

        resource_path = '/regex_entity_extractors/{instance_name}/retrieve'.replace('{format}', 'json')
        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'text_input' in params:
            body_params = params['text_input']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='EntityList',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
