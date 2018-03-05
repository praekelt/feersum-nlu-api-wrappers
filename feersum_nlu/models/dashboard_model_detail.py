# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.20
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


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
        'long_name': 'str',
        'desc': 'str',
        'model_type': 'str',
        'trashed': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'long_name': 'long_name',
        'desc': 'desc',
        'model_type': 'model_type',
        'trashed': 'trashed'
    }

    def __init__(self, name=None, long_name=None, desc=None, model_type=None, trashed=None):  # noqa: E501
        """DashboardModelDetail - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._long_name = None
        self._desc = None
        self._model_type = None
        self._trashed = None
        self.discriminator = None

        self.name = name
        if long_name is not None:
            self.long_name = long_name
        if desc is not None:
            self.desc = desc
        self.model_type = model_type
        if trashed is not None:
            self.trashed = trashed

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
        if not isinstance(other, DashboardModelDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
