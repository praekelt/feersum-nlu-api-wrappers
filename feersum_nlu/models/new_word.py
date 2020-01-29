# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.45
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class NewWord(object):
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
        'new_word': 'str',
        'similar_to': 'str'
    }

    attribute_map = {
        'new_word': 'new_word',
        'similar_to': 'similar_to'
    }

    def __init__(self, new_word=None, similar_to=None):  # noqa: E501
        """NewWord - a model defined in Swagger"""  # noqa: E501

        self._new_word = None
        self._similar_to = None
        self.discriminator = None

        self.new_word = new_word
        self.similar_to = similar_to

    @property
    def new_word(self):
        """Gets the new_word of this NewWord.  # noqa: E501


        :return: The new_word of this NewWord.  # noqa: E501
        :rtype: str
        """
        return self._new_word

    @new_word.setter
    def new_word(self, new_word):
        """Sets the new_word of this NewWord.


        :param new_word: The new_word of this NewWord.  # noqa: E501
        :type: str
        """
        if new_word is None:
            raise ValueError("Invalid value for `new_word`, must not be `None`")  # noqa: E501

        self._new_word = new_word

    @property
    def similar_to(self):
        """Gets the similar_to of this NewWord.  # noqa: E501


        :return: The similar_to of this NewWord.  # noqa: E501
        :rtype: str
        """
        return self._similar_to

    @similar_to.setter
    def similar_to(self, similar_to):
        """Sets the similar_to of this NewWord.


        :param similar_to: The similar_to of this NewWord.  # noqa: E501
        :type: str
        """
        if similar_to is None:
            raise ValueError("Invalid value for `similar_to`, must not be `None`")  # noqa: E501

        self._similar_to = similar_to

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
        if issubclass(NewWord, dict):
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
        if not isinstance(other, NewWord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
