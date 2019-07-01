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


class TextClassifierCreateDetails(object):
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
        'name': 'str',
        'long_name': 'str',
        'desc': 'str',
        'load_from_store': 'bool',
        'revision_uuid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'long_name': 'long_name',
        'desc': 'desc',
        'load_from_store': 'load_from_store',
        'revision_uuid': 'revision_uuid'
    }

    def __init__(self, name=None, long_name=None, desc=None, load_from_store=None, revision_uuid=None):  # noqa: E501
        """TextClassifierCreateDetails - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._long_name = None
        self._desc = None
        self._load_from_store = None
        self._revision_uuid = None
        self.discriminator = None

        self.name = name
        if long_name is not None:
            self.long_name = long_name
        if desc is not None:
            self.desc = desc
        self.load_from_store = load_from_store
        if revision_uuid is not None:
            self.revision_uuid = revision_uuid

    @property
    def name(self):
        """Gets the name of this TextClassifierCreateDetails.  # noqa: E501

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :return: The name of this TextClassifierCreateDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TextClassifierCreateDetails.

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :param name: The name of this TextClassifierCreateDetails.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def long_name(self):
        """Gets the long_name of this TextClassifierCreateDetails.  # noqa: E501

        The human-friendly-name of the instance.  # noqa: E501

        :return: The long_name of this TextClassifierCreateDetails.  # noqa: E501
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """Sets the long_name of this TextClassifierCreateDetails.

        The human-friendly-name of the instance.  # noqa: E501

        :param long_name: The long_name of this TextClassifierCreateDetails.  # noqa: E501
        :type: str
        """

        self._long_name = long_name

    @property
    def desc(self):
        """Gets the desc of this TextClassifierCreateDetails.  # noqa: E501

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :return: The desc of this TextClassifierCreateDetails.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this TextClassifierCreateDetails.

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :param desc: The desc of this TextClassifierCreateDetails.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def load_from_store(self):
        """Gets the load_from_store of this TextClassifierCreateDetails.  # noqa: E501

        Indicates if a pre-existing model with the specified name should be loaded from the trash. Usually set to False in which case a new model is created with details as specified.  # noqa: E501

        :return: The load_from_store of this TextClassifierCreateDetails.  # noqa: E501
        :rtype: bool
        """
        return self._load_from_store

    @load_from_store.setter
    def load_from_store(self, load_from_store):
        """Sets the load_from_store of this TextClassifierCreateDetails.

        Indicates if a pre-existing model with the specified name should be loaded from the trash. Usually set to False in which case a new model is created with details as specified.  # noqa: E501

        :param load_from_store: The load_from_store of this TextClassifierCreateDetails.  # noqa: E501
        :type: bool
        """
        if load_from_store is None:
            raise ValueError("Invalid value for `load_from_store`, must not be `None`")  # noqa: E501

        self._load_from_store = load_from_store

    @property
    def revision_uuid(self):
        """Gets the revision_uuid of this TextClassifierCreateDetails.  # noqa: E501

        If provided, the uuid of the revision of the model to try and load from the model history.  # noqa: E501

        :return: The revision_uuid of this TextClassifierCreateDetails.  # noqa: E501
        :rtype: str
        """
        return self._revision_uuid

    @revision_uuid.setter
    def revision_uuid(self, revision_uuid):
        """Sets the revision_uuid of this TextClassifierCreateDetails.

        If provided, the uuid of the revision of the model to try and load from the model history.  # noqa: E501

        :param revision_uuid: The revision_uuid of this TextClassifierCreateDetails.  # noqa: E501
        :type: str
        """

        self._revision_uuid = revision_uuid

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
        if not isinstance(other, TextClassifierCreateDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
