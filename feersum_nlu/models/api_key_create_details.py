# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.34.post7
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiKeyCreateDetails(object):
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
        'desc': 'str',
        'call_count_limit': 'int'
    }

    attribute_map = {
        'desc': 'desc',
        'call_count_limit': 'call_count_limit'
    }

    def __init__(self, desc=None, call_count_limit=None):  # noqa: E501
        """ApiKeyCreateDetails - a model defined in Swagger"""  # noqa: E501

        self._desc = None
        self._call_count_limit = None
        self.discriminator = None

        self.desc = desc
        if call_count_limit is not None:
            self.call_count_limit = call_count_limit

    @property
    def desc(self):
        """Gets the desc of this ApiKeyCreateDetails.  # noqa: E501

        Details of the purpose or owner of this key.  # noqa: E501

        :return: The desc of this ApiKeyCreateDetails.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ApiKeyCreateDetails.

        Details of the purpose or owner of this key.  # noqa: E501

        :param desc: The desc of this ApiKeyCreateDetails.  # noqa: E501
        :type: str
        """
        if desc is None:
            raise ValueError("Invalid value for `desc`, must not be `None`")  # noqa: E501

        self._desc = desc

    @property
    def call_count_limit(self):
        """Gets the call_count_limit of this ApiKeyCreateDetails.  # noqa: E501

        The number of calls loaded on this key. Default call count limit is 'unlimited'. See the other endpoints for managing the call count limit.  # noqa: E501

        :return: The call_count_limit of this ApiKeyCreateDetails.  # noqa: E501
        :rtype: int
        """
        return self._call_count_limit

    @call_count_limit.setter
    def call_count_limit(self, call_count_limit):
        """Sets the call_count_limit of this ApiKeyCreateDetails.

        The number of calls loaded on this key. Default call count limit is 'unlimited'. See the other endpoints for managing the call count limit.  # noqa: E501

        :param call_count_limit: The call_count_limit of this ApiKeyCreateDetails.  # noqa: E501
        :type: int
        """

        self._call_count_limit = call_count_limit

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
        if issubclass(ApiKeyCreateDetails, dict):
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
        if not isinstance(other, ApiKeyCreateDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
