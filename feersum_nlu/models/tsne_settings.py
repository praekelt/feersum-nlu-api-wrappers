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


class TsneSettings(object):
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
        'n_components': 'int',
        'perplexity': 'float',
        'learning_rate': 'float'
    }

    attribute_map = {
        'n_components': 'n_components',
        'perplexity': 'perplexity',
        'learning_rate': 'learning_rate'
    }

    def __init__(self, n_components=None, perplexity=None, learning_rate=None):  # noqa: E501
        """TsneSettings - a model defined in Swagger"""  # noqa: E501

        self._n_components = None
        self._perplexity = None
        self._learning_rate = None
        self.discriminator = None

        self.n_components = n_components
        if perplexity is not None:
            self.perplexity = perplexity
        if learning_rate is not None:
            self.learning_rate = learning_rate

    @property
    def n_components(self):
        """Gets the n_components of this TsneSettings.  # noqa: E501

        Dimension of the embedded space.  # noqa: E501

        :return: The n_components of this TsneSettings.  # noqa: E501
        :rtype: int
        """
        return self._n_components

    @n_components.setter
    def n_components(self, n_components):
        """Sets the n_components of this TsneSettings.

        Dimension of the embedded space.  # noqa: E501

        :param n_components: The n_components of this TsneSettings.  # noqa: E501
        :type: int
        """
        if n_components is None:
            raise ValueError("Invalid value for `n_components`, must not be `None`")  # noqa: E501

        self._n_components = n_components

    @property
    def perplexity(self):
        """Gets the perplexity of this TsneSettings.  # noqa: E501

        The perplexity is related to the number of nearest neighbors that is used in other manifold learning algorithms. Larger datasets usually require a larger perplexity. Consider selecting a value between 5 and 50. The choice is not extremely critical since t-SNE is quite insensitive to this parameter.  # noqa: E501

        :return: The perplexity of this TsneSettings.  # noqa: E501
        :rtype: float
        """
        return self._perplexity

    @perplexity.setter
    def perplexity(self, perplexity):
        """Sets the perplexity of this TsneSettings.

        The perplexity is related to the number of nearest neighbors that is used in other manifold learning algorithms. Larger datasets usually require a larger perplexity. Consider selecting a value between 5 and 50. The choice is not extremely critical since t-SNE is quite insensitive to this parameter.  # noqa: E501

        :param perplexity: The perplexity of this TsneSettings.  # noqa: E501
        :type: float
        """

        self._perplexity = perplexity

    @property
    def learning_rate(self):
        """Gets the learning_rate of this TsneSettings.  # noqa: E501

        The learning rate for t-SNE is usually in the range [10.0, 1000.0]. If the learning rate is too high, the data may look like a ‘ball’ with any point approximately equidistant from its nearest neighbours. If the learning rate is too low, most points may look compressed in a dense cloud with few outliers. If the cost function gets stuck in a bad local minimum increasing the learning rate may help.  # noqa: E501

        :return: The learning_rate of this TsneSettings.  # noqa: E501
        :rtype: float
        """
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        """Sets the learning_rate of this TsneSettings.

        The learning rate for t-SNE is usually in the range [10.0, 1000.0]. If the learning rate is too high, the data may look like a ‘ball’ with any point approximately equidistant from its nearest neighbours. If the learning rate is too low, most points may look compressed in a dense cloud with few outliers. If the cost function gets stuck in a bad local minimum increasing the learning rate may help.  # noqa: E501

        :param learning_rate: The learning_rate of this TsneSettings.  # noqa: E501
        :type: float
        """

        self._learning_rate = learning_rate

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TsneSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
