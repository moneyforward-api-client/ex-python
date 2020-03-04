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
from mfexapiclient.models.e_doc_meta_datum import EDocMetaDatum  # noqa: E501
from mfexapiclient.rest import ApiException

class TestEDocMetaDatum(unittest.TestCase):
    """EDocMetaDatum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EDocMetaDatum
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mfexapiclient.models.e_doc_meta_datum.EDocMetaDatum()  # noqa: E501
        if include_optional :
            return EDocMetaDatum(
                id = '0',
                number = 123,
                business_partner_name = '日本交通',
                trade_date = 2020-03-03,
                amount = null,
                ex_transactionable_type_text = '経費明細',
                ex_transactionable_number = 123,
                name = '領収書',
                document_type_text = '領収書',
                image_width = 200,
                image_height = 300,
                page_width = 595,
                page_height = 414,
                iso216_paper_size = 'A4',
                dpi = 200,
                image_depth = 256,
                timestamp_serial = 9999999999999,
                timestamp_at = 2020-03-03T19:47:46.000+09:00,
                timestamp_version = 1,
                timestamp_station_name = 'C=JP;S=Kanagawa;L=Yokohama;O=AMANO Corporation;OU=e-timing TSA;OU=Thales TSS ESN:EC0B-3BA8-XXXX;CN=dseXXX-XXX',
                timestamp_expires_at = 2030-03-03T19:47:46.000+09:00,
                scan_office_member_name = '山田　太郎',
                scan_office_member_number = '0000153'
            )
        else :
            return EDocMetaDatum(
                id = '0',
                number = 123,
                name = '領収書',
                document_type_text = '領収書',
                timestamp_serial = 9999999999999,
                timestamp_at = 2020-03-03T19:47:46.000+09:00,
                timestamp_version = 1,
                timestamp_station_name = 'C=JP;S=Kanagawa;L=Yokohama;O=AMANO Corporation;OU=e-timing TSA;OU=Thales TSS ESN:EC0B-3BA8-XXXX;CN=dseXXX-XXX',
                timestamp_expires_at = 2030-03-03T19:47:46.000+09:00,
        )

    def testEDocMetaDatum(self):
        """Test EDocMetaDatum"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
