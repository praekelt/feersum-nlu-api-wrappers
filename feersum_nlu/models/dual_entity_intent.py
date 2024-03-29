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


class DualEntityIntent(object):
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
        'entity': 'str',
        'value': 'str',
        'index': 'int',
        'len': 'int',
        'intent': 'str'
    }

    attribute_map = {
        'entity': 'entity',
        'value': 'value',
        'index': 'index',
        'len': 'len',
        'intent': 'intent'
    }

    def __init__(self, entity=None, value=None, index=None, len=None, intent=None):  # noqa: E501
        """DualEntityIntent - a model defined in Swagger"""  # noqa: E501

        self._entity = None
        self._value = None
        self._index = None
        self._len = None
        self._intent = None
        self.discriminator = None

        self.entity = entity
        self.value = value
        self.index = index
        self.len = len
        self.intent = intent

    @property
    def entity(self):
        """Gets the entity of this DualEntityIntent.  # noqa: E501

        The entity label/class/type.  # noqa: E501

        :return: The entity of this DualEntityIntent.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this DualEntityIntent.

        The entity label/class/type.  # noqa: E501

        :param entity: The entity of this DualEntityIntent.  # noqa: E501
        :type: str
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501

        self._entity = entity

    @property
    def value(self):
        """Gets the value of this DualEntityIntent.  # noqa: E501

        The value of the entity extracted from the input text. Not used during training!  # noqa: E501

        :return: The value of this DualEntityIntent.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DualEntityIntent.

        The value of the entity extracted from the input text. Not used during training!  # noqa: E501

        :param value: The value of this DualEntityIntent.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def index(self):
        """Gets the index of this DualEntityIntent.  # noqa: E501

        The first character of the entity in the associated utterance.  # noqa: E501

        :return: The index of this DualEntityIntent.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DualEntityIntent.

        The first character of the entity in the associated utterance.  # noqa: E501

        :param index: The index of this DualEntityIntent.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def len(self):
        """Gets the len of this DualEntityIntent.  # noqa: E501

        The length of the extracted entity in the associated utterance.  # noqa: E501

        :return: The len of this DualEntityIntent.  # noqa: E501
        :rtype: int
        """
        return self._len

    @len.setter
    def len(self, len):
        """Sets the len of this DualEntityIntent.

        The length of the extracted entity in the associated utterance.  # noqa: E501

        :param len: The len of this DualEntityIntent.  # noqa: E501
        :type: int
        """
        if len is None:
            raise ValueError("Invalid value for `len`, must not be `None`")  # noqa: E501

        self._len = len

    @property
    def intent(self):
        """Gets the intent of this DualEntityIntent.  # noqa: E501

        The intent label/class/type.  # noqa: E501

        :return: The intent of this DualEntityIntent.  # noqa: E501
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this DualEntityIntent.

        The intent label/class/type.  # noqa: E501

        :param intent: The intent of this DualEntityIntent.  # noqa: E501
        :type: str
        """
        if intent is None:
            raise ValueError("Invalid value for `intent`, must not be `None`")  # noqa: E501

        self._intent = intent

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
        if issubclass(DualEntityIntent, dict):
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
        if not isinstance(other, DualEntityIntent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
