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


class ExJournalBranch(object):
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
        'branch_number': 'int',
        'remark': 'str',
        'journal_branch_sides': 'list[ExJournalBranchSide]'
    }

    attribute_map = {
        'branch_number': 'branch_number',
        'remark': 'remark',
        'journal_branch_sides': 'journal_branch_sides'
    }

    def __init__(self, branch_number=None, remark=None, journal_branch_sides=None, local_vars_configuration=None):  # noqa: E501
        """ExJournalBranch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._branch_number = None
        self._remark = None
        self._journal_branch_sides = None
        self.discriminator = None

        self.branch_number = branch_number
        self.remark = remark
        if journal_branch_sides is not None:
            self.journal_branch_sides = journal_branch_sides

    @property
    def branch_number(self):
        """Gets the branch_number of this ExJournalBranch.  # noqa: E501

        行番号  # noqa: E501

        :return: The branch_number of this ExJournalBranch.  # noqa: E501
        :rtype: int
        """
        return self._branch_number

    @branch_number.setter
    def branch_number(self, branch_number):
        """Sets the branch_number of this ExJournalBranch.

        行番号  # noqa: E501

        :param branch_number: The branch_number of this ExJournalBranch.  # noqa: E501
        :type: int
        """

        self._branch_number = branch_number

    @property
    def remark(self):
        """Gets the remark of this ExJournalBranch.  # noqa: E501

        摘要  # noqa: E501

        :return: The remark of this ExJournalBranch.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ExJournalBranch.

        摘要  # noqa: E501

        :param remark: The remark of this ExJournalBranch.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                remark is not None and len(remark) > 1000):
            raise ValueError("Invalid value for `remark`, length must be less than or equal to `1000`")  # noqa: E501

        self._remark = remark

    @property
    def journal_branch_sides(self):
        """Gets the journal_branch_sides of this ExJournalBranch.  # noqa: E501

        仕訳貸借  # noqa: E501

        :return: The journal_branch_sides of this ExJournalBranch.  # noqa: E501
        :rtype: list[ExJournalBranchSide]
        """
        return self._journal_branch_sides

    @journal_branch_sides.setter
    def journal_branch_sides(self, journal_branch_sides):
        """Sets the journal_branch_sides of this ExJournalBranch.

        仕訳貸借  # noqa: E501

        :param journal_branch_sides: The journal_branch_sides of this ExJournalBranch.  # noqa: E501
        :type: list[ExJournalBranchSide]
        """

        self._journal_branch_sides = journal_branch_sides

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
        if not isinstance(other, ExJournalBranch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExJournalBranch):
            return True

        return self.to_dict() != other.to_dict()
