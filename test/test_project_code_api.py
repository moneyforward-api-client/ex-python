# coding: utf-8

"""
    マネーフォワード クラウド経費API

    このページは[マネーフォワード クラウド経費](https://expense.moneyforward.com)（クラウド型の経費精算・ワークフローサービス）のAPIドキュメントです。ご利用開始の手順については、[github](https://github.com/moneyforward/expense-api-doc) をご覧ください。バグ報告や改善要望はgithub上からissue登録をして頂ければ幸いです。このドキュメントは[Swagger](http://swagger.io)の仕様で作成されています。実際にこのページでAPIの試打を行うことができます。試打を行いたい場合は、APIを利用するアプリケーションの登録の際に、Redirect URIを`https://expense.moneyforward.com/api/oauth2-redirect.html`に指定してお試しください。  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import moneyforward_ex
from moneyforward_ex.api.project_code_api import ProjectCodeApi  # noqa: E501
from moneyforward_ex.rest import ApiException


class TestProjectCodeApi(unittest.TestCase):
    """ProjectCodeApi unit test stubs"""

    def setUp(self):
        self.api = moneyforward_ex.api.project_code_api.ProjectCodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project_code(self):
        """Test case for create_project_code

        プロジェクトコードを作成する  # noqa: E501
        """
        pass

    def test_delete_project_code(self):
        """Test case for delete_project_code

        プロジェクトコードを削除する  # noqa: E501
        """
        pass

    def test_find_project_code(self):
        """Test case for find_project_code

        プロジェクトコードを返す  # noqa: E501
        """
        pass

    def test_find_project_codes(self):
        """Test case for find_project_codes

        プロジェクト一覧を返す  # noqa: E501
        """
        pass

    def test_update_project_code(self):
        """Test case for update_project_code

        プロジェクトコードを更新する  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
