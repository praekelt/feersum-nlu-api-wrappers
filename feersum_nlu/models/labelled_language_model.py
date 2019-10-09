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


class LabelledLanguageModel(object):
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
        'lang_code': 'str',
        'lang_model': 'str'
    }

    attribute_map = {
        'lang_code': 'lang_code',
        'lang_model': 'lang_model'
    }

    def __init__(self, lang_code=None, lang_model=None):  # noqa: E501
        """LabelledLanguageModel - a model defined in Swagger"""  # noqa: E501

        self._lang_code = None
        self._lang_model = None
        self.discriminator = None

        self.lang_code = lang_code
        self.lang_model = lang_model

    @property
    def lang_code(self):
        """Gets the lang_code of this LabelledLanguageModel.  # noqa: E501

        The language code label. Please use ISO 639-3 language codes.  # noqa: E501

        :return: The lang_code of this LabelledLanguageModel.  # noqa: E501
        :rtype: str
        """
        return self._lang_code

    @lang_code.setter
    def lang_code(self, lang_code):
        """Sets the lang_code of this LabelledLanguageModel.

        The language code label. Please use ISO 639-3 language codes.  # noqa: E501

        :param lang_code: The lang_code of this LabelledLanguageModel.  # noqa: E501
        :type: str
        """
        if lang_code is None:
            raise ValueError("Invalid value for `lang_code`, must not be `None`")  # noqa: E501

        self._lang_code = lang_code

    @property
    def lang_model(self):
        """Gets the lang_model of this LabelledLanguageModel.  # noqa: E501

        The name of the language model to use for the language code in the associated model.  # noqa: E501

        :return: The lang_model of this LabelledLanguageModel.  # noqa: E501
        :rtype: str
        """
        return self._lang_model

    @lang_model.setter
    def lang_model(self, lang_model):
        """Sets the lang_model of this LabelledLanguageModel.

        The name of the language model to use for the language code in the associated model.  # noqa: E501

        :param lang_model: The lang_model of this LabelledLanguageModel.  # noqa: E501
        :type: str
        """
        if lang_model is None:
            raise ValueError("Invalid value for `lang_model`, must not be `None`")  # noqa: E501

        self._lang_model = lang_model

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
        if issubclass(LabelledLanguageModel, dict):
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
        if not isinstance(other, LabelledLanguageModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
