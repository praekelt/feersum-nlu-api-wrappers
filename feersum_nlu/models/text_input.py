# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0.49
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TextInput(object):
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
        'lang_code': 'str',
        'user_id': 'str',
        'session_id': 'str'
    }

    attribute_map = {
        'text': 'text',
        'lang_code': 'lang_code',
        'user_id': 'user_id',
        'session_id': 'session_id'
    }

    def __init__(self, text=None, lang_code=None, user_id=None, session_id=None):  # noqa: E501
        """TextInput - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._lang_code = None
        self._user_id = None
        self._session_id = None
        self.discriminator = None

        self.text = text
        if lang_code is not None:
            self.lang_code = lang_code
        if user_id is not None:
            self.user_id = user_id
        if session_id is not None:
            self.session_id = session_id

    @property
    def text(self):
        """Gets the text of this TextInput.  # noqa: E501

        The text input to be classified, matched or parsed.  # noqa: E501

        :return: The text of this TextInput.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextInput.

        The text input to be classified, matched or parsed.  # noqa: E501

        :param text: The text of this TextInput.  # noqa: E501
        :type: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def lang_code(self):
        """Gets the lang_code of this TextInput.  # noqa: E501

        An optional ISO 639-3 language code hint - eng, afr, nbl, xho, zul, ssw, nso, sot, tsn, ven, tso.  # noqa: E501

        :return: The lang_code of this TextInput.  # noqa: E501
        :rtype: str
        """
        return self._lang_code

    @lang_code.setter
    def lang_code(self, lang_code):
        """Sets the lang_code of this TextInput.

        An optional ISO 639-3 language code hint - eng, afr, nbl, xho, zul, ssw, nso, sot, tsn, ven, tso.  # noqa: E501

        :param lang_code: The lang_code of this TextInput.  # noqa: E501
        :type: str
        """

        self._lang_code = lang_code

    @property
    def user_id(self):
        """Gets the user_id of this TextInput.  # noqa: E501

        The user ID.  # noqa: E501

        :return: The user_id of this TextInput.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TextInput.

        The user ID.  # noqa: E501

        :param user_id: The user_id of this TextInput.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def session_id(self):
        """Gets the session_id of this TextInput.  # noqa: E501

        The session or conversation ID.  # noqa: E501

        :return: The session_id of this TextInput.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this TextInput.

        The session or conversation ID.  # noqa: E501

        :param session_id: The session_id of this TextInput.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

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
        if issubclass(TextInput, dict):
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
        if not isinstance(other, TextInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
