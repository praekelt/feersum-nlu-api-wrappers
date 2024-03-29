# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.55
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
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

    def regex_entity_extractor_create(self, create_details, **kwargs):  # noqa: E501
        """Create a regular expression entity extractor.  # noqa: E501

        Create a new regular expression entity extractor or reload one from the trash.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_create(create_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegexEntityExtractorCreateDetails create_details: The details of the instance to create. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regex_entity_extractor_create_with_http_info(create_details, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_create_with_http_info(create_details, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_create_with_http_info(self, create_details, **kwargs):  # noqa: E501
        """Create a regular expression entity extractor.  # noqa: E501

        Create a new regular expression entity extractor or reload one from the trash.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_create_with_http_info(create_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegexEntityExtractorCreateDetails create_details: The details of the instance to create. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_details', 'x_caller']  # noqa: E501
        all_params.append('async_req')
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
        # verify the required parameter 'create_details' is set
        if ('create_details' not in params or
                params['create_details'] is None):
            raise ValueError("Missing the required parameter `create_details` when calling `regex_entity_extractor_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_caller' in params:
            header_params['X-CALLER'] = params['x_caller']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_details' in params:
            body_params = params['create_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/nlu/v2/regex_entity_extractors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegexEntityExtractorInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_del(self, instance_name, **kwargs):  # noqa: E501
        """Delete named instance.  # noqa: E501

        Delete and get the details of the named regular expression entity extractor instance. Deleted models can be reloaded from the trash with the create operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_del(instance_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regex_entity_extractor_del_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_del_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_del_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Delete named instance.  # noqa: E501

        Delete and get the details of the named regular expression entity extractor instance. Deleted models can be reloaded from the trash with the create operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_del_with_http_info(instance_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'x_caller']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_del" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `regex_entity_extractor_del`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/nlu/v2/regex_entity_extractors/{instance_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegexEntityExtractorInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_get_details(self, instance_name, **kwargs):  # noqa: E501
        """Get details of named instance.  # noqa: E501

        Get the details of the named regular expression entity extractor instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_get_details(instance_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regex_entity_extractor_get_details_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_get_details_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_get_details_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Get details of named instance.  # noqa: E501

        Get the details of the named regular expression entity extractor instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_get_details_with_http_info(instance_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'x_caller']  # noqa: E501
        all_params.append('async_req')
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
            '/nlu/v2/regex_entity_extractors/{instance_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegexEntityExtractorInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_get_details_all(self, **kwargs):  # noqa: E501
        """Get list of regular expression entity extractors.  # noqa: E501

        Get the list of regular expression entity extractors.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_get_details_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_caller:
        :return: list[RegexEntityExtractorInstanceDetail]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regex_entity_extractor_get_details_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_get_details_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_get_details_all_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of regular expression entity extractors.  # noqa: E501

        Get the list of regular expression entity extractors.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_get_details_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_caller:
        :return: list[RegexEntityExtractorInstanceDetail]
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
                    " to method regex_entity_extractor_get_details_all" % key
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
            '/nlu/v2/regex_entity_extractors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RegexEntityExtractorInstanceDetail]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_get_params(self, instance_name, **kwargs):  # noqa: E501
        """Get the editable model parameters of named regex entity extractor.  # noqa: E501

        Get the editable model parameters of named regex entity extractor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_get_params(instance_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param str x_caller:
        :return: ModelParams
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regex_entity_extractor_get_params_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_get_params_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_get_params_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Get the editable model parameters of named regex entity extractor.  # noqa: E501

        Get the editable model parameters of named regex entity extractor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_get_params_with_http_info(instance_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param str x_caller:
        :return: ModelParams
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'x_caller']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_get_params" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `regex_entity_extractor_get_params`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/nlu/v2/regex_entity_extractors/{instance_name}/params', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelParams',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_retrieve(self, instance_name, text_input, **kwargs):  # noqa: E501
        """Extract information based on the regular expression.  # noqa: E501

        Extract the entities matching the regular expression.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_retrieve(instance_name, text_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param TextInput text_input: The input text. (required)
        :param str x_caller:
        :return: list[RegexEntity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_retrieve_with_http_info(self, instance_name, text_input, **kwargs):  # noqa: E501
        """Extract information based on the regular expression.  # noqa: E501

        Extract the entities matching the regular expression.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_retrieve_with_http_info(instance_name, text_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param TextInput text_input: The input text. (required)
        :param str x_caller:
        :return: list[RegexEntity]
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
            '/nlu/v2/regex_entity_extractors/{instance_name}/retrieve', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RegexEntity]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_set_params(self, instance_name, model_params, **kwargs):  # noqa: E501
        """Set the model parameters of named regex entity extractor.  # noqa: E501

        Set the model parameters of named regex entity extractor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_set_params(instance_name, model_params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param ModelParams model_params: The model parameters. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regex_entity_extractor_set_params_with_http_info(instance_name, model_params, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_set_params_with_http_info(instance_name, model_params, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_set_params_with_http_info(self, instance_name, model_params, **kwargs):  # noqa: E501
        """Set the model parameters of named regex entity extractor.  # noqa: E501

        Set the model parameters of named regex entity extractor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_set_params_with_http_info(instance_name, model_params, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param ModelParams model_params: The model parameters. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'model_params', 'x_caller']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_set_params" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `regex_entity_extractor_set_params`")  # noqa: E501
        # verify the required parameter 'model_params' is set
        if ('model_params' not in params or
                params['model_params'] is None):
            raise ValueError("Missing the required parameter `model_params` when calling `regex_entity_extractor_set_params`")  # noqa: E501

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
        if 'model_params' in params:
            body_params = params['model_params']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/nlu/v2/regex_entity_extractors/{instance_name}/params', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegexEntityExtractorInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def regex_entity_extractor_vaporise(self, instance_name, **kwargs):  # noqa: E501
        """Vaporise the named model.  # noqa: E501

        Permanently vaporises a model even if not trashed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_vaporise(instance_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.regex_entity_extractor_vaporise_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.regex_entity_extractor_vaporise_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def regex_entity_extractor_vaporise_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Vaporise the named model.  # noqa: E501

        Permanently vaporises a model even if not trashed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.regex_entity_extractor_vaporise_with_http_info(instance_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str instance_name: The name of the instance. (required)
        :param str x_caller:
        :return: RegexEntityExtractorInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'x_caller']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method regex_entity_extractor_vaporise" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `regex_entity_extractor_vaporise`")  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/nlu/v2/regex_entity_extractors/{instance_name}/vaporise', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegexEntityExtractorInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
