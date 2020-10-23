# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.52
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LabelledTextSample(object):
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
        'label': 'str',
        'lang_code': 'str',
        'comment': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'text': 'text',
        'label': 'label',
        'lang_code': 'lang_code',
        'comment': 'comment',
        'uuid': 'uuid'
    }

    def __init__(self, text=None, label=None, lang_code=None, comment=None, uuid=None):  # noqa: E501
        """LabelledTextSample - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._label = None
        self._lang_code = None
        self._comment = None
        self._uuid = None
        self.discriminator = None

        if text is not None:
            self.text = text
        if label is not None:
            self.label = label
        if lang_code is not None:
            self.lang_code = lang_code
        if comment is not None:
            self.comment = comment
        if uuid is not None:
            self.uuid = uuid

    @property
    def text(self):
        """Gets the text of this LabelledTextSample.  # noqa: E501


        :return: The text of this LabelledTextSample.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this LabelledTextSample.


        :param text: The text of this LabelledTextSample.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def label(self):
        """Gets the label of this LabelledTextSample.  # noqa: E501


        :return: The label of this LabelledTextSample.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LabelledTextSample.


        :param label: The label of this LabelledTextSample.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def lang_code(self):
        """Gets the lang_code of this LabelledTextSample.  # noqa: E501

        A 3 character ISO 639-3 language code - eng, afr, nbl, xho, zul, ssw, nso, sot, tsn, ven, tso.  # noqa: E501

        :return: The lang_code of this LabelledTextSample.  # noqa: E501
        :rtype: str
        """
        return self._lang_code

    @lang_code.setter
    def lang_code(self, lang_code):
        """Sets the lang_code of this LabelledTextSample.

        A 3 character ISO 639-3 language code - eng, afr, nbl, xho, zul, ssw, nso, sot, tsn, ven, tso.  # noqa: E501

        :param lang_code: The lang_code of this LabelledTextSample.  # noqa: E501
        :type: str
        """

        self._lang_code = lang_code

    @property
    def comment(self):
        """Gets the comment of this LabelledTextSample.  # noqa: E501

        A string note such as the exact answer text from a helpdesk or any other important facts about the text.  # noqa: E501

        :return: The comment of this LabelledTextSample.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this LabelledTextSample.

        A string note such as the exact answer text from a helpdesk or any other important facts about the text.  # noqa: E501

        :param comment: The comment of this LabelledTextSample.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def uuid(self):
        """Gets the uuid of this LabelledTextSample.  # noqa: E501

        The uuid of the sample.  # noqa: E501

        :return: The uuid of this LabelledTextSample.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this LabelledTextSample.

        The uuid of the sample.  # noqa: E501

        :param uuid: The uuid of this LabelledTextSample.  # noqa: E501
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
        if issubclass(LabelledTextSample, dict):
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
        if not isinstance(other, LabelledTextSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
