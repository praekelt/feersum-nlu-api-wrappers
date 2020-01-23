# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.44
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DucklingEntity(object):
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
        'body': 'str',
        'dim': 'str',
        'type': 'str',
        'value': 'str',
        'grain': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'body': 'body',
        'dim': 'dim',
        'type': 'type',
        'value': 'value',
        'grain': 'grain',
        'unit': 'unit'
    }

    def __init__(self, body=None, dim=None, type=None, value=None, grain=None, unit=None):  # noqa: E501
        """DucklingEntity - a model defined in Swagger"""  # noqa: E501

        self._body = None
        self._dim = None
        self._type = None
        self._value = None
        self._grain = None
        self._unit = None
        self.discriminator = None

        self.body = body
        self.dim = dim
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if grain is not None:
            self.grain = grain
        if unit is not None:
            self.unit = unit

    @property
    def body(self):
        """Gets the body of this DucklingEntity.  # noqa: E501

        The input text associated with the entity.  # noqa: E501

        :return: The body of this DucklingEntity.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DucklingEntity.

        The input text associated with the entity.  # noqa: E501

        :param body: The body of this DucklingEntity.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def dim(self):
        """Gets the dim of this DucklingEntity.  # noqa: E501

        The dimension (time, duration, distance, etc.) of the entity.  # noqa: E501

        :return: The dim of this DucklingEntity.  # noqa: E501
        :rtype: str
        """
        return self._dim

    @dim.setter
    def dim(self, dim):
        """Sets the dim of this DucklingEntity.

        The dimension (time, duration, distance, etc.) of the entity.  # noqa: E501

        :param dim: The dim of this DucklingEntity.  # noqa: E501
        :type: str
        """
        if dim is None:
            raise ValueError("Invalid value for `dim`, must not be `None`")  # noqa: E501

        self._dim = dim

    @property
    def type(self):
        """Gets the type of this DucklingEntity.  # noqa: E501

        The type (value, interval, etc.) of this entity.  # noqa: E501

        :return: The type of this DucklingEntity.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DucklingEntity.

        The type (value, interval, etc.) of this entity.  # noqa: E501

        :param type: The type of this DucklingEntity.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this DucklingEntity.  # noqa: E501

        Structured result value.  # noqa: E501

        :return: The value of this DucklingEntity.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DucklingEntity.

        Structured result value.  # noqa: E501

        :param value: The value of this DucklingEntity.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def grain(self):
        """Gets the grain of this DucklingEntity.  # noqa: E501

        The granularity/specificity of a time value.  # noqa: E501

        :return: The grain of this DucklingEntity.  # noqa: E501
        :rtype: str
        """
        return self._grain

    @grain.setter
    def grain(self, grain):
        """Sets the grain of this DucklingEntity.

        The granularity/specificity of a time value.  # noqa: E501

        :param grain: The grain of this DucklingEntity.  # noqa: E501
        :type: str
        """

        self._grain = grain

    @property
    def unit(self):
        """Gets the unit of this DucklingEntity.  # noqa: E501

        The units of the value property.  # noqa: E501

        :return: The unit of this DucklingEntity.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this DucklingEntity.

        The units of the value property.  # noqa: E501

        :param unit: The unit of this DucklingEntity.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if issubclass(DucklingEntity, dict):
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
        if not isinstance(other, DucklingEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
