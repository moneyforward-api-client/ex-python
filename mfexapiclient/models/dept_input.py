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


class DeptInput(object):
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
        'name': 'str',
        'memo': 'str',
        'code': 'str',
        'disp_order': 'int',
        'is_active': 'bool',
        'parent_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'memo': 'memo',
        'code': 'code',
        'disp_order': 'disp_order',
        'is_active': 'is_active',
        'parent_id': 'parent_id'
    }

    def __init__(self, name=None, memo=None, code=None, disp_order=0, is_active=True, parent_id=None, local_vars_configuration=None):  # noqa: E501
        """DeptInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._memo = None
        self._code = None
        self._disp_order = None
        self._is_active = None
        self._parent_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if memo is not None:
            self.memo = memo
        if code is not None:
            self.code = code
        if disp_order is not None:
            self.disp_order = disp_order
        if is_active is not None:
            self.is_active = is_active
        if parent_id is not None:
            self.parent_id = parent_id

    @property
    def name(self):
        """Gets the name of this DeptInput.  # noqa: E501

        部門名称  # noqa: E501

        :return: The name of this DeptInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeptInput.

        部門名称  # noqa: E501

        :param name: The name of this DeptInput.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 40):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `40`")  # noqa: E501

        self._name = name

    @property
    def memo(self):
        """Gets the memo of this DeptInput.  # noqa: E501

        メモ  # noqa: E501

        :return: The memo of this DeptInput.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this DeptInput.

        メモ  # noqa: E501

        :param memo: The memo of this DeptInput.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                memo is not None and len(memo) > 200):
            raise ValueError("Invalid value for `memo`, length must be less than or equal to `200`")  # noqa: E501

        self._memo = memo

    @property
    def code(self):
        """Gets the code of this DeptInput.  # noqa: E501

        コード  # noqa: E501

        :return: The code of this DeptInput.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DeptInput.

        コード  # noqa: E501

        :param code: The code of this DeptInput.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 20):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `20`")  # noqa: E501

        self._code = code

    @property
    def disp_order(self):
        """Gets the disp_order of this DeptInput.  # noqa: E501

        表示優先順（昇順）  # noqa: E501

        :return: The disp_order of this DeptInput.  # noqa: E501
        :rtype: int
        """
        return self._disp_order

    @disp_order.setter
    def disp_order(self, disp_order):
        """Sets the disp_order of this DeptInput.

        表示優先順（昇順）  # noqa: E501

        :param disp_order: The disp_order of this DeptInput.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                disp_order is not None and disp_order > 65534):  # noqa: E501
            raise ValueError("Invalid value for `disp_order`, must be a value less than or equal to `65534`")  # noqa: E501

        self._disp_order = disp_order

    @property
    def is_active(self):
        """Gets the is_active of this DeptInput.  # noqa: E501

        表示フラグをオフで新規の経費登録等の選択肢に表示されなくなります  # noqa: E501

        :return: The is_active of this DeptInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this DeptInput.

        表示フラグをオフで新規の経費登録等の選択肢に表示されなくなります  # noqa: E501

        :param is_active: The is_active of this DeptInput.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def parent_id(self):
        """Gets the parent_id of this DeptInput.  # noqa: E501

        親部門のid  # noqa: E501

        :return: The parent_id of this DeptInput.  # noqa: E501
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this DeptInput.

        親部門のid  # noqa: E501

        :param parent_id: The parent_id of this DeptInput.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                parent_id is not None and len(parent_id) > 40):
            raise ValueError("Invalid value for `parent_id`, length must be less than or equal to `40`")  # noqa: E501

        self._parent_id = parent_id

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
        if not isinstance(other, DeptInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeptInput):
            return True

        return self.to_dict() != other.to_dict()
