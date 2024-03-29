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


class DashboardParams(object):
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
        'show_data_objects': 'bool',
        'history_size': 'int'
    }

    attribute_map = {
        'show_data_objects': 'show_data_objects',
        'history_size': 'history_size'
    }

    def __init__(self, show_data_objects=None, history_size=None):  # noqa: E501
        """DashboardParams - a model defined in Swagger"""  # noqa: E501

        self._show_data_objects = None
        self._history_size = None
        self.discriminator = None

        if show_data_objects is not None:
            self.show_data_objects = show_data_objects
        if history_size is not None:
            self.history_size = history_size

    @property
    def show_data_objects(self):
        """Gets the show_data_objects of this DashboardParams.  # noqa: E501

        Set this to True to include the data objects on the dashboard. Default is False.  # noqa: E501

        :return: The show_data_objects of this DashboardParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_data_objects

    @show_data_objects.setter
    def show_data_objects(self, show_data_objects):
        """Sets the show_data_objects of this DashboardParams.

        Set this to True to include the data objects on the dashboard. Default is False.  # noqa: E501

        :param show_data_objects: The show_data_objects of this DashboardParams.  # noqa: E501
        :type: bool
        """

        self._show_data_objects = show_data_objects

    @property
    def history_size(self):
        """Gets the history_size of this DashboardParams.  # noqa: E501

        The max size of the revision history to include for a model.  # noqa: E501

        :return: The history_size of this DashboardParams.  # noqa: E501
        :rtype: int
        """
        return self._history_size

    @history_size.setter
    def history_size(self, history_size):
        """Sets the history_size of this DashboardParams.

        The max size of the revision history to include for a model.  # noqa: E501

        :param history_size: The history_size of this DashboardParams.  # noqa: E501
        :type: int
        """

        self._history_size = history_size

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
        if issubclass(DashboardParams, dict):
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
        if not isinstance(other, DashboardParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
