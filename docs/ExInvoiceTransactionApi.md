# mfexapiclient.ExInvoiceTransactionApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_office_ex_invoice_transactions**](ExInvoiceTransactionApi.md#find_office_ex_invoice_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_invoice_transactions | 事業所全体の支払明細リストを返す


# **find_office_ex_invoice_transactions**
> object find_office_ex_invoice_transactions(office_id, page=page, query_object_ex_destination_id=query_object_ex_destination_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_book_date_from=query_object_book_date_from, query_object_book_date_to=query_object_book_date_to, query_object_updated_at_from=query_object_updated_at_from, query_object_updated_at_to=query_object_updated_at_to, query_object_approval_status=query_object_approval_status, query_object_order_by_option=query_object_order_by_option)

事業所全体の支払明細リストを返す

事業所全体の支払明細リストを返す

### Example

* OAuth Authentication (mf_expense_oauth):
```python
from __future__ import print_function
import time
import mfexapiclient
from mfexapiclient.rest import ApiException
from pprint import pprint
configuration = mfexapiclient.Configuration()
# Configure OAuth2 access token for authorization: mf_expense_oauth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://expense.moneyforward.com
configuration.host = "https://expense.moneyforward.com"

# Enter a context with an instance of the API client
with mfexapiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mfexapiclient.ExInvoiceTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    page = 56 # int | ページ番号 (optional)
    query_object_ex_destination_id = 'query_object_ex_destination_id_example' # str | 支払先マスタidでフィルタ (optional)
    query_object_number = 56 # int | 支払明細番号でフィルタ (optional)
    query_object_number_from = 56 # int | 指定番号以上の支払明細番号でフィルタ (optional)
    query_object_number_to = 56 # int | 指定番号以下の支払明細番号でフィルタ (optional)
    query_object_dept_id = 'query_object_dept_id_example' # str | 部門idでフィルタ (optional)
    query_object_project_code_id = 'query_object_project_code_id_example' # str | プロジェクトidでフィルタ (optional)
    query_object_ex_item_id = 'query_object_ex_item_id_example' # str | 経費科目idでフィルタ (optional)
    query_object_office_member_id = 'query_object_office_member_id_example' # str | メンバーidでフィルタ (optional)
    query_object_approved_at_from = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以降でフィルタ ex.`2018-09-30 00:00:00 +0900` (optional)
    query_object_approved_at_to = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以前でフィルタ ex.`2018-09-30 23:59:59 +0900` (optional)
    query_object_book_date_from = '2013-10-20' # date | 費用計上日について指定日付以降でフィルタ ex.`2018-09-30` (optional)
    query_object_book_date_to = '2013-10-20' # date | 費用計上日について指定日付以前でフィルタ ex.`2018-09-30` (optional)
    query_object_updated_at_from = '2013-10-20' # date | 支払明細の更新日を指定日付以降でフィルタ ex.`2018-09-30` (optional)
    query_object_updated_at_to = '2013-10-20' # date | 支払明細の更新日を指定日付以前でフィルタ ex.`2018-09-30` (optional)
    query_object_approval_status = 56 # int | 申請ステータスで絞込む。（0:全て, 1:未申請, 2:申請済, 3:承認済） (optional)
    query_object_order_by_option = 56 # int | 条件により並び替えて取得する（0:支払明細id昇順, 1:支払明細id降順, 2:支払明細更新日昇順, 3:支払明細更新日降順, 4:申請の承認時刻昇順, 5:申請の承認時刻降順） (optional)

    try:
        # 事業所全体の支払明細リストを返す
        api_response = api_instance.find_office_ex_invoice_transactions(office_id, page=page, query_object_ex_destination_id=query_object_ex_destination_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_book_date_from=query_object_book_date_from, query_object_book_date_to=query_object_book_date_to, query_object_updated_at_from=query_object_updated_at_from, query_object_updated_at_to=query_object_updated_at_to, query_object_approval_status=query_object_approval_status, query_object_order_by_option=query_object_order_by_option)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExInvoiceTransactionApi->find_office_ex_invoice_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **page** | **int**| ページ番号 | [optional]
 **query_object_ex_destination_id** | **str**| 支払先マスタidでフィルタ | [optional]
 **query_object_number** | **int**| 支払明細番号でフィルタ | [optional]
 **query_object_number_from** | **int**| 指定番号以上の支払明細番号でフィルタ | [optional]
 **query_object_number_to** | **int**| 指定番号以下の支払明細番号でフィルタ | [optional]
 **query_object_dept_id** | **str**| 部門idでフィルタ | [optional]
 **query_object_project_code_id** | **str**| プロジェクトidでフィルタ | [optional]
 **query_object_ex_item_id** | **str**| 経費科目idでフィルタ | [optional]
 **query_object_office_member_id** | **str**| メンバーidでフィルタ | [optional]
 **query_object_approved_at_from** | [**datetime**](.md)| 申請の承認時刻について指定時刻以降でフィルタ ex.&#x60;2018-09-30 00:00:00 +0900&#x60; | [optional]
 **query_object_approved_at_to** | [**datetime**](.md)| 申請の承認時刻について指定時刻以前でフィルタ ex.&#x60;2018-09-30 23:59:59 +0900&#x60; | [optional]
 **query_object_book_date_from** | [**date**](.md)| 費用計上日について指定日付以降でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_book_date_to** | [**date**](.md)| 費用計上日について指定日付以前でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_updated_at_from** | [**date**](.md)| 支払明細の更新日を指定日付以降でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_updated_at_to** | [**date**](.md)| 支払明細の更新日を指定日付以前でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_approval_status** | **int**| 申請ステータスで絞込む。（0:全て, 1:未申請, 2:申請済, 3:承認済） | [optional]
 **query_object_order_by_option** | **int**| 条件により並び替えて取得する（0:支払明細id昇順, 1:支払明細id降順, 2:支払明細更新日昇順, 3:支払明細更新日降順, 4:申請の承認時刻昇順, 5:申請の承認時刻降順） | [optional]

### Return type

**object**

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

