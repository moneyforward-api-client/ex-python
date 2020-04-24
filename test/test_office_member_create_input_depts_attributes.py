# coding: utf-8

"""
    マネーフォワード クラウド経費API

    このページは[マネーフォワード クラウド経費](https://expense.moneyforward.com)（クラウド型の経費精算・ワークフローサービス）のAPIドキュメントです。ご利用開始の手順については、[github](https://github.com/moneyforward/expense-api-doc) をご覧ください。バグ報告や改善要望はgithub上からissue登録をして頂ければ幸いです。このドキュメントは[Swagger](http://swagger.io)の仕様で作成されています。実際にこのページでAPIの試打を行うことができます。試打を行いたい場合は、APIを利用するアプリケーションの登録の際に、Redirect URIを`https://expense.moneyforward.com/api/oauth2-redirect.html`に指定してお試しください。  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import moneyforward_ex
from moneyforward_ex.models.office_member_create_input_depts_attributes import OfficeMemberCreateInputDeptsAttributes  # noqa: E501
from moneyforward_ex.rest import ApiException

class TestOfficeMemberCreateInputDeptsAttributes(unittest.TestCase):
    """OfficeMemberCreateInputDeptsAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfficeMemberCreateInputDeptsAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = moneyforward_ex.models.office_member_create_input_depts_attributes.OfficeMemberCreateInputDeptsAttributes()  # noqa: E501
        if include_optional :
            return OfficeMemberCreateInputDeptsAttributes(
                id = '0'
            )
        else :
            return OfficeMemberCreateInputDeptsAttributes(
        )

    def testOfficeMemberCreateInputDeptsAttributes(self):
        """Test OfficeMemberCreateInputDeptsAttributes"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
