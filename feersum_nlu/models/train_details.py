# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.46
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from feersum_nlu.models.labelled_language_model import LabelledLanguageModel  # noqa: F401,E501
from feersum_nlu.models.labelled_word_manifold import LabelledWordManifold  # noqa: F401,E501


class TrainDetails(object):
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
        'threshold': 'float',
        'temperature': 'float',
        'immediate_mode': 'bool',
        'word_manifold': 'str',
        'word_manifold_list': 'list[LabelledWordManifold]',
        'clsfr_algorithm': 'str',
        'num_epochs': 'int',
        'language_model_list': 'list[LabelledLanguageModel]'
    }

    attribute_map = {
        'threshold': 'threshold',
        'temperature': 'temperature',
        'immediate_mode': 'immediate_mode',
        'word_manifold': 'word_manifold',
        'word_manifold_list': 'word_manifold_list',
        'clsfr_algorithm': 'clsfr_algorithm',
        'num_epochs': 'num_epochs',
        'language_model_list': 'language_model_list'
    }

    def __init__(self, threshold=None, temperature=None, immediate_mode=None, word_manifold=None, word_manifold_list=None, clsfr_algorithm=None, num_epochs=None, language_model_list=None):  # noqa: E501
        """TrainDetails - a model defined in Swagger"""  # noqa: E501

        self._threshold = None
        self._temperature = None
        self._immediate_mode = None
        self._word_manifold = None
        self._word_manifold_list = None
        self._clsfr_algorithm = None
        self._num_epochs = None
        self._language_model_list = None
        self.discriminator = None

        if threshold is not None:
            self.threshold = threshold
        if temperature is not None:
            self.temperature = temperature
        if immediate_mode is not None:
            self.immediate_mode = immediate_mode
        if word_manifold is not None:
            self.word_manifold = word_manifold
        if word_manifold_list is not None:
            self.word_manifold_list = word_manifold_list
        if clsfr_algorithm is not None:
            self.clsfr_algorithm = clsfr_algorithm
        if num_epochs is not None:
            self.num_epochs = num_epochs
        if language_model_list is not None:
            self.language_model_list = language_model_list

    @property
    def threshold(self):
        """Gets the threshold of this TrainDetails.  # noqa: E501

        There is typically some model dependent threshold to be set upon training which is possibly mutable post training. This is that threshold.  # noqa: E501

        :return: The threshold of this TrainDetails.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this TrainDetails.

        There is typically some model dependent threshold to be set upon training which is possibly mutable post training. This is that threshold.  # noqa: E501

        :param threshold: The threshold of this TrainDetails.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def temperature(self):
        """Gets the temperature of this TrainDetails.  # noqa: E501

        The softmax temperature. The lower the temperature the more pronounced the winning class' probability will be. The default is 1.0. A lower temperature is useful in a many class problem when the probabilty might otherwise be diluted amongst the classes.  # noqa: E501

        :return: The temperature of this TrainDetails.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this TrainDetails.

        The softmax temperature. The lower the temperature the more pronounced the winning class' probability will be. The default is 1.0. A lower temperature is useful in a many class problem when the probabilty might otherwise be diluted amongst the classes.  # noqa: E501

        :param temperature: The temperature of this TrainDetails.  # noqa: E501
        :type: float
        """

        self._temperature = temperature

    @property
    def immediate_mode(self):
        """Gets the immediate_mode of this TrainDetails.  # noqa: E501

        Set immediate_mode to True to do synchronous/blocking training. Might be forced to False in production.  # noqa: E501

        :return: The immediate_mode of this TrainDetails.  # noqa: E501
        :rtype: bool
        """
        return self._immediate_mode

    @immediate_mode.setter
    def immediate_mode(self, immediate_mode):
        """Sets the immediate_mode of this TrainDetails.

        Set immediate_mode to True to do synchronous/blocking training. Might be forced to False in production.  # noqa: E501

        :param immediate_mode: The immediate_mode of this TrainDetails.  # noqa: E501
        :type: bool
        """

        self._immediate_mode = immediate_mode

    @property
    def word_manifold(self):
        """Gets the word_manifold of this TrainDetails.  # noqa: E501

        The word manifold instance to use for training and later inference.  Rather use the word_manifold_list for supplying a language labelled list of word manifold instances to use in a multi-language system.   # noqa: E501

        :return: The word_manifold of this TrainDetails.  # noqa: E501
        :rtype: str
        """
        return self._word_manifold

    @word_manifold.setter
    def word_manifold(self, word_manifold):
        """Sets the word_manifold of this TrainDetails.

        The word manifold instance to use for training and later inference.  Rather use the word_manifold_list for supplying a language labelled list of word manifold instances to use in a multi-language system.   # noqa: E501

        :param word_manifold: The word_manifold of this TrainDetails.  # noqa: E501
        :type: str
        """

        self._word_manifold = word_manifold

    @property
    def word_manifold_list(self):
        """Gets the word_manifold_list of this TrainDetails.  # noqa: E501

        The list of labelled word manifolds to use for training.  # noqa: E501

        :return: The word_manifold_list of this TrainDetails.  # noqa: E501
        :rtype: list[LabelledWordManifold]
        """
        return self._word_manifold_list

    @word_manifold_list.setter
    def word_manifold_list(self, word_manifold_list):
        """Sets the word_manifold_list of this TrainDetails.

        The list of labelled word manifolds to use for training.  # noqa: E501

        :param word_manifold_list: The word_manifold_list of this TrainDetails.  # noqa: E501
        :type: list[LabelledWordManifold]
        """

        self._word_manifold_list = word_manifold_list

    @property
    def clsfr_algorithm(self):
        """Gets the clsfr_algorithm of this TrainDetails.  # noqa: E501

        The name of the algorithm that should be used for the classification.  # noqa: E501

        :return: The clsfr_algorithm of this TrainDetails.  # noqa: E501
        :rtype: str
        """
        return self._clsfr_algorithm

    @clsfr_algorithm.setter
    def clsfr_algorithm(self, clsfr_algorithm):
        """Sets the clsfr_algorithm of this TrainDetails.

        The name of the algorithm that should be used for the classification.  # noqa: E501

        :param clsfr_algorithm: The clsfr_algorithm of this TrainDetails.  # noqa: E501
        :type: str
        """

        self._clsfr_algorithm = clsfr_algorithm

    @property
    def num_epochs(self):
        """Gets the num_epochs of this TrainDetails.  # noqa: E501

        The number of epochs to train the model for.  # noqa: E501

        :return: The num_epochs of this TrainDetails.  # noqa: E501
        :rtype: int
        """
        return self._num_epochs

    @num_epochs.setter
    def num_epochs(self, num_epochs):
        """Sets the num_epochs of this TrainDetails.

        The number of epochs to train the model for.  # noqa: E501

        :param num_epochs: The num_epochs of this TrainDetails.  # noqa: E501
        :type: int
        """

        self._num_epochs = num_epochs

    @property
    def language_model_list(self):
        """Gets the language_model_list of this TrainDetails.  # noqa: E501

        The list of labelled language models used as sentence encoders.  # noqa: E501

        :return: The language_model_list of this TrainDetails.  # noqa: E501
        :rtype: list[LabelledLanguageModel]
        """
        return self._language_model_list

    @language_model_list.setter
    def language_model_list(self, language_model_list):
        """Sets the language_model_list of this TrainDetails.

        The list of labelled language models used as sentence encoders.  # noqa: E501

        :param language_model_list: The language_model_list of this TrainDetails.  # noqa: E501
        :type: list[LabelledLanguageModel]
        """

        self._language_model_list = language_model_list

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
        if issubclass(TrainDetails, dict):
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
        if not isinstance(other, TrainDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
