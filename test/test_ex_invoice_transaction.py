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
from mfexapiclient.models.ex_invoice_transaction import ExInvoiceTransaction  # noqa: E501
from mfexapiclient.rest import ApiException

class TestExInvoiceTransaction(unittest.TestCase):
    """ExInvoiceTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExInvoiceTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mfexapiclient.models.ex_invoice_transaction.ExInvoiceTransaction()  # noqa: E501
        if include_optional :
            return ExInvoiceTransaction(
                id = '0',
                office_id = '0',
                office_member_id = '0',
                ex_report_id = '0',
                ex_destination_id = '0',
                dept_id = '0',
                project_code_id = '0',
                ex_item_id = '0',
                dr_excise_id = '0',
                cr_item_id = '0',
                cr_sub_item_id = '0',
                number = 1,
                name = '0',
                unit_value = null,
                quantity = null,
                total_value = 1,
                excise_value = 1,
                has_withholding_income_tax = True,
                withholding_income_tax_value = 1,
                memo = '0',
                currency = 'JPY',
                jpyrate = 99999.999999,
                use_custom_jpy_rate = False,
                created_at = 2020-03-03T19:47:46.294+09:00,
                updated_at = 2020-03-03T19:47:46.294+09:00,
                office_member = mfexapiclient.models.office_member.OfficeMember(
                    id = '0',
                    identification_code = '0',
                    number = '0',
                    name = '0',
                    created_at = 2020-03-03T19:47:44.570+09:00,
                    updated_at = 2020-03-03T19:47:44.570+09:00,
                    ex_activated_at = null,
                    is_ex_user = True,
                    is_ex_authorizer = True,
                    is_ex_administrator = True,
                    ex_office_member_setting = mfexapiclient.models.ex_office_member_setting.ExOfficeMemberSetting(
                        id = '0',
                        use_agent = True,
                        approving_priority = 1,
                        default_cr_item = mfexapiclient.models.item.Item(
                            id = '0',
                            excise_id = '0',
                            name = '勘定科目名称',
                            code = 'item-code-xxx', ),
                        default_cr_sub_item = mfexapiclient.models.sub_item.SubItem(
                            id = '0',
                            item_id = '0',
                            excise_id = '0',
                            name = '補助勘定科目名称',
                            code = 'sub-item-code-xxx', ),
                        default_transportation_ex_item = mfexapiclient.models.ex_item.ExItem(
                            id = '0',
                            name = '経費科目名称',
                            code = '0',
                            is_active = True,
                            item_id = '0',
                            sub_item_id = '0',
                            default_excise_id = '0',
                            item = mfexapiclient.models.item.Item(
                                id = '0',
                                excise_id = '0',
                                name = '勘定科目名称',
                                code = 'item-code-xxx', ),
                            sub_item = mfexapiclient.models.sub_item.SubItem(
                                id = '0',
                                item_id = '0',
                                excise_id = '0',
                                name = '補助勘定科目名称',
                                code = 'sub-item-code-xxx', ),
                            default_dr_excise = mfexapiclient.models.excise.Excise(
                                id = '0',
                                long_name = '課税仕入 8%',
                                code = '税区分コード',
                                rate = 0.08, ), ),
                        default_driving_expense_ex_item = mfexapiclient.models.ex_item.ExItem(
                            id = '0',
                            name = '経費科目名称',
                            code = '0',
                            is_active = True,
                            item_id = '0',
                            sub_item_id = '0',
                            default_excise_id = '0', ),
                        default_project_code = mfexapiclient.models.dept.Dept(
                            id = '0',
                            name = '営業部',
                            memo = '0',
                            code = '0',
                            disp_order = 56,
                            is_active = True,
                            parent_id = '0',
                            root_id = '0', ), ),
                    reimburse_bank_account = mfexapiclient.models.reimburse_bank_account.ReimburseBankAccount(
                        id = '0',
                        account_type = 1,
                        number = '1234567',
                        holder_name = '山田　太郎',
                        holder_name_kana = 'ﾔﾏﾀﾞ ﾀﾛｳ',
                        bank = mfexapiclient.models.bank.Bank(
                            code = '0001',
                            name = 'みずほ銀行',
                            name_kana = 'ﾐｽﾞﾎ', ),
                        bank_branch = mfexapiclient.models.bank_branch.BankBranch(
                            code = '093',
                            name = '本店',
                            name_kana = 'ﾎﾝﾃﾝ', ), ),
                    position = mfexapiclient.models.position.Position(
                        id = '0',
                        name = '部長',
                        is_authorizer = True,
                        priority = 1, ),
                    depts = [
                        mfexapiclient.models.dept.Dept(
                            id = '0',
                            name = '営業部',
                            memo = '0',
                            code = '0',
                            disp_order = 56,
                            is_active = True,
                            parent_id = '0',
                            root_id = '0', )
                        ], ),
                ex_report = mfexapiclient.models.ex_report.ExReport(
                    id = '0',
                    ex_report_type_id = '0',
                    office_member_id = '0',
                    number = 1,
                    title = '0',
                    submitted_at = 2020-03-03T19:47:44.249+09:00,
                    approved_at = 2020-03-03T19:47:44.249+09:00,
                    created_at = 2020-03-03T19:47:44.249+09:00,
                    updated_at = 2020-03-03T19:47:44.249+09:00,
                    status = 'approved',
                    ex_report_approvals = [
                        mfexapiclient.models.ex_report_approval.ExReportApproval(
                            step = 1,
                            is_active = True,
                            approved_at = 2020-03-03T19:47:46.215+09:00,
                            approve_office_member = mfexapiclient.models.office_member.OfficeMember(
                                id = '0',
                                identification_code = '0',
                                number = '0',
                                name = '0',
                                created_at = 2020-03-03T19:47:44.570+09:00,
                                updated_at = 2020-03-03T19:47:44.570+09:00,
                                ex_activated_at = null,
                                is_ex_user = True,
                                is_ex_authorizer = True,
                                is_ex_administrator = True,
                                ex_office_member_setting = mfexapiclient.models.ex_office_member_setting.ExOfficeMemberSetting(
                                    id = '0',
                                    use_agent = True,
                                    approving_priority = 1,
                                    default_cr_item = mfexapiclient.models.item.Item(
                                        id = '0',
                                        excise_id = '0',
                                        name = '勘定科目名称',
                                        code = 'item-code-xxx', ),
                                    default_cr_sub_item = mfexapiclient.models.sub_item.SubItem(
                                        id = '0',
                                        item_id = '0',
                                        excise_id = '0',
                                        name = '補助勘定科目名称',
                                        code = 'sub-item-code-xxx', ),
                                    default_transportation_ex_item = mfexapiclient.models.ex_item.ExItem(
                                        id = '0',
                                        name = '経費科目名称',
                                        code = '0',
                                        is_active = True,
                                        item_id = '0',
                                        sub_item_id = '0',
                                        default_excise_id = '0',
                                        item = mfexapiclient.models.item.Item(
                                            id = '0',
                                            excise_id = '0',
                                            name = '勘定科目名称',
                                            code = 'item-code-xxx', ),
                                        sub_item = mfexapiclient.models.sub_item.SubItem(
                                            id = '0',
                                            item_id = '0',
                                            excise_id = '0',
                                            name = '補助勘定科目名称',
                                            code = 'sub-item-code-xxx', ),
                                        default_dr_excise = mfexapiclient.models.excise.Excise(
                                            id = '0',
                                            long_name = '課税仕入 8%',
                                            code = '税区分コード',
                                            rate = 0.08, ), ),
                                    default_driving_expense_ex_item = mfexapiclient.models.ex_item.ExItem(
                                        id = '0',
                                        name = '経費科目名称',
                                        code = '0',
                                        is_active = True,
                                        item_id = '0',
                                        sub_item_id = '0',
                                        default_excise_id = '0', ),
                                    default_project_code = mfexapiclient.models.dept.Dept(
                                        id = '0',
                                        name = '営業部',
                                        memo = '0',
                                        code = '0',
                                        disp_order = 56,
                                        is_active = True,
                                        parent_id = '0',
                                        root_id = '0', ), ),
                                reimburse_bank_account = mfexapiclient.models.reimburse_bank_account.ReimburseBankAccount(
                                    id = '0',
                                    account_type = 1,
                                    number = '1234567',
                                    holder_name = '山田　太郎',
                                    holder_name_kana = 'ﾔﾏﾀﾞ ﾀﾛｳ',
                                    bank = mfexapiclient.models.bank.Bank(
                                        code = '0001',
                                        name = 'みずほ銀行',
                                        name_kana = 'ﾐｽﾞﾎ', ),
                                    bank_branch = mfexapiclient.models.bank_branch.BankBranch(
                                        code = '093',
                                        name = '本店',
                                        name_kana = 'ﾎﾝﾃﾝ', ), ),
                                position = mfexapiclient.models.position.Position(
                                    id = '0',
                                    name = '部長',
                                    is_authorizer = True,
                                    priority = 1, ),
                                depts = [
                                    mfexapiclient.models.dept.Dept(
                                        id = '0',
                                        name = '営業部',
                                        memo = '0',
                                        code = '0',
                                        disp_order = 56,
                                        is_active = True,
                                        parent_id = '0',
                                        root_id = '0', )
                                    ], ), )
                        ], ),
                ex_destination = mfexapiclient.models.ex_destination.ExDestination(
                    id = '0',
                    name = 'A商店',
                    code = 'A001',
                    pay_day = 31,
                    number_of_months_later = 1,
                    exclude_holiday_kind = 1,
                    is_withholding_tax = False,
                    default_ex_item_id = '0',
                    default_cr_item_id = '0',
                    default_cr_sub_item_id = '0',
                    default_dept_id = '0',
                    default_project_code_id = '0',
                    withholding_tax_cr_item_id = '0',
                    withholding_tax_cr_sub_item_id = '0',
                    is_tax_include = False,
                    is_active = True,
                    priority = 0, ),
                dept = mfexapiclient.models.dept.Dept(
                    id = '0',
                    name = '営業部',
                    memo = '0',
                    code = '0',
                    disp_order = 56,
                    is_active = True,
                    parent_id = '0',
                    root_id = '0', ),
                project_code = mfexapiclient.models.project_code.ProjectCode(
                    id = '0',
                    name = '本社移転プロジェクト',
                    code = 'project-code-001',
                    priority = 0,
                    is_active = True,
                    parent_id = '0',
                    root_id = '0', ),
                ex_item = mfexapiclient.models.ex_item.ExItem(
                    id = '0',
                    name = '経費科目名称',
                    code = '0',
                    is_active = True,
                    item_id = '0',
                    sub_item_id = '0',
                    default_excise_id = '0',
                    item = mfexapiclient.models.item.Item(
                        id = '0',
                        excise_id = '0',
                        name = '勘定科目名称',
                        code = 'item-code-xxx', ),
                    sub_item = mfexapiclient.models.sub_item.SubItem(
                        id = '0',
                        item_id = '0',
                        excise_id = '0',
                        name = '補助勘定科目名称',
                        code = 'sub-item-code-xxx', ),
                    default_dr_excise = mfexapiclient.models.excise.Excise(
                        id = '0',
                        long_name = '課税仕入 8%',
                        code = '税区分コード',
                        rate = 0.08, ), ),
                dr_excise = mfexapiclient.models.excise.Excise(
                    id = '0',
                    long_name = '課税仕入 8%',
                    code = '税区分コード',
                    rate = 0.08, ),
                cr_item = mfexapiclient.models.item.Item(
                    id = '0',
                    excise_id = '0',
                    name = '勘定科目名称',
                    code = 'item-code-xxx', ),
                cr_sub_item = mfexapiclient.models.sub_item.SubItem(
                    id = '0',
                    item_id = '0',
                    excise_id = '0',
                    name = '補助勘定科目名称',
                    code = 'sub-item-code-xxx', )
            )
        else :
            return ExInvoiceTransaction(
                id = '0',
                office_id = '0',
                office_member_id = '0',
                ex_report_id = '0',
                number = 1,
                quantity = null,
                total_value = 1,
                excise_value = 1,
                jpyrate = 99999.999999,
                use_custom_jpy_rate = False,
        )

    def testExInvoiceTransaction(self):
        """Test ExInvoiceTransaction"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
