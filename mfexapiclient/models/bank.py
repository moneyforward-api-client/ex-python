# coding: utf-8

"""
    マネーフォワード クラウド経費API

    このページは[マネーフォワード クラウド経費](https://expense.moneyforward.com)（クラウド型の経費精算・ワークフローサービス）のAPIドキュメントです。ご利用開始の手順については、[github](https://github.com/moneyforward/expense-api-doc) をご覧ください。バグ報告や改善要望はgithub上からissue登録をして頂ければ幸いです。このドキュメントは[Swagger](http://swagger.io)の仕様で作成されています。実際にこのページでAPIの試打を行うことができます。試打を行いたい場合は、APIを利用するアプリケーションの登録の際に、Redirect URIを`https://expense.moneyforward.com/api/oauth2-redirect.html`に指定してお試しください。  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mfexapiclient.configuration import Configuration


class Bank(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'code': 'str',
        'name': 'str',
        'name_kana': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'name_kana': 'name_kana'
    }

    def __init__(self, code=None, name=None, name_kana=None, local_vars_configuration=None):  # noqa: E501
        """Bank - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._name = None
        self._name_kana = None
        self.discriminator = None

        self.code = code
        self.name = name
        self.name_kana = name_kana

    @property
    def code(self):
        """Gets the code of this Bank.  # noqa: E501

        銀行コード  # noqa: E501

        :return: The code of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Bank.

        銀行コード  # noqa: E501

        :param code: The code of this Bank.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 4):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `4`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 4):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `4`")  # noqa: E501

        self._code = code

    @property
    def name(self):
        """Gets the name of this Bank.  # noqa: E501

        銀行名  # noqa: E501

        :return: The name of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Bank.

        銀行名  # noqa: E501

        :param name: The name of this Bank.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def name_kana(self):
        """Gets the name_kana of this Bank.  # noqa: E501

        銀行名カナ  # noqa: E501

        :return: The name_kana of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._name_kana

    @name_kana.setter
    def name_kana(self, name_kana):
        """Sets the name_kana of this Bank.

        銀行名カナ  # noqa: E501

        :param name_kana: The name_kana of this Bank.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name_kana is None:  # noqa: E501
            raise ValueError("Invalid value for `name_kana`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name_kana is not None and len(name_kana) > 255):
            raise ValueError("Invalid value for `name_kana`, length must be less than or equal to `255`")  # noqa: E501

        self._name_kana = name_kana

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Bank):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Bank):
            return True

        return self.to_dict() != other.to_dict()
