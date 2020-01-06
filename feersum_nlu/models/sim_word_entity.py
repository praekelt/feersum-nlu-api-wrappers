# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.43.post6
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SimWordEntity(object):
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
        'similarity': 'float'
    }

    attribute_map = {
        'entity': 'entity',
        'similarity': 'similarity'
    }

    def __init__(self, entity=None, similarity=None):  # noqa: E501
        """SimWordEntity - a model defined in Swagger"""  # noqa: E501

        self._entity = None
        self._similarity = None
        self.discriminator = None

        self.entity = entity
        self.similarity = similarity

    @property
    def entity(self):
        """Gets the entity of this SimWordEntity.  # noqa: E501

        The extracted word.  # noqa: E501

        :return: The entity of this SimWordEntity.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this SimWordEntity.

        The extracted word.  # noqa: E501

        :param entity: The entity of this SimWordEntity.  # noqa: E501
        :type: str
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501

        self._entity = entity

    @property
    def similarity(self):
        """Gets the similarity of this SimWordEntity.  # noqa: E501

        The cosine similarity between the extracted word and the closest example word.  # noqa: E501

        :return: The similarity of this SimWordEntity.  # noqa: E501
        :rtype: float
        """
        return self._similarity

    @similarity.setter
    def similarity(self, similarity):
        """Sets the similarity of this SimWordEntity.

        The cosine similarity between the extracted word and the closest example word.  # noqa: E501

        :param similarity: The similarity of this SimWordEntity.  # noqa: E501
        :type: float
        """
        if similarity is None:
            raise ValueError("Invalid value for `similarity`, must not be `None`")  # noqa: E501

        self._similarity = similarity

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
        if issubclass(SimWordEntity, dict):
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
        if not isinstance(other, SimWordEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
