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


class Item(object):
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
        'id': 'str',
        'excise_id': 'str',
        'name': 'str',
        'code': 'str'
    }

    attribute_map = {
        'id': 'id',
        'excise_id': 'excise_id',
        'name': 'name',
        'code': 'code'
    }

    def __init__(self, id=None, excise_id=None, name=None, code=None, local_vars_configuration=None):  # noqa: E501
        """Item - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._excise_id = None
        self._name = None
        self._code = None
        self.discriminator = None

        self.id = id
        if excise_id is not None:
            self.excise_id = excise_id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code

    @property
    def id(self):
        """Gets the id of this Item.  # noqa: E501

        勘定科目id  # noqa: E501

        :return: The id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Item.

        勘定科目id  # noqa: E501

        :param id: The id of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 40):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `40`")  # noqa: E501

        self._id = id

    @property
    def excise_id(self):
        """Gets the excise_id of this Item.  # noqa: E501

        税区分id  # noqa: E501

        :return: The excise_id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._excise_id

    @excise_id.setter
    def excise_id(self, excise_id):
        """Sets the excise_id of this Item.

        税区分id  # noqa: E501

        :param excise_id: The excise_id of this Item.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                excise_id is not None and len(excise_id) > 40):
            raise ValueError("Invalid value for `excise_id`, length must be less than or equal to `40`")  # noqa: E501

        self._excise_id = excise_id

    @property
    def name(self):
        """Gets the name of this Item.  # noqa: E501

        勘定科目名称  # noqa: E501

        :return: The name of this Item.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Item.

        勘定科目名称  # noqa: E501

        :param name: The name of this Item.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 20):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `20`")  # noqa: E501

        self._name = name

    @property
    def code(self):
        """Gets the code of this Item.  # noqa: E501

        勘定科目コード  # noqa: E501

        :return: The code of this Item.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Item.

        勘定科目コード  # noqa: E501

        :param code: The code of this Item.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 20):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `20`")  # noqa: E501

        self._code = code

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
        if not isinstance(other, Item):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Item):
            return True

        return self.to_dict() != other.to_dict()
