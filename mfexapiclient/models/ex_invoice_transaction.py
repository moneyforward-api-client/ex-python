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


class ExInvoiceTransaction(object):
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
        'office_id': 'str',
        'office_member_id': 'str',
        'ex_report_id': 'str',
        'ex_destination_id': 'str',
        'dept_id': 'str',
        'project_code_id': 'str',
        'ex_item_id': 'str',
        'dr_excise_id': 'str',
        'cr_item_id': 'str',
        'cr_sub_item_id': 'str',
        'number': 'int',
        'name': 'str',
        'unit_value': 'float',
        'quantity': 'float',
        'total_value': 'int',
        'excise_value': 'int',
        'has_withholding_income_tax': 'bool',
        'withholding_income_tax_value': 'int',
        'memo': 'str',
        'currency': 'str',
        'jpyrate': 'float',
        'use_custom_jpy_rate': 'bool',
        'created_at': 'Datetime',
        'updated_at': 'Datetime',
        'office_member': 'OfficeMember',
        'ex_report': 'ExReport',
        'ex_destination': 'ExDestination',
        'dept': 'Dept',
        'project_code': 'ProjectCode',
        'ex_item': 'ExItem',
        'dr_excise': 'Excise',
        'cr_item': 'Item',
        'cr_sub_item': 'SubItem'
    }

    attribute_map = {
        'id': 'id',
        'office_id': 'office_id',
        'office_member_id': 'office_member_id',
        'ex_report_id': 'ex_report_id',
        'ex_destination_id': 'ex_destination_id',
        'dept_id': 'dept_id',
        'project_code_id': 'project_code_id',
        'ex_item_id': 'ex_item_id',
        'dr_excise_id': 'dr_excise_id',
        'cr_item_id': 'cr_item_id',
        'cr_sub_item_id': 'cr_sub_item_id',
        'number': 'number',
        'name': 'name',
        'unit_value': 'unit_value',
        'quantity': 'quantity',
        'total_value': 'total_value',
        'excise_value': 'excise_value',
        'has_withholding_income_tax': 'has_withholding_income_tax',
        'withholding_income_tax_value': 'withholding_income_tax_value',
        'memo': 'memo',
        'currency': 'currency',
        'jpyrate': 'jpyrate',
        'use_custom_jpy_rate': 'use_custom_jpy_rate',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'office_member': 'office_member',
        'ex_report': 'ex_report',
        'ex_destination': 'ex_destination',
        'dept': 'dept',
        'project_code': 'project_code',
        'ex_item': 'ex_item',
        'dr_excise': 'dr_excise',
        'cr_item': 'cr_item',
        'cr_sub_item': 'cr_sub_item'
    }

    def __init__(self, id=None, office_id=None, office_member_id=None, ex_report_id=None, ex_destination_id=None, dept_id=None, project_code_id=None, ex_item_id=None, dr_excise_id=None, cr_item_id=None, cr_sub_item_id=None, number=None, name=None, unit_value=None, quantity=None, total_value=None, excise_value=None, has_withholding_income_tax=False, withholding_income_tax_value=None, memo=None, currency='JPY', jpyrate=None, use_custom_jpy_rate=False, created_at=None, updated_at=None, office_member=None, ex_report=None, ex_destination=None, dept=None, project_code=None, ex_item=None, dr_excise=None, cr_item=None, cr_sub_item=None, local_vars_configuration=None):  # noqa: E501
        """ExInvoiceTransaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._office_id = None
        self._office_member_id = None
        self._ex_report_id = None
        self._ex_destination_id = None
        self._dept_id = None
        self._project_code_id = None
        self._ex_item_id = None
        self._dr_excise_id = None
        self._cr_item_id = None
        self._cr_sub_item_id = None
        self._number = None
        self._name = None
        self._unit_value = None
        self._quantity = None
        self._total_value = None
        self._excise_value = None
        self._has_withholding_income_tax = None
        self._withholding_income_tax_value = None
        self._memo = None
        self._currency = None
        self._jpyrate = None
        self._use_custom_jpy_rate = None
        self._created_at = None
        self._updated_at = None
        self._office_member = None
        self._ex_report = None
        self._ex_destination = None
        self._dept = None
        self._project_code = None
        self._ex_item = None
        self._dr_excise = None
        self._cr_item = None
        self._cr_sub_item = None
        self.discriminator = None

        self.id = id
        self.office_id = office_id
        self.office_member_id = office_member_id
        self.ex_report_id = ex_report_id
        if ex_destination_id is not None:
            self.ex_destination_id = ex_destination_id
        if dept_id is not None:
            self.dept_id = dept_id
        if project_code_id is not None:
            self.project_code_id = project_code_id
        if ex_item_id is not None:
            self.ex_item_id = ex_item_id
        if dr_excise_id is not None:
            self.dr_excise_id = dr_excise_id
        if cr_item_id is not None:
            self.cr_item_id = cr_item_id
        self.cr_sub_item_id = cr_sub_item_id
        self.number = number
        if name is not None:
            self.name = name
        if unit_value is not None:
            self.unit_value = unit_value
        self.quantity = quantity
        self.total_value = total_value
        self.excise_value = excise_value
        if has_withholding_income_tax is not None:
            self.has_withholding_income_tax = has_withholding_income_tax
        if withholding_income_tax_value is not None:
            self.withholding_income_tax_value = withholding_income_tax_value
        if memo is not None:
            self.memo = memo
        if currency is not None:
            self.currency = currency
        self.jpyrate = jpyrate
        self.use_custom_jpy_rate = use_custom_jpy_rate
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if office_member is not None:
            self.office_member = office_member
        if ex_report is not None:
            self.ex_report = ex_report
        if ex_destination is not None:
            self.ex_destination = ex_destination
        if dept is not None:
            self.dept = dept
        if project_code is not None:
            self.project_code = project_code
        if ex_item is not None:
            self.ex_item = ex_item
        if dr_excise is not None:
            self.dr_excise = dr_excise
        if cr_item is not None:
            self.cr_item = cr_item
        if cr_sub_item is not None:
            self.cr_sub_item = cr_sub_item

    @property
    def id(self):
        """Gets the id of this ExInvoiceTransaction.  # noqa: E501

        支払明細id  # noqa: E501

        :return: The id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExInvoiceTransaction.

        支払明細id  # noqa: E501

        :param id: The id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 40):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `40`")  # noqa: E501

        self._id = id

    @property
    def office_id(self):
        """Gets the office_id of this ExInvoiceTransaction.  # noqa: E501

        事業所id  # noqa: E501

        :return: The office_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this ExInvoiceTransaction.

        事業所id  # noqa: E501

        :param office_id: The office_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and office_id is None:  # noqa: E501
            raise ValueError("Invalid value for `office_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                office_id is not None and len(office_id) > 40):
            raise ValueError("Invalid value for `office_id`, length must be less than or equal to `40`")  # noqa: E501

        self._office_id = office_id

    @property
    def office_member_id(self):
        """Gets the office_member_id of this ExInvoiceTransaction.  # noqa: E501

        メンバーid  # noqa: E501

        :return: The office_member_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._office_member_id

    @office_member_id.setter
    def office_member_id(self, office_member_id):
        """Sets the office_member_id of this ExInvoiceTransaction.

        メンバーid  # noqa: E501

        :param office_member_id: The office_member_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and office_member_id is None:  # noqa: E501
            raise ValueError("Invalid value for `office_member_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                office_member_id is not None and len(office_member_id) > 40):
            raise ValueError("Invalid value for `office_member_id`, length must be less than or equal to `40`")  # noqa: E501

        self._office_member_id = office_member_id

    @property
    def ex_report_id(self):
        """Gets the ex_report_id of this ExInvoiceTransaction.  # noqa: E501

        申請id  # noqa: E501

        :return: The ex_report_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._ex_report_id

    @ex_report_id.setter
    def ex_report_id(self, ex_report_id):
        """Sets the ex_report_id of this ExInvoiceTransaction.

        申請id  # noqa: E501

        :param ex_report_id: The ex_report_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ex_report_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ex_report_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ex_report_id is not None and len(ex_report_id) > 40):
            raise ValueError("Invalid value for `ex_report_id`, length must be less than or equal to `40`")  # noqa: E501

        self._ex_report_id = ex_report_id

    @property
    def ex_destination_id(self):
        """Gets the ex_destination_id of this ExInvoiceTransaction.  # noqa: E501

        支払先id  # noqa: E501

        :return: The ex_destination_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._ex_destination_id

    @ex_destination_id.setter
    def ex_destination_id(self, ex_destination_id):
        """Sets the ex_destination_id of this ExInvoiceTransaction.

        支払先id  # noqa: E501

        :param ex_destination_id: The ex_destination_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ex_destination_id is not None and len(ex_destination_id) > 40):
            raise ValueError("Invalid value for `ex_destination_id`, length must be less than or equal to `40`")  # noqa: E501

        self._ex_destination_id = ex_destination_id

    @property
    def dept_id(self):
        """Gets the dept_id of this ExInvoiceTransaction.  # noqa: E501

        部門id  # noqa: E501

        :return: The dept_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._dept_id

    @dept_id.setter
    def dept_id(self, dept_id):
        """Sets the dept_id of this ExInvoiceTransaction.

        部門id  # noqa: E501

        :param dept_id: The dept_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                dept_id is not None and len(dept_id) > 40):
            raise ValueError("Invalid value for `dept_id`, length must be less than or equal to `40`")  # noqa: E501

        self._dept_id = dept_id

    @property
    def project_code_id(self):
        """Gets the project_code_id of this ExInvoiceTransaction.  # noqa: E501

        プロジェクトid  # noqa: E501

        :return: The project_code_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._project_code_id

    @project_code_id.setter
    def project_code_id(self, project_code_id):
        """Sets the project_code_id of this ExInvoiceTransaction.

        プロジェクトid  # noqa: E501

        :param project_code_id: The project_code_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                project_code_id is not None and len(project_code_id) > 40):
            raise ValueError("Invalid value for `project_code_id`, length must be less than or equal to `40`")  # noqa: E501

        self._project_code_id = project_code_id

    @property
    def ex_item_id(self):
        """Gets the ex_item_id of this ExInvoiceTransaction.  # noqa: E501

        経費科目id  # noqa: E501

        :return: The ex_item_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._ex_item_id

    @ex_item_id.setter
    def ex_item_id(self, ex_item_id):
        """Sets the ex_item_id of this ExInvoiceTransaction.

        経費科目id  # noqa: E501

        :param ex_item_id: The ex_item_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ex_item_id is not None and len(ex_item_id) > 40):
            raise ValueError("Invalid value for `ex_item_id`, length must be less than or equal to `40`")  # noqa: E501

        self._ex_item_id = ex_item_id

    @property
    def dr_excise_id(self):
        """Gets the dr_excise_id of this ExInvoiceTransaction.  # noqa: E501

        税区分id  # noqa: E501

        :return: The dr_excise_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._dr_excise_id

    @dr_excise_id.setter
    def dr_excise_id(self, dr_excise_id):
        """Sets the dr_excise_id of this ExInvoiceTransaction.

        税区分id  # noqa: E501

        :param dr_excise_id: The dr_excise_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                dr_excise_id is not None and len(dr_excise_id) > 40):
            raise ValueError("Invalid value for `dr_excise_id`, length must be less than or equal to `40`")  # noqa: E501

        self._dr_excise_id = dr_excise_id

    @property
    def cr_item_id(self):
        """Gets the cr_item_id of this ExInvoiceTransaction.  # noqa: E501

        貸方勘定科目id  # noqa: E501

        :return: The cr_item_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._cr_item_id

    @cr_item_id.setter
    def cr_item_id(self, cr_item_id):
        """Sets the cr_item_id of this ExInvoiceTransaction.

        貸方勘定科目id  # noqa: E501

        :param cr_item_id: The cr_item_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cr_item_id is not None and len(cr_item_id) > 40):
            raise ValueError("Invalid value for `cr_item_id`, length must be less than or equal to `40`")  # noqa: E501

        self._cr_item_id = cr_item_id

    @property
    def cr_sub_item_id(self):
        """Gets the cr_sub_item_id of this ExInvoiceTransaction.  # noqa: E501

        貸方補助科目id  # noqa: E501

        :return: The cr_sub_item_id of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._cr_sub_item_id

    @cr_sub_item_id.setter
    def cr_sub_item_id(self, cr_sub_item_id):
        """Sets the cr_sub_item_id of this ExInvoiceTransaction.

        貸方補助科目id  # noqa: E501

        :param cr_sub_item_id: The cr_sub_item_id of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                cr_sub_item_id is not None and len(cr_sub_item_id) > 40):
            raise ValueError("Invalid value for `cr_sub_item_id`, length must be less than or equal to `40`")  # noqa: E501

        self._cr_sub_item_id = cr_sub_item_id

    @property
    def number(self):
        """Gets the number of this ExInvoiceTransaction.  # noqa: E501

        明細番号  # noqa: E501

        :return: The number of this ExInvoiceTransaction.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this ExInvoiceTransaction.

        明細番号  # noqa: E501

        :param number: The number of this ExInvoiceTransaction.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and number is None:  # noqa: E501
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number is not None and number > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `number`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                number is not None and number < 1):  # noqa: E501
            raise ValueError("Invalid value for `number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number = number

    @property
    def name(self):
        """Gets the name of this ExInvoiceTransaction.  # noqa: E501

        品目  # noqa: E501

        :return: The name of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExInvoiceTransaction.

        品目  # noqa: E501

        :param name: The name of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def unit_value(self):
        """Gets the unit_value of this ExInvoiceTransaction.  # noqa: E501

        単価  # noqa: E501

        :return: The unit_value of this ExInvoiceTransaction.  # noqa: E501
        :rtype: float
        """
        return self._unit_value

    @unit_value.setter
    def unit_value(self, unit_value):
        """Sets the unit_value of this ExInvoiceTransaction.

        単価  # noqa: E501

        :param unit_value: The unit_value of this ExInvoiceTransaction.  # noqa: E501
        :type: float
        """

        self._unit_value = unit_value

    @property
    def quantity(self):
        """Gets the quantity of this ExInvoiceTransaction.  # noqa: E501

        数量  # noqa: E501

        :return: The quantity of this ExInvoiceTransaction.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ExInvoiceTransaction.

        数量  # noqa: E501

        :param quantity: The quantity of this ExInvoiceTransaction.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def total_value(self):
        """Gets the total_value of this ExInvoiceTransaction.  # noqa: E501

        合計金額  # noqa: E501

        :return: The total_value of this ExInvoiceTransaction.  # noqa: E501
        :rtype: int
        """
        return self._total_value

    @total_value.setter
    def total_value(self, total_value):
        """Sets the total_value of this ExInvoiceTransaction.

        合計金額  # noqa: E501

        :param total_value: The total_value of this ExInvoiceTransaction.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_value is None:  # noqa: E501
            raise ValueError("Invalid value for `total_value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                total_value is not None and total_value > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `total_value`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                total_value is not None and total_value < 1):  # noqa: E501
            raise ValueError("Invalid value for `total_value`, must be a value greater than or equal to `1`")  # noqa: E501

        self._total_value = total_value

    @property
    def excise_value(self):
        """Gets the excise_value of this ExInvoiceTransaction.  # noqa: E501

        消費税額  # noqa: E501

        :return: The excise_value of this ExInvoiceTransaction.  # noqa: E501
        :rtype: int
        """
        return self._excise_value

    @excise_value.setter
    def excise_value(self, excise_value):
        """Sets the excise_value of this ExInvoiceTransaction.

        消費税額  # noqa: E501

        :param excise_value: The excise_value of this ExInvoiceTransaction.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and excise_value is None:  # noqa: E501
            raise ValueError("Invalid value for `excise_value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                excise_value is not None and excise_value > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `excise_value`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                excise_value is not None and excise_value < 1):  # noqa: E501
            raise ValueError("Invalid value for `excise_value`, must be a value greater than or equal to `1`")  # noqa: E501

        self._excise_value = excise_value

    @property
    def has_withholding_income_tax(self):
        """Gets the has_withholding_income_tax of this ExInvoiceTransaction.  # noqa: E501

        源泉徴収有無  # noqa: E501

        :return: The has_withholding_income_tax of this ExInvoiceTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._has_withholding_income_tax

    @has_withholding_income_tax.setter
    def has_withholding_income_tax(self, has_withholding_income_tax):
        """Sets the has_withholding_income_tax of this ExInvoiceTransaction.

        源泉徴収有無  # noqa: E501

        :param has_withholding_income_tax: The has_withholding_income_tax of this ExInvoiceTransaction.  # noqa: E501
        :type: bool
        """

        self._has_withholding_income_tax = has_withholding_income_tax

    @property
    def withholding_income_tax_value(self):
        """Gets the withholding_income_tax_value of this ExInvoiceTransaction.  # noqa: E501

        源泉徴収税額  # noqa: E501

        :return: The withholding_income_tax_value of this ExInvoiceTransaction.  # noqa: E501
        :rtype: int
        """
        return self._withholding_income_tax_value

    @withholding_income_tax_value.setter
    def withholding_income_tax_value(self, withholding_income_tax_value):
        """Sets the withholding_income_tax_value of this ExInvoiceTransaction.

        源泉徴収税額  # noqa: E501

        :param withholding_income_tax_value: The withholding_income_tax_value of this ExInvoiceTransaction.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                withholding_income_tax_value is not None and withholding_income_tax_value > 4294967295):  # noqa: E501
            raise ValueError("Invalid value for `withholding_income_tax_value`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                withholding_income_tax_value is not None and withholding_income_tax_value < 1):  # noqa: E501
            raise ValueError("Invalid value for `withholding_income_tax_value`, must be a value greater than or equal to `1`")  # noqa: E501

        self._withholding_income_tax_value = withholding_income_tax_value

    @property
    def memo(self):
        """Gets the memo of this ExInvoiceTransaction.  # noqa: E501

        メモ  # noqa: E501

        :return: The memo of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this ExInvoiceTransaction.

        メモ  # noqa: E501

        :param memo: The memo of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                memo is not None and len(memo) > 1000):
            raise ValueError("Invalid value for `memo`, length must be less than or equal to `1000`")  # noqa: E501

        self._memo = memo

    @property
    def currency(self):
        """Gets the currency of this ExInvoiceTransaction.  # noqa: E501

        通貨  # noqa: E501

        :return: The currency of this ExInvoiceTransaction.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ExInvoiceTransaction.

        通貨  # noqa: E501

        :param currency: The currency of this ExInvoiceTransaction.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) > 3):
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                currency is not None and len(currency) < 3):
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._currency = currency

    @property
    def jpyrate(self):
        """Gets the jpyrate of this ExInvoiceTransaction.  # noqa: E501

        為替レート  # noqa: E501

        :return: The jpyrate of this ExInvoiceTransaction.  # noqa: E501
        :rtype: float
        """
        return self._jpyrate

    @jpyrate.setter
    def jpyrate(self, jpyrate):
        """Sets the jpyrate of this ExInvoiceTransaction.

        為替レート  # noqa: E501

        :param jpyrate: The jpyrate of this ExInvoiceTransaction.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and jpyrate is None:  # noqa: E501
            raise ValueError("Invalid value for `jpyrate`, must not be `None`")  # noqa: E501

        self._jpyrate = jpyrate

    @property
    def use_custom_jpy_rate(self):
        """Gets the use_custom_jpy_rate of this ExInvoiceTransaction.  # noqa: E501

        為替レートを手動設定するかどうか  # noqa: E501

        :return: The use_custom_jpy_rate of this ExInvoiceTransaction.  # noqa: E501
        :rtype: bool
        """
        return self._use_custom_jpy_rate

    @use_custom_jpy_rate.setter
    def use_custom_jpy_rate(self, use_custom_jpy_rate):
        """Sets the use_custom_jpy_rate of this ExInvoiceTransaction.

        為替レートを手動設定するかどうか  # noqa: E501

        :param use_custom_jpy_rate: The use_custom_jpy_rate of this ExInvoiceTransaction.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and use_custom_jpy_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `use_custom_jpy_rate`, must not be `None`")  # noqa: E501

        self._use_custom_jpy_rate = use_custom_jpy_rate

    @property
    def created_at(self):
        """Gets the created_at of this ExInvoiceTransaction.  # noqa: E501

        登録日時  # noqa: E501

        :return: The created_at of this ExInvoiceTransaction.  # noqa: E501
        :rtype: Datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ExInvoiceTransaction.

        登録日時  # noqa: E501

        :param created_at: The created_at of this ExInvoiceTransaction.  # noqa: E501
        :type: Datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ExInvoiceTransaction.  # noqa: E501

        更新日時  # noqa: E501

        :return: The updated_at of this ExInvoiceTransaction.  # noqa: E501
        :rtype: Datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ExInvoiceTransaction.

        更新日時  # noqa: E501

        :param updated_at: The updated_at of this ExInvoiceTransaction.  # noqa: E501
        :type: Datetime
        """

        self._updated_at = updated_at

    @property
    def office_member(self):
        """Gets the office_member of this ExInvoiceTransaction.  # noqa: E501


        :return: The office_member of this ExInvoiceTransaction.  # noqa: E501
        :rtype: OfficeMember
        """
        return self._office_member

    @office_member.setter
    def office_member(self, office_member):
        """Sets the office_member of this ExInvoiceTransaction.


        :param office_member: The office_member of this ExInvoiceTransaction.  # noqa: E501
        :type: OfficeMember
        """

        self._office_member = office_member

    @property
    def ex_report(self):
        """Gets the ex_report of this ExInvoiceTransaction.  # noqa: E501


        :return: The ex_report of this ExInvoiceTransaction.  # noqa: E501
        :rtype: ExReport
        """
        return self._ex_report

    @ex_report.setter
    def ex_report(self, ex_report):
        """Sets the ex_report of this ExInvoiceTransaction.


        :param ex_report: The ex_report of this ExInvoiceTransaction.  # noqa: E501
        :type: ExReport
        """

        self._ex_report = ex_report

    @property
    def ex_destination(self):
        """Gets the ex_destination of this ExInvoiceTransaction.  # noqa: E501


        :return: The ex_destination of this ExInvoiceTransaction.  # noqa: E501
        :rtype: ExDestination
        """
        return self._ex_destination

    @ex_destination.setter
    def ex_destination(self, ex_destination):
        """Sets the ex_destination of this ExInvoiceTransaction.


        :param ex_destination: The ex_destination of this ExInvoiceTransaction.  # noqa: E501
        :type: ExDestination
        """

        self._ex_destination = ex_destination

    @property
    def dept(self):
        """Gets the dept of this ExInvoiceTransaction.  # noqa: E501


        :return: The dept of this ExInvoiceTransaction.  # noqa: E501
        :rtype: Dept
        """
        return self._dept

    @dept.setter
    def dept(self, dept):
        """Sets the dept of this ExInvoiceTransaction.


        :param dept: The dept of this ExInvoiceTransaction.  # noqa: E501
        :type: Dept
        """

        self._dept = dept

    @property
    def project_code(self):
        """Gets the project_code of this ExInvoiceTransaction.  # noqa: E501


        :return: The project_code of this ExInvoiceTransaction.  # noqa: E501
        :rtype: ProjectCode
        """
        return self._project_code

    @project_code.setter
    def project_code(self, project_code):
        """Sets the project_code of this ExInvoiceTransaction.


        :param project_code: The project_code of this ExInvoiceTransaction.  # noqa: E501
        :type: ProjectCode
        """

        self._project_code = project_code

    @property
    def ex_item(self):
        """Gets the ex_item of this ExInvoiceTransaction.  # noqa: E501


        :return: The ex_item of this ExInvoiceTransaction.  # noqa: E501
        :rtype: ExItem
        """
        return self._ex_item

    @ex_item.setter
    def ex_item(self, ex_item):
        """Sets the ex_item of this ExInvoiceTransaction.


        :param ex_item: The ex_item of this ExInvoiceTransaction.  # noqa: E501
        :type: ExItem
        """

        self._ex_item = ex_item

    @property
    def dr_excise(self):
        """Gets the dr_excise of this ExInvoiceTransaction.  # noqa: E501


        :return: The dr_excise of this ExInvoiceTransaction.  # noqa: E501
        :rtype: Excise
        """
        return self._dr_excise

    @dr_excise.setter
    def dr_excise(self, dr_excise):
        """Sets the dr_excise of this ExInvoiceTransaction.


        :param dr_excise: The dr_excise of this ExInvoiceTransaction.  # noqa: E501
        :type: Excise
        """

        self._dr_excise = dr_excise

    @property
    def cr_item(self):
        """Gets the cr_item of this ExInvoiceTransaction.  # noqa: E501


        :return: The cr_item of this ExInvoiceTransaction.  # noqa: E501
        :rtype: Item
        """
        return self._cr_item

    @cr_item.setter
    def cr_item(self, cr_item):
        """Sets the cr_item of this ExInvoiceTransaction.


        :param cr_item: The cr_item of this ExInvoiceTransaction.  # noqa: E501
        :type: Item
        """

        self._cr_item = cr_item

    @property
    def cr_sub_item(self):
        """Gets the cr_sub_item of this ExInvoiceTransaction.  # noqa: E501


        :return: The cr_sub_item of this ExInvoiceTransaction.  # noqa: E501
        :rtype: SubItem
        """
        return self._cr_sub_item

    @cr_sub_item.setter
    def cr_sub_item(self, cr_sub_item):
        """Sets the cr_sub_item of this ExInvoiceTransaction.


        :param cr_sub_item: The cr_sub_item of this ExInvoiceTransaction.  # noqa: E501
        :type: SubItem
        """

        self._cr_sub_item = cr_sub_item

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
        if not isinstance(other, ExInvoiceTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExInvoiceTransaction):
            return True

        return self.to_dict() != other.to_dict()
