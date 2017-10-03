# coding: utf-8

"""
    Feersum NLU API

    This is the HTTP API for Feersum NLU

    OpenAPI spec version: 2.0.1
    
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


class Lr4InstanceDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, id=None, desc=None, model_file=None):
        """
        Lr4InstanceDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'id': 'str',
            'desc': 'str',
            'model_file': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'desc': 'desc',
            'model_file': 'model_file'
        }

        self._name = name
        self._id = id
        self._desc = desc
        self._model_file = model_file


    @property
    def name(self):
        """
        Gets the name of this Lr4InstanceDetail.
        The name of the model instance.

        :return: The name of this Lr4InstanceDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Lr4InstanceDetail.
        The name of the model instance.

        :param name: The name of this Lr4InstanceDetail.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id(self):
        """
        Gets the id of this Lr4InstanceDetail.
        The unique id of a specific version of the model instance.

        :return: The id of this Lr4InstanceDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Lr4InstanceDetail.
        The unique id of a specific version of the model instance.

        :param id: The id of this Lr4InstanceDetail.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def desc(self):
        """
        Gets the desc of this Lr4InstanceDetail.
        A longer description of the model instance's purpose in life.

        :return: The desc of this Lr4InstanceDetail.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """
        Sets the desc of this Lr4InstanceDetail.
        A longer description of the model instance's purpose in life.

        :param desc: The desc of this Lr4InstanceDetail.
        :type: str
        """

        self._desc = desc

    @property
    def model_file(self):
        """
        Gets the model_file of this Lr4InstanceDetail.
        The pre-trained model this instance was created from.

        :return: The model_file of this Lr4InstanceDetail.
        :rtype: str
        """
        return self._model_file

    @model_file.setter
    def model_file(self, model_file):
        """
        Sets the model_file of this Lr4InstanceDetail.
        The pre-trained model this instance was created from.

        :param model_file: The model_file of this Lr4InstanceDetail.
        :type: str
        """
        if model_file is None:
            raise ValueError("Invalid value for `model_file`, must not be `None`")

        self._model_file = model_file

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
