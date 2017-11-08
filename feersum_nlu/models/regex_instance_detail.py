# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.

    OpenAPI spec version: 2.0.3
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class RegexInstanceDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, id=None, desc=None, regex=None):
        """
        RegexInstanceDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'desc': 'str',
            'regex': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'desc': 'desc',
            'regex': 'regex'
        }

        self._name = name
        self._id = id
        self._desc = desc
        self._regex = regex


    @property
    def name(self):
        """
        Gets the name of this RegexInstanceDetail.
        The sluggy-url-friendly-name of the instance.

        :return: The name of this RegexInstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RegexInstanceDetail.
        The sluggy-url-friendly-name of the instance.

        :param name: The name of this RegexInstanceDetail.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this RegexInstanceDetail.
        The unique id of a specific version of the model instance.

        :return: The id of this RegexInstanceDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RegexInstanceDetail.
        The unique id of a specific version of the model instance.

        :param id: The id of this RegexInstanceDetail.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def desc(self):
        """
        Gets the desc of this RegexInstanceDetail.
        The longer existential description of this instance's purpose in life.

        :return: The desc of this RegexInstanceDetail.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """
        Sets the desc of this RegexInstanceDetail.
        The longer existential description of this instance's purpose in life.

        :param desc: The desc of this RegexInstanceDetail.
        :type: str
        """

        self._desc = desc

    @property
    def regex(self):
        """
        Gets the regex of this RegexInstanceDetail.
        The regular expression i.e. '(?P<license>([A-Z]{3}[ ]?[0-9]{3}[ ]?(GP|NW|MP|EC|L|NC|NW)))'

        :return: The regex of this RegexInstanceDetail.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """
        Sets the regex of this RegexInstanceDetail.
        The regular expression i.e. '(?P<license>([A-Z]{3}[ ]?[0-9]{3}[ ]?(GP|NW|MP|EC|L|NC|NW)))'

        :param regex: The regex of this RegexInstanceDetail.
        :type: str
        """
        if regex is None:
            raise ValueError("Invalid value for `regex`, must not be `None`")

        self._regex = regex

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
