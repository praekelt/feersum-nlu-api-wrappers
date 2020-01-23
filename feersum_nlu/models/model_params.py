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


class ModelParams(object):
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
        'long_name': 'str',
        'desc': 'str',
        'readonly': 'bool',
        'threshold': 'float',
        'reference_time': 'str',
        'regex': 'str',
        'similar_words': 'list[str]',
        'word_manifold': 'str',
        'lid_model_file': 'str',
        'temperature': 'float'
    }

    attribute_map = {
        'long_name': 'long_name',
        'desc': 'desc',
        'readonly': 'readonly',
        'threshold': 'threshold',
        'reference_time': 'reference_time',
        'regex': 'regex',
        'similar_words': 'similar_words',
        'word_manifold': 'word_manifold',
        'lid_model_file': 'lid_model_file',
        'temperature': 'temperature'
    }

    def __init__(self, long_name=None, desc=None, readonly=None, threshold=None, reference_time=None, regex=None, similar_words=None, word_manifold=None, lid_model_file=None, temperature=None):  # noqa: E501
        """ModelParams - a model defined in Swagger"""  # noqa: E501

        self._long_name = None
        self._desc = None
        self._readonly = None
        self._threshold = None
        self._reference_time = None
        self._regex = None
        self._similar_words = None
        self._word_manifold = None
        self._lid_model_file = None
        self._temperature = None
        self.discriminator = None

        if long_name is not None:
            self.long_name = long_name
        if desc is not None:
            self.desc = desc
        if readonly is not None:
            self.readonly = readonly
        if threshold is not None:
            self.threshold = threshold
        if reference_time is not None:
            self.reference_time = reference_time
        if regex is not None:
            self.regex = regex
        if similar_words is not None:
            self.similar_words = similar_words
        if word_manifold is not None:
            self.word_manifold = word_manifold
        if lid_model_file is not None:
            self.lid_model_file = lid_model_file
        if temperature is not None:
            self.temperature = temperature

    @property
    def long_name(self):
        """Gets the long_name of this ModelParams.  # noqa: E501


        :return: The long_name of this ModelParams.  # noqa: E501
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """Sets the long_name of this ModelParams.


        :param long_name: The long_name of this ModelParams.  # noqa: E501
        :type: str
        """

        self._long_name = long_name

    @property
    def desc(self):
        """Gets the desc of this ModelParams.  # noqa: E501


        :return: The desc of this ModelParams.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this ModelParams.


        :param desc: The desc of this ModelParams.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def readonly(self):
        """Gets the readonly of this ModelParams.  # noqa: E501


        :return: The readonly of this ModelParams.  # noqa: E501
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this ModelParams.


        :param readonly: The readonly of this ModelParams.  # noqa: E501
        :type: bool
        """

        self._readonly = readonly

    @property
    def threshold(self):
        """Gets the threshold of this ModelParams.  # noqa: E501


        :return: The threshold of this ModelParams.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this ModelParams.


        :param threshold: The threshold of this ModelParams.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def reference_time(self):
        """Gets the reference_time of this ModelParams.  # noqa: E501


        :return: The reference_time of this ModelParams.  # noqa: E501
        :rtype: str
        """
        return self._reference_time

    @reference_time.setter
    def reference_time(self, reference_time):
        """Sets the reference_time of this ModelParams.


        :param reference_time: The reference_time of this ModelParams.  # noqa: E501
        :type: str
        """

        self._reference_time = reference_time

    @property
    def regex(self):
        """Gets the regex of this ModelParams.  # noqa: E501


        :return: The regex of this ModelParams.  # noqa: E501
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this ModelParams.


        :param regex: The regex of this ModelParams.  # noqa: E501
        :type: str
        """

        self._regex = regex

    @property
    def similar_words(self):
        """Gets the similar_words of this ModelParams.  # noqa: E501


        :return: The similar_words of this ModelParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._similar_words

    @similar_words.setter
    def similar_words(self, similar_words):
        """Sets the similar_words of this ModelParams.


        :param similar_words: The similar_words of this ModelParams.  # noqa: E501
        :type: list[str]
        """

        self._similar_words = similar_words

    @property
    def word_manifold(self):
        """Gets the word_manifold of this ModelParams.  # noqa: E501


        :return: The word_manifold of this ModelParams.  # noqa: E501
        :rtype: str
        """
        return self._word_manifold

    @word_manifold.setter
    def word_manifold(self, word_manifold):
        """Sets the word_manifold of this ModelParams.


        :param word_manifold: The word_manifold of this ModelParams.  # noqa: E501
        :type: str
        """

        self._word_manifold = word_manifold

    @property
    def lid_model_file(self):
        """Gets the lid_model_file of this ModelParams.  # noqa: E501


        :return: The lid_model_file of this ModelParams.  # noqa: E501
        :rtype: str
        """
        return self._lid_model_file

    @lid_model_file.setter
    def lid_model_file(self, lid_model_file):
        """Sets the lid_model_file of this ModelParams.


        :param lid_model_file: The lid_model_file of this ModelParams.  # noqa: E501
        :type: str
        """

        self._lid_model_file = lid_model_file

    @property
    def temperature(self):
        """Gets the temperature of this ModelParams.  # noqa: E501

        The softmax temperature. The lower the temperature the more pronounced the winning class' probability will be. The default is 1.0. A lower temperature is useful in a many class problem when the probabilty might otherwise be diluted amongst the classes.  # noqa: E501

        :return: The temperature of this ModelParams.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this ModelParams.

        The softmax temperature. The lower the temperature the more pronounced the winning class' probability will be. The default is 1.0. A lower temperature is useful in a many class problem when the probabilty might otherwise be diluted amongst the classes.  # noqa: E501

        :param temperature: The temperature of this ModelParams.  # noqa: E501
        :type: float
        """

        self._temperature = temperature

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
        if issubclass(ModelParams, dict):
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
        if not isinstance(other, ModelParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
