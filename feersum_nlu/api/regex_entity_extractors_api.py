# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.10
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

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from feersum_nlu.api_client import ApiClient


class RegexEntityExtractorsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def regex_entity_extractor_create(self, regex_ent_create_details, **kwargs):  # noqa: E501
        """Create a regular expression entity extractor.  # noqa: E501

        Create a new regular expression entity extractor or load one from the store.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.regex_entity_extractor_create(regex_ent_create_details, async=True)
        >>> result = thread.get()

        :param async bool
        :param RegexEntCreateDetails regex_ent_create_details: The details of the instance to create. (required)
        :return: RegexInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.regex_entity_extractor_create_with_http_info(regex_ent_create_details, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_create_with_http_info(regex_ent_create_details, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_create_with_http_info(self, regex_ent_create_details, **kwargs):  # noqa: E501
        """Create a regular expression entity extractor.  # noqa: E501

        Create a new regular expression entity extractor or load one from the store.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.regex_entity_extractor_create_with_http_info(regex_ent_create_details, async=True)
        >>> result = thread.get()

        :param async bool
        :param RegexEntCreateDetails regex_ent_create_details: The details of the instance to create. (required)
        :return: RegexInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['regex_ent_create_details']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'regex_ent_create_details' is set
        if ('regex_ent_create_details' not in params or
                params['regex_ent_create_details'] is None):
            raise ValueError("Missing the required parameter `regex_ent_create_details` when calling `regex_entity_extractor_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'regex_ent_create_details' in params:
            body_params = params['regex_ent_create_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/regex_entity_extractors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegexInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_get_details(self, instance_name, **kwargs):  # noqa: E501
        """Get details of named instance.  # noqa: E501

        Get the details of the named regular expression entity extractor instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.regex_entity_extractor_get_details(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :return: RegexInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.regex_entity_extractor_get_details_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_get_details_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_get_details_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Get details of named instance.  # noqa: E501

        Get the details of the named regular expression entity extractor instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.regex_entity_extractor_get_details_with_http_info(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :return: RegexInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_get_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `regex_entity_extractor_get_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/regex_entity_extractors/{instance_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegexInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_get_details_all(self, **kwargs):  # noqa: E501
        """Get list of loaded regular expression entity extractors.  # noqa: E501

        Get the list of loaded regular expression entity extractors.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.regex_entity_extractor_get_details_all(async=True)
        >>> result = thread.get()

        :param async bool
        :return: RegexInstanceDetailList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.regex_entity_extractor_get_details_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_get_details_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_get_details_all_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of loaded regular expression entity extractors.  # noqa: E501

        Get the list of loaded regular expression entity extractors.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.regex_entity_extractor_get_details_all_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: RegexInstanceDetailList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_get_details_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            '/regex_entity_extractors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegexInstanceDetailList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_retrieve(self, instance_name, text_input, **kwargs):  # noqa: E501
        """Extract information based on the regular expression.  # noqa: E501

        Extract the entities matching the regular expression.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.regex_entity_extractor_retrieve(instance_name, text_input, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param TextInput text_input: The input text. (required)
        :return: EntityList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_retrieve_with_http_info(self, instance_name, text_input, **kwargs):  # noqa: E501
        """Extract information based on the regular expression.  # noqa: E501

        Extract the entities matching the regular expression.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param TextInput text_input: The input text. (required)
        :return: EntityList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'text_input']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `regex_entity_extractor_retrieve`")  # noqa: E501
        # verify the required parameter 'text_input' is set
        if ('text_input' not in params or
                params['text_input'] is None):
            raise ValueError("Missing the required parameter `text_input` when calling `regex_entity_extractor_retrieve`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'instance_name' in params:
            path_params['instance_name'] = params['instance_name']  # noqa: E501

        query_params = []

        header_params = {}

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
            '/regex_entity_extractors/{instance_name}/retrieve', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EntityList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
