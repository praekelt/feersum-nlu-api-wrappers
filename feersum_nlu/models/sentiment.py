# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.42
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from feersum_nlu.models.sentiment_detail import SentimentDetail  # noqa: F401,E501


class Sentiment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'value': 'float',
        'detail_list': 'list[SentimentDetail]'
    }

    attribute_map = {
        'value': 'value',
        'detail_list': 'detail_list'
    }

    def __init__(self, value=None, detail_list=None):  # noqa: E501
        """Sentiment - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._detail_list = None
        self.discriminator = None

        self.value = value
        if detail_list is not None:
            self.detail_list = detail_list

    @property
    def value(self):
        """Gets the value of this Sentiment.  # noqa: E501


        :return: The value of this Sentiment.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Sentiment.


        :param value: The value of this Sentiment.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def detail_list(self):
        """Gets the detail_list of this Sentiment.  # noqa: E501

        A list with detailed sentiments on parts of the text..  # noqa: E501

        :return: The detail_list of this Sentiment.  # noqa: E501
        :rtype: list[SentimentDetail]
        """
        return self._detail_list

    @detail_list.setter
    def detail_list(self, detail_list):
        """Sets the detail_list of this Sentiment.

        A list with detailed sentiments on parts of the text..  # noqa: E501

        :param detail_list: The detail_list of this Sentiment.  # noqa: E501
        :type: list[SentimentDetail]
        """

        self._detail_list = detail_list

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Sentiment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Sentiment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
