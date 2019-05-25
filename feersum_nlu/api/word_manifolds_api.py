# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.30.dev4
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from feersum_nlu.api_client import ApiClient


class WordManifoldsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def word_manifold_add_similar_words(self, instance_name, new_word_list, **kwargs):  # noqa: E501
        """Add new words.  # noqa: E501

        Add new words to the manifold that are similar to existing words and save the manifold. Warning! - Because this operation saves the updated word manifold to the store it could take a few seconds to complete. Returns the details of the updated instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_add_similar_words(instance_name, new_word_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param list[NewWord] new_word_list: List of new words. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_add_similar_words_with_http_info(instance_name, new_word_list, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_add_similar_words_with_http_info(instance_name, new_word_list, **kwargs)  # noqa: E501
            return data

    def word_manifold_add_similar_words_with_http_info(self, instance_name, new_word_list, **kwargs):  # noqa: E501
        """Add new words.  # noqa: E501

        Add new words to the manifold that are similar to existing words and save the manifold. Warning! - Because this operation saves the updated word manifold to the store it could take a few seconds to complete. Returns the details of the updated instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_add_similar_words_with_http_info(instance_name, new_word_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param list[NewWord] new_word_list: List of new words. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'new_word_list', 'x_caller']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_add_similar_words" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `word_manifold_add_similar_words`")  # noqa: E501
        # verify the required parameter 'new_word_list' is set
        if ('new_word_list' not in params or
                params['new_word_list'] is None):
            raise ValueError("Missing the required parameter `new_word_list` when calling `word_manifold_add_similar_words`")  # noqa: E501

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
        if 'new_word_list' in params:
            body_params = params['new_word_list']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyHeader_old']  # noqa: E501

        return self.api_client.call_api(
            '/word_manifolds/{instance_name}/vocab', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WordManifoldInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def word_manifold_create(self, create_details, **kwargs):  # noqa: E501
        """Create a word manifold model.  # noqa: E501

        Create a new word manifold model using an input file or reload one from the trash. Warning! - These models are quite big and each takes a few seconds to load/create. Returns the details of the new or loaded instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_create(create_details, async=True)
        >>> result = thread.get()

        :param async bool
        :param WordManifoldCreateDetails create_details: The details of the word manifold instance to create. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_create_with_http_info(create_details, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_create_with_http_info(create_details, **kwargs)  # noqa: E501
            return data

    def word_manifold_create_with_http_info(self, create_details, **kwargs):  # noqa: E501
        """Create a word manifold model.  # noqa: E501

        Create a new word manifold model using an input file or reload one from the trash. Warning! - These models are quite big and each takes a few seconds to load/create. Returns the details of the new or loaded instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_create_with_http_info(create_details, async=True)
        >>> result = thread.get()

        :param async bool
        :param WordManifoldCreateDetails create_details: The details of the word manifold instance to create. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_details', 'x_caller']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_details' is set
        if ('create_details' not in params or
                params['create_details'] is None):
            raise ValueError("Missing the required parameter `create_details` when calling `word_manifold_create`")  # noqa: E501

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
            '/word_manifolds', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WordManifoldInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def word_manifold_del(self, instance_name, **kwargs):  # noqa: E501
        """Delete named instance.  # noqa: E501

        Delete and return the details of the word manifold instance. Deleted models can be reloaded from the trash with the create operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_del(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_del_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_del_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def word_manifold_del_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Delete named instance.  # noqa: E501

        Delete and return the details of the word manifold instance. Deleted models can be reloaded from the trash with the create operation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_del_with_http_info(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'x_caller']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_del" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `word_manifold_del`")  # noqa: E501

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
            '/word_manifolds/{instance_name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WordManifoldInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def word_manifold_get_details(self, instance_name, **kwargs):  # noqa: E501
        """Get details of named instance.  # noqa: E501

        Get the details of the named word manifold instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_get_details(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_get_details_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_get_details_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def word_manifold_get_details_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Get details of named instance.  # noqa: E501

        Get the details of the named word manifold instance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_get_details_with_http_info(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'x_caller']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_get_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `word_manifold_get_details`")  # noqa: E501

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
            '/word_manifolds/{instance_name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WordManifoldInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def word_manifold_vaporise(self, instance_name, **kwargs):  # noqa: E501
        """Vaporise the named model.  # noqa: E501

        Permanently vaporises a model even if not trashed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_vaporise(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.word_manifold_vaporise_with_http_info(instance_name, **kwargs)  # noqa: E501
        else:
            (data) = self.word_manifold_vaporise_with_http_info(instance_name, **kwargs)  # noqa: E501
            return data

    def word_manifold_vaporise_with_http_info(self, instance_name, **kwargs):  # noqa: E501
        """Vaporise the named model.  # noqa: E501

        Permanently vaporises a model even if not trashed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.word_manifold_vaporise_with_http_info(instance_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str instance_name: The name of the model instance. (required)
        :param str x_caller:
        :return: WordManifoldInstanceDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instance_name', 'x_caller']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method word_manifold_vaporise" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params or
                params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `word_manifold_vaporise`")  # noqa: E501

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
            '/word_manifolds/{instance_name}/vaporise', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WordManifoldInstanceDetail',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
