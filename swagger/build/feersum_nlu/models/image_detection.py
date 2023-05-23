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


class ImageDetection(object):
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
        'label': 'str',
        'box_x': 'float',
        'box_y': 'float',
        'box_w': 'float',
        'box_h': 'float',
        'id': 'int'
    }

    attribute_map = {
        'label': 'label',
        'box_x': 'box_x',
        'box_y': 'box_y',
        'box_w': 'box_w',
        'box_h': 'box_h',
        'id': 'id'
    }

    def __init__(self, label=None, box_x=None, box_y=None, box_w=None, box_h=None, id=None):  # noqa: E501
        """ImageDetection - a model defined in Swagger"""  # noqa: E501

        self._label = None
        self._box_x = None
        self._box_y = None
        self._box_w = None
        self._box_h = None
        self._id = None
        self.discriminator = None

        self.label = label
        self.box_x = box_x
        self.box_y = box_y
        self.box_w = box_w
        self.box_h = box_h
        self.id = id

    @property
    def label(self):
        """Gets the label of this ImageDetection.  # noqa: E501


        :return: The label of this ImageDetection.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ImageDetection.


        :param label: The label of this ImageDetection.  # noqa: E501
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def box_x(self):
        """Gets the box_x of this ImageDetection.  # noqa: E501


        :return: The box_x of this ImageDetection.  # noqa: E501
        :rtype: float
        """
        return self._box_x

    @box_x.setter
    def box_x(self, box_x):
        """Sets the box_x of this ImageDetection.


        :param box_x: The box_x of this ImageDetection.  # noqa: E501
        :type: float
        """
        if box_x is None:
            raise ValueError("Invalid value for `box_x`, must not be `None`")  # noqa: E501

        self._box_x = box_x

    @property
    def box_y(self):
        """Gets the box_y of this ImageDetection.  # noqa: E501


        :return: The box_y of this ImageDetection.  # noqa: E501
        :rtype: float
        """
        return self._box_y

    @box_y.setter
    def box_y(self, box_y):
        """Sets the box_y of this ImageDetection.


        :param box_y: The box_y of this ImageDetection.  # noqa: E501
        :type: float
        """
        if box_y is None:
            raise ValueError("Invalid value for `box_y`, must not be `None`")  # noqa: E501

        self._box_y = box_y

    @property
    def box_w(self):
        """Gets the box_w of this ImageDetection.  # noqa: E501


        :return: The box_w of this ImageDetection.  # noqa: E501
        :rtype: float
        """
        return self._box_w

    @box_w.setter
    def box_w(self, box_w):
        """Sets the box_w of this ImageDetection.


        :param box_w: The box_w of this ImageDetection.  # noqa: E501
        :type: float
        """
        if box_w is None:
            raise ValueError("Invalid value for `box_w`, must not be `None`")  # noqa: E501

        self._box_w = box_w

    @property
    def box_h(self):
        """Gets the box_h of this ImageDetection.  # noqa: E501


        :return: The box_h of this ImageDetection.  # noqa: E501
        :rtype: float
        """
        return self._box_h

    @box_h.setter
    def box_h(self, box_h):
        """Sets the box_h of this ImageDetection.


        :param box_h: The box_h of this ImageDetection.  # noqa: E501
        :type: float
        """
        if box_h is None:
            raise ValueError("Invalid value for `box_h`, must not be `None`")  # noqa: E501

        self._box_h = box_h

    @property
    def id(self):
        """Gets the id of this ImageDetection.  # noqa: E501


        :return: The id of this ImageDetection.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageDetection.


        :param id: The id of this ImageDetection.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if issubclass(ImageDetection, dict):
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
        if not isinstance(other, ImageDetection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
