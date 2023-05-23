# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.55
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DateEntity(object):
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
        'value': 'str',
        'granularity': 'str'
    }

    attribute_map = {
        'value': 'value',
        'granularity': 'granularity'
    }

    def __init__(self, value=None, granularity=None):  # noqa: E501
        """DateEntity - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._granularity = None
        self.discriminator = None

        self.value = value
        self.granularity = granularity

    @property
    def value(self):
        """Gets the value of this DateEntity.  # noqa: E501


        :return: The value of this DateEntity.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DateEntity.


        :param value: The value of this DateEntity.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def granularity(self):
        """Gets the granularity of this DateEntity.  # noqa: E501


        :return: The granularity of this DateEntity.  # noqa: E501
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this DateEntity.


        :param granularity: The granularity of this DateEntity.  # noqa: E501
        :type: str
        """
        if granularity is None:
            raise ValueError("Invalid value for `granularity`, must not be `None`")  # noqa: E501
        allowed_values = ["second", "minute", "hour", "day", "week", "month", "year"]  # noqa: E501
        if granularity not in allowed_values:
            raise ValueError(
                "Invalid value for `granularity` ({0}), must be one of {1}"  # noqa: E501
                .format(granularity, allowed_values)
            )

        self._granularity = granularity

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
        if issubclass(DateEntity, dict):
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
        if not isinstance(other, DateEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
