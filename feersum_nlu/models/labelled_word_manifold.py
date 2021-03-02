# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.54.dev1
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LabelledWordManifold(object):
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
        'label': 'str',
        'word_manifold': 'str'
    }

    attribute_map = {
        'label': 'label',
        'word_manifold': 'word_manifold'
    }

    def __init__(self, label=None, word_manifold=None):  # noqa: E501
        """LabelledWordManifold - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._word_manifold = None
        self.discriminator = None

        self.label = label
        self.word_manifold = word_manifold

    @property
    def label(self):
        """Gets the label of this LabelledWordManifold.  # noqa: E501

        The language code label. Please use ISO 639-3 language codes.  # noqa: E501

        :return: The label of this LabelledWordManifold.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LabelledWordManifold.

        The language code label. Please use ISO 639-3 language codes.  # noqa: E501

        :param label: The label of this LabelledWordManifold.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def word_manifold(self):
        """Gets the word_manifold of this LabelledWordManifold.  # noqa: E501

        The name of the word manifold to use for the language code.  # noqa: E501

        :return: The word_manifold of this LabelledWordManifold.  # noqa: E501
        :rtype: str
        """
        return self._word_manifold

    @word_manifold.setter
    def word_manifold(self, word_manifold):
        """Sets the word_manifold of this LabelledWordManifold.

        The name of the word manifold to use for the language code.  # noqa: E501

        :param word_manifold: The word_manifold of this LabelledWordManifold.  # noqa: E501
        :type: str
        """
        if word_manifold is None:
            raise ValueError("Invalid value for `word_manifold`, must not be `None`")  # noqa: E501

        self._word_manifold = word_manifold

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
        if issubclass(LabelledWordManifold, dict):
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
        if not isinstance(other, LabelledWordManifold):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
