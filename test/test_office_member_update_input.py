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

import mfexapiclient
from mfexapiclient.models.office_member_update_input import OfficeMemberUpdateInput  # noqa: E501
from mfexapiclient.rest import ApiException

class TestOfficeMemberUpdateInput(unittest.TestCase):
    """OfficeMemberUpdateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfficeMemberUpdateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mfexapiclient.models.office_member_update_input.OfficeMemberUpdateInput()  # noqa: E501
        if include_optional :
            return OfficeMemberUpdateInput(
                name = '0',
                number = '0',
                permission_role_id = 201,
                depts_attributes = [
                    mfexapiclient.models.office_member_create_input_depts_attributes.OfficeMemberCreateInput_depts_attributes(
                        id = '0', )
                    ],
                position_attributes = mfexapiclient.models.office_member_create_input_position_attributes.OfficeMemberCreateInput_position_attributes(
                    id = '0', )
            )
        else :
            return OfficeMemberUpdateInput(
        )

    def testOfficeMemberUpdateInput(self):
        """Test OfficeMemberUpdateInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
