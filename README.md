# ex-python

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install moneyforward-ex
```

Then import the package:
```python
import moneyforward_ex
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import moneyforward_ex
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import moneyforward_ex
from moneyforward_ex.rest import ApiException
from pprint import pprint

configuration = moneyforward_ex.Configuration()
# Configure OAuth2 access token for authorization: mf_expense_oauth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://expense.moneyforward.com
configuration.host = "https://expense.moneyforward.com"

# Enter a context with an instance of the API client
with moneyforward_ex.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = moneyforward_ex.DeptApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    unknown_base_type = moneyforward_ex.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 部門のパラメータ

    try:
        # 部門を作成する
        api_response = api_instance.create_dept(office_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeptApi->create_dept: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://expense.moneyforward.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeptApi* | [**create_dept**](docs/DeptApi.md#create_dept) | **POST** /api/external/v1/offices/{office_id}/depts | 部門を作成する
*DeptApi* | [**delete_dept**](docs/DeptApi.md#delete_dept) | **DELETE** /api/external/v1/offices/{office_id}/depts/{id} | 部門を削除する
*DeptApi* | [**find_dept**](docs/DeptApi.md#find_dept) | **GET** /api/external/v1/offices/{office_id}/depts/{id} | 部門を返す
*DeptApi* | [**find_depts**](docs/DeptApi.md#find_depts) | **GET** /api/external/v1/offices/{office_id}/depts | 部門一覧を返す
*DeptApi* | [**update_dept**](docs/DeptApi.md#update_dept) | **PUT** /api/external/v1/offices/{office_id}/depts/{id} | 部門を更新する
*EDocApi* | [**find_e_docs**](docs/EDocApi.md#find_e_docs) | **GET** /api/external/v1/offices/{office_id}/e_docs | 電子帳簿保存法書類情報を返す
*EDocApi* | [**send_mf_file_belongs_to_e_doc**](docs/EDocApi.md#send_mf_file_belongs_to_e_doc) | **GET** /api/external/v1/offices/{office_id}/e_docs/{e_doc_id}/mf_file | 電子帳簿保存法書類データに紐づく画像ファイルを返す
*ExDestinationApi* | [**create_ex_destination**](docs/ExDestinationApi.md#create_ex_destination) | **POST** /api/external/v1/offices/{office_id}/ex_destinations | 支払先マスタを作成する
*ExDestinationApi* | [**delete_ex_destination**](docs/ExDestinationApi.md#delete_ex_destination) | **DELETE** /api/external/v1/offices/{office_id}/ex_destinations/{id} | 支払先マスタを削除する
*ExDestinationApi* | [**find_ex_destination**](docs/ExDestinationApi.md#find_ex_destination) | **GET** /api/external/v1/offices/{office_id}/ex_destinations/{id} | 支払先マスタを返す
*ExDestinationApi* | [**find_ex_destinations**](docs/ExDestinationApi.md#find_ex_destinations) | **GET** /api/external/v1/offices/{office_id}/ex_destinations | 支払先マスタ一覧を返す
*ExDestinationApi* | [**update_ex_destination**](docs/ExDestinationApi.md#update_ex_destination) | **PUT** /api/external/v1/offices/{office_id}/ex_destinations/{id} | 支払先マスタを更新する
*ExInvoiceTransactionApi* | [**find_office_ex_invoice_transactions**](docs/ExInvoiceTransactionApi.md#find_office_ex_invoice_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_invoice_transactions | 事業所全体の支払明細リストを返す
*ExItemApi* | [**find_ex_item**](docs/ExItemApi.md#find_ex_item) | **GET** /api/external/v1/offices/{office_id}/ex_items/{id} | 経費科目を返す
*ExItemApi* | [**find_ex_items**](docs/ExItemApi.md#find_ex_items) | **GET** /api/external/v1/offices/{office_id}/ex_items | 経費科目一覧を返す
*ExJournalApi* | [**find_office_ex_journals_by_ex_reports**](docs/ExJournalApi.md#find_office_ex_journals_by_ex_reports) | **GET** /api/external/v1/offices/{office_id}/ex_journals_by_ex_reports | 事業所全体の申請に紐づく仕訳リストを返す
*ExJournalApi* | [**find_office_ex_journals_by_ex_transactions**](docs/ExJournalApi.md#find_office_ex_journals_by_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_journals_by_ex_transactions | 事業所全体の明細に紐づく仕訳リストを返す
*ExJournalApi* | [**find_office_ex_report_journal**](docs/ExJournalApi.md#find_office_ex_report_journal) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_id}/ex_journal | 申請に対応する仕訳を返す
*ExJournalApi* | [**find_office_ex_report_unit_journal**](docs/ExJournalApi.md#find_office_ex_report_unit_journal) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_unit_id}/ex_journal | 集計に対応する仕訳を返す
*ExJournalApi* | [**find_office_ex_transaction_journal**](docs/ExJournalApi.md#find_office_ex_transaction_journal) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{ex_transaction_id}/ex_journal | 経費明細に対応する仕訳を返す
*ExOfficeMemberSettingApi* | [**find_ex_office_member_setting**](docs/ExOfficeMemberSettingApi.md#find_ex_office_member_setting) | **GET** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/ex_office_member_setting | メンバーの経費設定を返す
*ExOfficeMemberSettingApi* | [**update_ex_office_member_setting**](docs/ExOfficeMemberSettingApi.md#update_ex_office_member_setting) | **PUT** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/ex_office_member_setting | メンバーの経費設定を更新する
*ExReportApi* | [**find_ex_report_ex_transactions**](docs/ExReportApi.md#find_ex_report_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_id}/ex_transactions | 経費申請に含まれる経費明細リストを返す
*ExReportApi* | [**find_office_approving_ex_reports**](docs/ExReportApi.md#find_office_approving_ex_reports) | **GET** /api/external/v1/offices/{office_id}/approving_ex_reports | 事業所全体の承認待ちリストを返す
*ExReportApi* | [**find_office_ex_journals_by_ex_reports**](docs/ExReportApi.md#find_office_ex_journals_by_ex_reports) | **GET** /api/external/v1/offices/{office_id}/ex_journals_by_ex_reports | 事業所全体の申請に紐づく仕訳リストを返す
*ExReportApi* | [**find_office_ex_report**](docs/ExReportApi.md#find_office_ex_report) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{id} | 事業所全体の申請を返す
*ExReportApi* | [**find_office_ex_report_journal**](docs/ExReportApi.md#find_office_ex_report_journal) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_id}/ex_journal | 申請に対応する仕訳を返す
*ExReportApi* | [**find_office_ex_report_me**](docs/ExReportApi.md#find_office_ex_report_me) | **GET** /api/external/v1/offices/{office_id}/me/ex_reports/{id} | 自分の申請を返す
*ExReportApi* | [**find_office_ex_reports**](docs/ExReportApi.md#find_office_ex_reports) | **GET** /api/external/v1/offices/{office_id}/ex_reports | 事業所全体の申請リストを返す
*ExReportApi* | [**find_office_ex_reports_me**](docs/ExReportApi.md#find_office_ex_reports_me) | **GET** /api/external/v1/offices/{office_id}/me/ex_reports | 自分の申請リストを返す
*ExReportApi* | [**find_office_member_approving_ex_reports**](docs/ExReportApi.md#find_office_member_approving_ex_reports) | **GET** /api/external/v1/offices/{office_id}/me/approving_ex_reports | 自分の承認待ちリストを返す
*ExReportUnitApi* | [**find_ex_report_unit_ex_transactions**](docs/ExReportUnitApi.md#find_ex_report_unit_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_report_units/{ex_report_unit_id}/ex_transactions | 経費集計に含まれる経費明細リストを返す
*ExReportUnitApi* | [**find_office_ex_report_unit**](docs/ExReportUnitApi.md#find_office_ex_report_unit) | **GET** /api/external/v1/offices/{office_id}/ex_report_units/{id} | 集計を返す
*ExReportUnitApi* | [**find_office_ex_report_unit_journal**](docs/ExReportUnitApi.md#find_office_ex_report_unit_journal) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_unit_id}/ex_journal | 集計に対応する仕訳を返す
*ExReportUnitApi* | [**find_office_ex_report_units**](docs/ExReportUnitApi.md#find_office_ex_report_units) | **GET** /api/external/v1/offices/{office_id}/ex_report_units | 集計のリストを返す
*ExTransactionApi* | [**create_ex_transaction**](docs/ExTransactionApi.md#create_ex_transaction) | **POST** /api/external/v1/offices/{office_id}/me/ex_transactions | 自分の経費明細を追加する
*ExTransactionApi* | [**create_office_ex_transaction**](docs/ExTransactionApi.md#create_office_ex_transaction) | **POST** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/ex_transactions | 経費明細を追加する
*ExTransactionApi* | [**destroy_ex_transaction**](docs/ExTransactionApi.md#destroy_ex_transaction) | **DELETE** /api/external/v1/offices/{office_id}/me/ex_transactions/{id} | 自分の経費明細を削除する
*ExTransactionApi* | [**destroy_office_ex_transaction**](docs/ExTransactionApi.md#destroy_office_ex_transaction) | **DELETE** /api/external/v1/offices/{office_id}/ex_transactions/{id} | 事業所全体の指定idの経費明細を削除する
*ExTransactionApi* | [**find_ex_report_ex_transactions**](docs/ExTransactionApi.md#find_ex_report_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_id}/ex_transactions | 経費申請に含まれる経費明細リストを返す
*ExTransactionApi* | [**find_ex_report_unit_ex_transactions**](docs/ExTransactionApi.md#find_ex_report_unit_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_report_units/{ex_report_unit_id}/ex_transactions | 経費集計に含まれる経費明細リストを返す
*ExTransactionApi* | [**find_ex_transaction**](docs/ExTransactionApi.md#find_ex_transaction) | **GET** /api/external/v1/offices/{office_id}/me/ex_transactions/{id} | 自分の経費明細を返す
*ExTransactionApi* | [**find_ex_transactions**](docs/ExTransactionApi.md#find_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/me/ex_transactions | 自分の経費明細リストを返す
*ExTransactionApi* | [**find_office_ex_journals_by_ex_transactions**](docs/ExTransactionApi.md#find_office_ex_journals_by_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_journals_by_ex_transactions | 事業所全体の明細に紐づく仕訳リストを返す
*ExTransactionApi* | [**find_office_ex_transaction**](docs/ExTransactionApi.md#find_office_ex_transaction) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{id} | 事業所全体の指定idの経費明細を返す
*ExTransactionApi* | [**find_office_ex_transaction_journal**](docs/ExTransactionApi.md#find_office_ex_transaction_journal) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{ex_transaction_id}/ex_journal | 経費明細に対応する仕訳を返す
*ExTransactionApi* | [**find_office_ex_transaction_mf_file**](docs/ExTransactionApi.md#find_office_ex_transaction_mf_file) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{ex_transaction_id}/mf_file | 経費明細に紐づく添付ファイルを返す
*ExTransactionApi* | [**find_office_ex_transaction_mf_file_me**](docs/ExTransactionApi.md#find_office_ex_transaction_mf_file_me) | **GET** /api/external/v1/offices/{office_id}/me/ex_transactions/{ex_transaction_id}/mf_file | 経費明細に紐づく添付ファイルを返す
*ExTransactionApi* | [**find_office_ex_transactions**](docs/ExTransactionApi.md#find_office_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_transactions | 事業所全体の経費明細リストを返す
*ExTransactionApi* | [**update_ex_transaction**](docs/ExTransactionApi.md#update_ex_transaction) | **PUT** /api/external/v1/offices/{office_id}/me/ex_transactions/{id} | 自分の経費明細を更新する
*ExTransactionApi* | [**update_office_ex_transaction**](docs/ExTransactionApi.md#update_office_ex_transaction) | **PUT** /api/external/v1/offices/{office_id}/ex_transactions/{id} | 事業所全体の指定idの経費明細を更新する
*ExTransactionApi* | [**upload_member_receipt**](docs/ExTransactionApi.md#upload_member_receipt) | **POST** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/upload_receipt | 領収書をアップロードして経費登録する
*ExTransactionApi* | [**upload_receipt**](docs/ExTransactionApi.md#upload_receipt) | **POST** /api/external/v1/offices/{office_id}/me/upload_receipt | 自分の領収書をアップロードして経費登録する
*ExciseApi* | [**find_excise**](docs/ExciseApi.md#find_excise) | **GET** /api/external/v1/offices/{office_id}/excises/{id} | 税区分を返す
*ExciseApi* | [**find_excises**](docs/ExciseApi.md#find_excises) | **GET** /api/external/v1/offices/{office_id}/excises | 税区分一覧を返す
*MfFileApi* | [**find_office_ex_transaction_mf_file**](docs/MfFileApi.md#find_office_ex_transaction_mf_file) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{ex_transaction_id}/mf_file | 経費明細に紐づく添付ファイルを返す
*MfFileApi* | [**find_office_ex_transaction_mf_file_me**](docs/MfFileApi.md#find_office_ex_transaction_mf_file_me) | **GET** /api/external/v1/offices/{office_id}/me/ex_transactions/{ex_transaction_id}/mf_file | 経費明細に紐づく添付ファイルを返す
*MfFileApi* | [**send_mf_file_belongs_to_e_doc**](docs/MfFileApi.md#send_mf_file_belongs_to_e_doc) | **GET** /api/external/v1/offices/{office_id}/e_docs/{e_doc_id}/mf_file | 電子帳簿保存法書類データに紐づく画像ファイルを返す
*OfficeApi* | [**find_offices**](docs/OfficeApi.md#find_offices) | **GET** /api/external/v1/offices | 自分が所属する事業所一覧を返す
*OfficeMemberApi* | [**create_office_member**](docs/OfficeMemberApi.md#create_office_member) | **POST** /api/external/v1/offices/{office_id}/office_members | メンバーを追加する
*OfficeMemberApi* | [**destroy_office_member**](docs/OfficeMemberApi.md#destroy_office_member) | **DELETE** /api/external/v1/offices/{office_id}/office_members/{id} | メンバーを削除する
*OfficeMemberApi* | [**destroy_reimburse_bank_account**](docs/OfficeMemberApi.md#destroy_reimburse_bank_account) | **DELETE** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/reimburse_bank_account | メンバーの振込口座を削除する
*OfficeMemberApi* | [**find_office_member**](docs/OfficeMemberApi.md#find_office_member) | **GET** /api/external/v1/offices/{office_id}/office_members/{id} | 事業所に所属するメンバーを返す
*OfficeMemberApi* | [**find_office_members**](docs/OfficeMemberApi.md#find_office_members) | **GET** /api/external/v1/offices/{office_id}/office_members | 事業所に所属するメンバー一覧を返す
*OfficeMemberApi* | [**save_reimburse_bank_account**](docs/OfficeMemberApi.md#save_reimburse_bank_account) | **PUT** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/reimburse_bank_account | メンバーの振込口座を登録／更新する
*OfficeMemberApi* | [**update_office_member**](docs/OfficeMemberApi.md#update_office_member) | **PUT** /api/external/v1/offices/{office_id}/office_members/{id} | メンバーを更新する
*PositionApi* | [**create_position**](docs/PositionApi.md#create_position) | **POST** /api/external/v1/offices/{office_id}/positions | 役職を作成する
*PositionApi* | [**delete_position**](docs/PositionApi.md#delete_position) | **DELETE** /api/external/v1/offices/{office_id}/positions/{id} | 役職を削除する
*PositionApi* | [**find_position**](docs/PositionApi.md#find_position) | **GET** /api/external/v1/offices/{office_id}/positions/{id} | 役職を返す
*PositionApi* | [**find_positions**](docs/PositionApi.md#find_positions) | **GET** /api/external/v1/offices/{office_id}/positions | 役職一覧を返す
*PositionApi* | [**update_position**](docs/PositionApi.md#update_position) | **PUT** /api/external/v1/offices/{office_id}/positions/{id} | 役職を更新する
*ProjectCodeApi* | [**create_project_code**](docs/ProjectCodeApi.md#create_project_code) | **POST** /api/external/v1/offices/{office_id}/project_codes | プロジェクトコードを作成する
*ProjectCodeApi* | [**delete_project_code**](docs/ProjectCodeApi.md#delete_project_code) | **DELETE** /api/external/v1/offices/{office_id}/project_codes/{id} | プロジェクトコードを削除する
*ProjectCodeApi* | [**find_project_code**](docs/ProjectCodeApi.md#find_project_code) | **GET** /api/external/v1/offices/{office_id}/project_codes/{id} | プロジェクトコードを返す
*ProjectCodeApi* | [**find_project_codes**](docs/ProjectCodeApi.md#find_project_codes) | **GET** /api/external/v1/offices/{office_id}/project_codes | プロジェクト一覧を返す
*ProjectCodeApi* | [**update_project_code**](docs/ProjectCodeApi.md#update_project_code) | **PUT** /api/external/v1/offices/{office_id}/project_codes/{id} | プロジェクトコードを更新する


## Documentation For Models

 - [Attendant](docs/Attendant.md)
 - [Bank](docs/Bank.md)
 - [BankBranch](docs/BankBranch.md)
 - [Dept](docs/Dept.md)
 - [DeptInput](docs/DeptInput.md)
 - [EDocMetaDatum](docs/EDocMetaDatum.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [ExDestination](docs/ExDestination.md)
 - [ExDestinationInput](docs/ExDestinationInput.md)
 - [ExInvoiceTransaction](docs/ExInvoiceTransaction.md)
 - [ExItem](docs/ExItem.md)
 - [ExJournal](docs/ExJournal.md)
 - [ExJournalBranch](docs/ExJournalBranch.md)
 - [ExJournalBranchSide](docs/ExJournalBranchSide.md)
 - [ExOfficeMemberSetting](docs/ExOfficeMemberSetting.md)
 - [ExOfficeMemberSettingInput](docs/ExOfficeMemberSettingInput.md)
 - [ExReport](docs/ExReport.md)
 - [ExReportApproval](docs/ExReportApproval.md)
 - [ExReportType](docs/ExReportType.md)
 - [ExReportUnit](docs/ExReportUnit.md)
 - [ExTransaction](docs/ExTransaction.md)
 - [ExTransactionCreateInput](docs/ExTransactionCreateInput.md)
 - [ExTransactionUpdateInput](docs/ExTransactionUpdateInput.md)
 - [Excise](docs/Excise.md)
 - [Item](docs/Item.md)
 - [MfFile](docs/MfFile.md)
 - [Office](docs/Office.md)
 - [OfficeMember](docs/OfficeMember.md)
 - [OfficeMemberCreateInput](docs/OfficeMemberCreateInput.md)
 - [OfficeMemberCreateInputDeptsAttributes](docs/OfficeMemberCreateInputDeptsAttributes.md)
 - [OfficeMemberCreateInputPositionAttributes](docs/OfficeMemberCreateInputPositionAttributes.md)
 - [OfficeMemberUpdateInput](docs/OfficeMemberUpdateInput.md)
 - [Position](docs/Position.md)
 - [PositionInput](docs/PositionInput.md)
 - [ProjectCode](docs/ProjectCode.md)
 - [ProjectCodeInput](docs/ProjectCodeInput.md)
 - [ReceiptInput](docs/ReceiptInput.md)
 - [ReimburseBankAccount](docs/ReimburseBankAccount.md)
 - [ReimburseBankAccountInput](docs/ReimburseBankAccountInput.md)
 - [SubItem](docs/SubItem.md)


## Documentation For Authorization


## mf_expense_oauth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: /oauth/authorize
- **Scopes**:
 - **office_setting:write**: 事業所の設定から、事業所のメンバーの設定まで管理できる権限
 - **user_setting:write**: ユーザー自身の設定を管理できる権限
 - **transaction:write**: 経費明細の読み書きができる権限
 - **report:write**: 申請の読み書きができる権限
 - **account:write**: 口座・カードの管理が出来る権限
 - **public_resource:read**: 公開リソースを読み込む権限


## Author




