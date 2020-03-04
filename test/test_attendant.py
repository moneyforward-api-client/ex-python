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
from mfexapiclient.models.attendant import Attendant  # noqa: E501
from mfexapiclient.rest import ApiException

class TestAttendant(unittest.TestCase):
    """Attendant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Attendant
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mfexapiclient.models.attendant.Attendant()  # noqa: E501
        if include_optional :
            return Attendant(
                id = '0',
                name = '山田太郎',
                company_name = 'A株式会社',
                department_name = '営業部',
                position_name = '部長',
                is_own_company = False
            )
        else :
            return Attendant(
                id = '0',
                name = '山田太郎',
                company_name = 'A株式会社',
                is_own_company = False,
        )

    def testAttendant(self):
        """Test Attendant"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
