# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.41
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LabelledImageSample(object):
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
        'image': 'str',
        'label': 'str',
        'comment': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'image': 'image',
        'label': 'label',
        'comment': 'comment',
        'uuid': 'uuid'
    }

    def __init__(self, image=None, label=None, comment=None, uuid=None):  # noqa: E501
        """LabelledImageSample - a model defined in Swagger"""  # noqa: E501

        self._image = None
        self._label = None
        self._comment = None
        self._uuid = None
        self.discriminator = None

        if image is not None:
            self.image = image
        if label is not None:
            self.label = label
        if comment is not None:
            self.comment = comment
        if uuid is not None:
            self.uuid = uuid

    @property
    def image(self):
        """Gets the image of this LabelledImageSample.  # noqa: E501


        :return: The image of this LabelledImageSample.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this LabelledImageSample.


        :param image: The image of this LabelledImageSample.  # noqa: E501
        :type: str
        """
        if image is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', image):  # noqa: E501
            raise ValueError(r"Invalid value for `image`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._image = image

    @property
    def label(self):
        """Gets the label of this LabelledImageSample.  # noqa: E501


        :return: The label of this LabelledImageSample.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LabelledImageSample.


        :param label: The label of this LabelledImageSample.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def comment(self):
        """Gets the comment of this LabelledImageSample.  # noqa: E501

        A string note about the sample.  # noqa: E501

        :return: The comment of this LabelledImageSample.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this LabelledImageSample.

        A string note about the sample.  # noqa: E501

        :param comment: The comment of this LabelledImageSample.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def uuid(self):
        """Gets the uuid of this LabelledImageSample.  # noqa: E501

        The uuid of the sample.  # noqa: E501

        :return: The uuid of this LabelledImageSample.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this LabelledImageSample.

        The uuid of the sample.  # noqa: E501

        :param uuid: The uuid of this LabelledImageSample.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(LabelledImageSample, dict):
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
        if not isinstance(other, LabelledImageSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
