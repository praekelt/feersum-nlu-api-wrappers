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


class SynonymEntity(object):
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
        'ignore_word_boundaries': 'bool',
        'ignore_case': 'bool',
        'syn_set': 'list[str]',
        'index': 'int',
        'len': 'int',
        'value': 'str'
    }

    attribute_map = {
        'entity': 'entity',
        'ignore_word_boundaries': 'ignore_word_boundaries',
        'ignore_case': 'ignore_case',
        'syn_set': 'syn_set',
        'index': 'index',
        'len': 'len',
        'value': 'value'
    }

    def __init__(self, entity=None, ignore_word_boundaries=None, ignore_case=None, syn_set=None, index=None, len=None, value=None):  # noqa: E501
        """SynonymEntity - a model defined in Swagger"""  # noqa: E501

        self._entity = None
        self._ignore_word_boundaries = None
        self._ignore_case = None
        self._syn_set = None
        self._index = None
        self._len = None
        self._value = None
        self.discriminator = None

        self.entity = entity
        if ignore_word_boundaries is not None:
            self.ignore_word_boundaries = ignore_word_boundaries
        if ignore_case is not None:
            self.ignore_case = ignore_case
        if syn_set is not None:
            self.syn_set = syn_set
        if index is not None:
            self.index = index
        if len is not None:
            self.len = len
        if value is not None:
            self.value = value

    @property
    def entity(self):
        """Gets the entity of this SynonymEntity.  # noqa: E501

        The entity label/class/type.  # noqa: E501

        :return: The entity of this SynonymEntity.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this SynonymEntity.

        The entity label/class/type.  # noqa: E501

        :param entity: The entity of this SynonymEntity.  # noqa: E501
        :type: str
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501

        self._entity = entity

    @property
    def ignore_word_boundaries(self):
        """Gets the ignore_word_boundaries of this SynonymEntity.  # noqa: E501

        If True then parts of input words will also be matched. Default is False to only match input words exactly. See 'ignore_case' flag to also control the case sensitivity of the match.  # noqa: E501

        :return: The ignore_word_boundaries of this SynonymEntity.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_word_boundaries

    @ignore_word_boundaries.setter
    def ignore_word_boundaries(self, ignore_word_boundaries):
        """Sets the ignore_word_boundaries of this SynonymEntity.

        If True then parts of input words will also be matched. Default is False to only match input words exactly. See 'ignore_case' flag to also control the case sensitivity of the match.  # noqa: E501

        :param ignore_word_boundaries: The ignore_word_boundaries of this SynonymEntity.  # noqa: E501
        :type: bool
        """

        self._ignore_word_boundaries = ignore_word_boundaries

    @property
    def ignore_case(self):
        """Gets the ignore_case of this SynonymEntity.  # noqa: E501

        If True then the casing is ignored. The default is True i.e. to ignore case.  # noqa: E501

        :return: The ignore_case of this SynonymEntity.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_case

    @ignore_case.setter
    def ignore_case(self, ignore_case):
        """Sets the ignore_case of this SynonymEntity.

        If True then the casing is ignored. The default is True i.e. to ignore case.  # noqa: E501

        :param ignore_case: The ignore_case of this SynonymEntity.  # noqa: E501
        :type: bool
        """

        self._ignore_case = ignore_case

    @property
    def syn_set(self):
        """Gets the syn_set of this SynonymEntity.  # noqa: E501

        The list of synonyms associated with this entity label. One should either provide a synset OR an index and len of a specific synonym in the associated utterance.  # noqa: E501

        :return: The syn_set of this SynonymEntity.  # noqa: E501
        :rtype: list[str]
        """
        return self._syn_set

    @syn_set.setter
    def syn_set(self, syn_set):
        """Sets the syn_set of this SynonymEntity.

        The list of synonyms associated with this entity label. One should either provide a synset OR an index and len of a specific synonym in the associated utterance.  # noqa: E501

        :param syn_set: The syn_set of this SynonymEntity.  # noqa: E501
        :type: list[str]
        """

        self._syn_set = syn_set

    @property
    def index(self):
        """Gets the index of this SynonymEntity.  # noqa: E501

        The first character of the entity in the associated utterance. One should either provide a synset OR an index and len of a specific synonym in the associated utterance.  # noqa: E501

        :return: The index of this SynonymEntity.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this SynonymEntity.

        The first character of the entity in the associated utterance. One should either provide a synset OR an index and len of a specific synonym in the associated utterance.  # noqa: E501

        :param index: The index of this SynonymEntity.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def len(self):
        """Gets the len of this SynonymEntity.  # noqa: E501

        The length of the extracted entity in the associated utterance.  # noqa: E501

        :return: The len of this SynonymEntity.  # noqa: E501
        :rtype: int
        """
        return self._len

    @len.setter
    def len(self, len):
        """Sets the len of this SynonymEntity.

        The length of the extracted entity in the associated utterance.  # noqa: E501

        :param len: The len of this SynonymEntity.  # noqa: E501
        :type: int
        """

        self._len = len

    @property
    def value(self):
        """Gets the value of this SynonymEntity.  # noqa: E501

        The value of the entity as extracted from the input text. Not used during training!  # noqa: E501

        :return: The value of this SynonymEntity.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SynonymEntity.

        The value of the entity as extracted from the input text. Not used during training!  # noqa: E501

        :param value: The value of this SynonymEntity.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(SynonymEntity, dict):
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
        if not isinstance(other, SynonymEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
