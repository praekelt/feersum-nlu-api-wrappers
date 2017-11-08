# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.

    OpenAPI spec version: 2.0.3
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


class SentimentDetectorsApi(object):
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

    def sentiment_detector_retrieve(self, instance_name, text_input, **kwargs):
        """
        Detect sentiment.
        Detect the general sentiment in the input text.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sentiment_detector_retrieve(instance_name, text_input, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instance_name: The name of the model instance. (required)
        :param TextInput text_input: The input text. (required)
        :return: Sentiment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sentiment_detector_retrieve_with_http_info(instance_name, text_input, **kwargs)
        else:
            (data) = self.sentiment_detector_retrieve_with_http_info(instance_name, text_input, **kwargs)
            return data

    def sentiment_detector_retrieve_with_http_info(self, instance_name, text_input, **kwargs):
        """
        Detect sentiment.
        Detect the general sentiment in the input text.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sentiment_detector_retrieve_with_http_info(instance_name, text_input, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instance_name: The name of the model instance. (required)
        :param TextInput text_input: The input text. (required)
        :return: Sentiment
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
                    " to method sentiment_detector_retrieve" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instance_name' is set
        if ('instance_name' not in params) or (params['instance_name'] is None):
            raise ValueError("Missing the required parameter `instance_name` when calling `sentiment_detector_retrieve`")
        # verify the required parameter 'text_input' is set
        if ('text_input' not in params) or (params['text_input'] is None):
            raise ValueError("Missing the required parameter `text_input` when calling `sentiment_detector_retrieve`")


        collection_formats = {}

        resource_path = '/sentiment_detectors/{instance_name}/retrieve'.replace('{format}', 'json')
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
                                            response_type='Sentiment',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
