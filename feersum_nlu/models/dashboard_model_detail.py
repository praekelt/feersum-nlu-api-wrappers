# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.45.post3
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from feersum_nlu.models.model_revision import ModelRevision  # noqa: F401,E501


class DashboardModelDetail(object):
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
        'uuid': 'str',
        'long_name': 'str',
        'desc': 'str',
        'model_type': 'str',
        'collection_uri': 'str',
        'trashed': 'bool',
        'history': 'list[ModelRevision]'
    }

    attribute_map = {
        'name': 'name',
        'uuid': 'uuid',
        'long_name': 'long_name',
        'desc': 'desc',
        'model_type': 'model_type',
        'collection_uri': 'collection_uri',
        'trashed': 'trashed',
        'history': 'history'
    }

    def __init__(self, name=None, uuid=None, long_name=None, desc=None, model_type=None, collection_uri=None, trashed=None, history=None):  # noqa: E501
        """DashboardModelDetail - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._uuid = None
        self._long_name = None
        self._desc = None
        self._model_type = None
        self._collection_uri = None
        self._trashed = None
        self._history = None
        self.discriminator = None

        self.name = name
        if uuid is not None:
            self.uuid = uuid
        if long_name is not None:
            self.long_name = long_name
        if desc is not None:
            self.desc = desc
        self.model_type = model_type
        self.collection_uri = collection_uri
        if trashed is not None:
            self.trashed = trashed
        if history is not None:
            self.history = history

    @property
    def name(self):
        """Gets the name of this DashboardModelDetail.  # noqa: E501

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :return: The name of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DashboardModelDetail.

        The sluggy-url-friendly-name of the instance.  # noqa: E501

        :param name: The name of this DashboardModelDetail.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this DashboardModelDetail.  # noqa: E501

        A universally unique ID used to reference this revision of the model.  # noqa: E501

        :return: The uuid of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DashboardModelDetail.

        A universally unique ID used to reference this revision of the model.  # noqa: E501

        :param uuid: The uuid of this DashboardModelDetail.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def long_name(self):
        """Gets the long_name of this DashboardModelDetail.  # noqa: E501

        The human-friendly-name of the instance.  # noqa: E501

        :return: The long_name of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._long_name

    @long_name.setter
    def long_name(self, long_name):
        """Sets the long_name of this DashboardModelDetail.

        The human-friendly-name of the instance.  # noqa: E501

        :param long_name: The long_name of this DashboardModelDetail.  # noqa: E501
        :type: str
        """

        self._long_name = long_name

    @property
    def desc(self):
        """Gets the desc of this DashboardModelDetail.  # noqa: E501

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :return: The desc of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this DashboardModelDetail.

        The longer existential description of this instance's purpose in life.  # noqa: E501

        :param desc: The desc of this DashboardModelDetail.  # noqa: E501
        :type: str
        """

        self._desc = desc

    @property
    def model_type(self):
        """Gets the model_type of this DashboardModelDetail.  # noqa: E501

        The type of this model.  # noqa: E501

        :return: The model_type of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this DashboardModelDetail.

        The type of this model.  # noqa: E501

        :param model_type: The model_type of this DashboardModelDetail.  # noqa: E501
        :type: str
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def collection_uri(self):
        """Gets the collection_uri of this DashboardModelDetail.  # noqa: E501

        The URI of the model type's collection resource e.g. /faq_matchers for the collection of faq_matcher models.  # noqa: E501

        :return: The collection_uri of this DashboardModelDetail.  # noqa: E501
        :rtype: str
        """
        return self._collection_uri

    @collection_uri.setter
    def collection_uri(self, collection_uri):
        """Sets the collection_uri of this DashboardModelDetail.

        The URI of the model type's collection resource e.g. /faq_matchers for the collection of faq_matcher models.  # noqa: E501

        :param collection_uri: The collection_uri of this DashboardModelDetail.  # noqa: E501
        :type: str
        """
        if collection_uri is None:
            raise ValueError("Invalid value for `collection_uri`, must not be `None`")  # noqa: E501

        self._collection_uri = collection_uri

    @property
    def trashed(self):
        """Gets the trashed of this DashboardModelDetail.  # noqa: E501

        Whether or not this model has been deleted. Deleted models need to be loaded to be used again.  # noqa: E501

        :return: The trashed of this DashboardModelDetail.  # noqa: E501
        :rtype: bool
        """
        return self._trashed

    @trashed.setter
    def trashed(self, trashed):
        """Sets the trashed of this DashboardModelDetail.

        Whether or not this model has been deleted. Deleted models need to be loaded to be used again.  # noqa: E501

        :param trashed: The trashed of this DashboardModelDetail.  # noqa: E501
        :type: bool
        """

        self._trashed = trashed

    @property
    def history(self):
        """Gets the history of this DashboardModelDetail.  # noqa: E501

        The model's history. The history includes the current version of the model only if the last update was pushed to the history.  # noqa: E501

        :return: The history of this DashboardModelDetail.  # noqa: E501
        :rtype: list[ModelRevision]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this DashboardModelDetail.

        The model's history. The history includes the current version of the model only if the last update was pushed to the history.  # noqa: E501

        :param history: The history of this DashboardModelDetail.  # noqa: E501
        :type: list[ModelRevision]
        """

        self._history = history

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
        if issubclass(DashboardModelDetail, dict):
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
        if not isinstance(other, DashboardModelDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
