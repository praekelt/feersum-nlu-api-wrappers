# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.52
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ServiceParams(object):
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
        'cba': 'bool',
        'dba': 'bool'
    }

    attribute_map = {
        'cba': 'cba',
        'dba': 'dba'
    }

    def __init__(self, cba=None, dba=None):  # noqa: E501
        """ServiceParams - a model defined in Swagger"""  # noqa: E501

        self._cba = None
        self._dba = None
        self.discriminator = None

        if cba is not None:
            self.cba = cba
        if dba is not None:
            self.dba = dba

    @property
    def cba(self):
        """Gets the cba of this ServiceParams.  # noqa: E501


        :return: The cba of this ServiceParams.  # noqa: E501
        :rtype: bool
        """
        return self._cba

    @cba.setter
    def cba(self, cba):
        """Sets the cba of this ServiceParams.


        :param cba: The cba of this ServiceParams.  # noqa: E501
        :type: bool
        """

        self._cba = cba

    @property
    def dba(self):
        """Gets the dba of this ServiceParams.  # noqa: E501


        :return: The dba of this ServiceParams.  # noqa: E501
        :rtype: bool
        """
        return self._dba

    @dba.setter
    def dba(self, dba):
        """Sets the dba of this ServiceParams.


        :param dba: The dba of this ServiceParams.  # noqa: E501
        :type: bool
        """

        self._dba = dba

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
        if issubclass(ServiceParams, dict):
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
        if not isinstance(other, ServiceParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
