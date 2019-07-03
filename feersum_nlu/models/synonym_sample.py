# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.35.dev1
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from feersum_nlu.models.synonym_entity import SynonymEntity  # noqa: F401,E501


class SynonymSample(object):
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
        'text': 'str',
        'intent': 'str',
        'entity_list': 'list[SynonymEntity]'
    }

    attribute_map = {
        'text': 'text',
        'intent': 'intent',
        'entity_list': 'entity_list'
    }

    def __init__(self, text=None, intent=None, entity_list=None):  # noqa: E501
        """SynonymSample - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._intent = None
        self._entity_list = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if intent is not None:
            self.intent = intent
        if entity_list is not None:
            self.entity_list = entity_list

    @property
    def text(self):
        """Gets the text of this SynonymSample.  # noqa: E501


        :return: The text of this SynonymSample.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SynonymSample.


        :param text: The text of this SynonymSample.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def intent(self):
        """Gets the intent of this SynonymSample.  # noqa: E501


        :return: The intent of this SynonymSample.  # noqa: E501
        :rtype: str
        """
        return self._intent

    @intent.setter
    def intent(self, intent):
        """Sets the intent of this SynonymSample.


        :param intent: The intent of this SynonymSample.  # noqa: E501
        :type: str
        """

        self._intent = intent

    @property
    def entity_list(self):
        """Gets the entity_list of this SynonymSample.  # noqa: E501

        A list of labelled entities.  # noqa: E501

        :return: The entity_list of this SynonymSample.  # noqa: E501
        :rtype: list[SynonymEntity]
        """
        return self._entity_list

    @entity_list.setter
    def entity_list(self, entity_list):
        """Sets the entity_list of this SynonymSample.

        A list of labelled entities.  # noqa: E501

        :param entity_list: The entity_list of this SynonymSample.  # noqa: E501
        :type: list[SynonymEntity]
        """

        self._entity_list = entity_list

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
        if issubclass(SynonymSample, dict):
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
        if not isinstance(other, SynonymSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
