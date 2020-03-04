# mfexapiclient.ExTransactionApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ex_transaction**](ExTransactionApi.md#create_ex_transaction) | **POST** /api/external/v1/offices/{office_id}/me/ex_transactions | 自分の経費明細を追加する
[**create_office_ex_transaction**](ExTransactionApi.md#create_office_ex_transaction) | **POST** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/ex_transactions | 経費明細を追加する
[**destroy_ex_transaction**](ExTransactionApi.md#destroy_ex_transaction) | **DELETE** /api/external/v1/offices/{office_id}/me/ex_transactions/{id} | 自分の経費明細を削除する
[**destroy_office_ex_transaction**](ExTransactionApi.md#destroy_office_ex_transaction) | **DELETE** /api/external/v1/offices/{office_id}/ex_transactions/{id} | 事業所全体の指定idの経費明細を削除する
[**find_ex_report_ex_transactions**](ExTransactionApi.md#find_ex_report_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_id}/ex_transactions | 経費申請に含まれる経費明細リストを返す
[**find_ex_report_unit_ex_transactions**](ExTransactionApi.md#find_ex_report_unit_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_report_units/{ex_report_unit_id}/ex_transactions | 経費集計に含まれる経費明細リストを返す
[**find_ex_transaction**](ExTransactionApi.md#find_ex_transaction) | **GET** /api/external/v1/offices/{office_id}/me/ex_transactions/{id} | 自分の経費明細を返す
[**find_ex_transactions**](ExTransactionApi.md#find_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/me/ex_transactions | 自分の経費明細リストを返す
[**find_office_ex_journals_by_ex_transactions**](ExTransactionApi.md#find_office_ex_journals_by_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_journals_by_ex_transactions | 事業所全体の明細に紐づく仕訳リストを返す
[**find_office_ex_transaction**](ExTransactionApi.md#find_office_ex_transaction) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{id} | 事業所全体の指定idの経費明細を返す
[**find_office_ex_transaction_journal**](ExTransactionApi.md#find_office_ex_transaction_journal) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{ex_transaction_id}/ex_journal | 経費明細に対応する仕訳を返す
[**find_office_ex_transaction_mf_file**](ExTransactionApi.md#find_office_ex_transaction_mf_file) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{ex_transaction_id}/mf_file | 経費明細に紐づく添付ファイルを返す
[**find_office_ex_transaction_mf_file_me**](ExTransactionApi.md#find_office_ex_transaction_mf_file_me) | **GET** /api/external/v1/offices/{office_id}/me/ex_transactions/{ex_transaction_id}/mf_file | 経費明細に紐づく添付ファイルを返す
[**find_office_ex_transactions**](ExTransactionApi.md#find_office_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_transactions | 事業所全体の経費明細リストを返す
[**update_ex_transaction**](ExTransactionApi.md#update_ex_transaction) | **PUT** /api/external/v1/offices/{office_id}/me/ex_transactions/{id} | 自分の経費明細を更新する
[**update_office_ex_transaction**](ExTransactionApi.md#update_office_ex_transaction) | **PUT** /api/external/v1/offices/{office_id}/ex_transactions/{id} | 事業所全体の指定idの経費明細を更新する
[**upload_member_receipt**](ExTransactionApi.md#upload_member_receipt) | **POST** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/upload_receipt | 領収書をアップロードして経費登録する
[**upload_receipt**](ExTransactionApi.md#upload_receipt) | **POST** /api/external/v1/offices/{office_id}/me/upload_receipt | 自分の領収書をアップロードして経費登録する


# **create_ex_transaction**
> ExTransaction create_ex_transaction(office_id, unknown_base_type)

自分の経費明細を追加する

自分の経費明細を追加する

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 経費明細のパラメータ

    try:
        # 自分の経費明細を追加する
        api_response = api_instance.create_ex_transaction(office_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->create_ex_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| 経費明細のパラメータ |

### Return type

[**ExTransaction**](ExTransaction.md)

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |
**422** | バリデーションエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_office_ex_transaction**
> ExTransaction create_office_ex_transaction(office_id, office_member_id, unknown_base_type)

経費明細を追加する

経費明細を追加する

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    office_member_id = 'office_member_id_example' # str | メンバーid
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 経費明細のパラメータ

    try:
        # 経費明細を追加する
        api_response = api_instance.create_office_ex_transaction(office_id, office_member_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->create_office_ex_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **office_member_id** | **str**| メンバーid |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| 経費明細のパラメータ |

### Return type

[**ExTransaction**](ExTransaction.md)

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |
**422** | バリデーションエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_ex_transaction**
> destroy_ex_transaction(office_id, id)

自分の経費明細を削除する

自分の経費明細を削除する

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id

    try:
        # 自分の経費明細を削除する
        api_instance.destroy_ex_transaction(office_id, id)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->destroy_ex_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |

### Return type

void (empty response body)

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |
**422** | バリデーションエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_office_ex_transaction**
> destroy_office_ex_transaction(office_id, id)

事業所全体の指定idの経費明細を削除する

事業所全体の指定idの経費明細を削除する

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id

    try:
        # 事業所全体の指定idの経費明細を削除する
        api_instance.destroy_office_ex_transaction(office_id, id)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->destroy_office_ex_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |

### Return type

void (empty response body)

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |
**422** | バリデーションエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_ex_report_ex_transactions**
> object find_ex_report_ex_transactions(office_id, ex_report_id, page=page, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_value_min=query_object_value_min, query_object_value_max=query_object_value_max, query_object_is_exported=query_object_is_exported, query_object_is_reported=query_object_is_reported, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)

経費申請に含まれる経費明細リストを返す

経費申請に含まれる経費明細リストを返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    ex_report_id = 'ex_report_id_example' # str | 申請id
    page = 56 # int | ページ番号 (optional)
    query_object_dept_id = 'query_object_dept_id_example' # str | 部門idでフィルタ (optional)
    query_object_project_code_id = 'query_object_project_code_id_example' # str | プロジェクトidでフィルタ (optional)
    query_object_ex_item_id = 'query_object_ex_item_id_example' # str | 経費科目idでフィルタ (optional)
    query_object_office_member_id = 'query_object_office_member_id_example' # str | メンバーidでフィルタ (optional)
    query_object_number = 56 # int | 経費明細番号でフィルタ (optional)
    query_object_number_from = 56 # int | 指定番号以上の経費明細番号でフィルタ (optional)
    query_object_number_to = 56 # int | 指定番号以下の経費明細番号でフィルタ (optional)
    query_object_value_min = 3.4 # float | 金額下限でフィルタ (optional)
    query_object_value_max = 3.4 # float | 金額上限でフィルタ (optional)
    query_object_is_exported = True # bool | 仕訳出力済みかどうかでフィルタ (optional)
    query_object_is_reported = True # bool | 経費申請に含まれるかどうかでフィルタ (optional)
    query_object_approved_at_from = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以降でフィルタ ex.`2018-09-30 00:00:00 +0900` (optional)
    query_object_approved_at_to = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以前でフィルタ ex.`2018-09-30 23:59:59 +0900` (optional)
    query_object_recognized_at_from = '2013-10-20' # date | 日付に指定日付以降でフィルタ ex.`2018-09-30` (optional)
    query_object_recognized_at_to = '2013-10-20' # date | 日付に指定日付以前でフィルタ ex.`2018-09-30` (optional)

    try:
        # 経費申請に含まれる経費明細リストを返す
        api_response = api_instance.find_ex_report_ex_transactions(office_id, ex_report_id, page=page, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_value_min=query_object_value_min, query_object_value_max=query_object_value_max, query_object_is_exported=query_object_is_exported, query_object_is_reported=query_object_is_reported, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_ex_report_ex_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **ex_report_id** | **str**| 申請id |
 **page** | **int**| ページ番号 | [optional]
 **query_object_dept_id** | **str**| 部門idでフィルタ | [optional]
 **query_object_project_code_id** | **str**| プロジェクトidでフィルタ | [optional]
 **query_object_ex_item_id** | **str**| 経費科目idでフィルタ | [optional]
 **query_object_office_member_id** | **str**| メンバーidでフィルタ | [optional]
 **query_object_number** | **int**| 経費明細番号でフィルタ | [optional]
 **query_object_number_from** | **int**| 指定番号以上の経費明細番号でフィルタ | [optional]
 **query_object_number_to** | **int**| 指定番号以下の経費明細番号でフィルタ | [optional]
 **query_object_value_min** | [**float**](.md)| 金額下限でフィルタ | [optional]
 **query_object_value_max** | [**float**](.md)| 金額上限でフィルタ | [optional]
 **query_object_is_exported** | **bool**| 仕訳出力済みかどうかでフィルタ | [optional]
 **query_object_is_reported** | **bool**| 経費申請に含まれるかどうかでフィルタ | [optional]
 **query_object_approved_at_from** | [**datetime**](.md)| 申請の承認時刻について指定時刻以降でフィルタ ex.&#x60;2018-09-30 00:00:00 +0900&#x60; | [optional]
 **query_object_approved_at_to** | [**datetime**](.md)| 申請の承認時刻について指定時刻以前でフィルタ ex.&#x60;2018-09-30 23:59:59 +0900&#x60; | [optional]
 **query_object_recognized_at_from** | [**date**](.md)| 日付に指定日付以降でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_recognized_at_to** | [**date**](.md)| 日付に指定日付以前でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]

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

# **find_ex_report_unit_ex_transactions**
> object find_ex_report_unit_ex_transactions(office_id, ex_report_unit_id, page=page, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_value_min=query_object_value_min, query_object_value_max=query_object_value_max, query_object_is_exported=query_object_is_exported, query_object_is_reported=query_object_is_reported, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)

経費集計に含まれる経費明細リストを返す

経費集計に含まれる経費明細リストを返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    ex_report_unit_id = 'ex_report_unit_id_example' # str | 集計id
    page = 56 # int | ページ番号 (optional)
    query_object_dept_id = 'query_object_dept_id_example' # str | 部門idでフィルタ (optional)
    query_object_project_code_id = 'query_object_project_code_id_example' # str | プロジェクトidでフィルタ (optional)
    query_object_ex_item_id = 'query_object_ex_item_id_example' # str | 経費科目idでフィルタ (optional)
    query_object_office_member_id = 'query_object_office_member_id_example' # str | メンバーidでフィルタ (optional)
    query_object_number = 56 # int | 経費明細番号でフィルタ (optional)
    query_object_number_from = 56 # int | 指定番号以上の経費明細番号でフィルタ (optional)
    query_object_number_to = 56 # int | 指定番号以下の経費明細番号でフィルタ (optional)
    query_object_value_min = 3.4 # float | 金額下限でフィルタ (optional)
    query_object_value_max = 3.4 # float | 金額上限でフィルタ (optional)
    query_object_is_exported = True # bool | 仕訳出力済みかどうかでフィルタ (optional)
    query_object_is_reported = True # bool | 経費申請に含まれるかどうかでフィルタ (optional)
    query_object_approved_at_from = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以降でフィルタ ex.`2018-09-30 00:00:00 +0900` (optional)
    query_object_approved_at_to = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以前でフィルタ ex.`2018-09-30 23:59:59 +0900` (optional)
    query_object_recognized_at_from = '2013-10-20' # date | 日付に指定日付以降でフィルタ ex.`2018-09-30` (optional)
    query_object_recognized_at_to = '2013-10-20' # date | 日付に指定日付以前でフィルタ ex.`2018-09-30` (optional)

    try:
        # 経費集計に含まれる経費明細リストを返す
        api_response = api_instance.find_ex_report_unit_ex_transactions(office_id, ex_report_unit_id, page=page, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_value_min=query_object_value_min, query_object_value_max=query_object_value_max, query_object_is_exported=query_object_is_exported, query_object_is_reported=query_object_is_reported, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_ex_report_unit_ex_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **ex_report_unit_id** | **str**| 集計id |
 **page** | **int**| ページ番号 | [optional]
 **query_object_dept_id** | **str**| 部門idでフィルタ | [optional]
 **query_object_project_code_id** | **str**| プロジェクトidでフィルタ | [optional]
 **query_object_ex_item_id** | **str**| 経費科目idでフィルタ | [optional]
 **query_object_office_member_id** | **str**| メンバーidでフィルタ | [optional]
 **query_object_number** | **int**| 経費明細番号でフィルタ | [optional]
 **query_object_number_from** | **int**| 指定番号以上の経費明細番号でフィルタ | [optional]
 **query_object_number_to** | **int**| 指定番号以下の経費明細番号でフィルタ | [optional]
 **query_object_value_min** | [**float**](.md)| 金額下限でフィルタ | [optional]
 **query_object_value_max** | [**float**](.md)| 金額上限でフィルタ | [optional]
 **query_object_is_exported** | **bool**| 仕訳出力済みかどうかでフィルタ | [optional]
 **query_object_is_reported** | **bool**| 経費申請に含まれるかどうかでフィルタ | [optional]
 **query_object_approved_at_from** | [**datetime**](.md)| 申請の承認時刻について指定時刻以降でフィルタ ex.&#x60;2018-09-30 00:00:00 +0900&#x60; | [optional]
 **query_object_approved_at_to** | [**datetime**](.md)| 申請の承認時刻について指定時刻以前でフィルタ ex.&#x60;2018-09-30 23:59:59 +0900&#x60; | [optional]
 **query_object_recognized_at_from** | [**date**](.md)| 日付に指定日付以降でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_recognized_at_to** | [**date**](.md)| 日付に指定日付以前でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]

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

# **find_ex_transaction**
> ExTransaction find_ex_transaction(office_id, id)

自分の経費明細を返す

自分の経費明細を返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id

    try:
        # 自分の経費明細を返す
        api_response = api_instance.find_ex_transaction(office_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_ex_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |

### Return type

[**ExTransaction**](ExTransaction.md)

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

# **find_ex_transactions**
> object find_ex_transactions(office_id, page=page, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_value_min=query_object_value_min, query_object_value_max=query_object_value_max, query_object_is_exported=query_object_is_exported, query_object_is_reported=query_object_is_reported, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to, query_object_is_recognized_at_blank=query_object_is_recognized_at_blank)

自分の経費明細リストを返す

自分の経費明細リストを返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    page = 56 # int | ページ番号 (optional)
    query_object_dept_id = 'query_object_dept_id_example' # str | 部門idでフィルタ (optional)
    query_object_project_code_id = 'query_object_project_code_id_example' # str | プロジェクトidでフィルタ (optional)
    query_object_ex_item_id = 'query_object_ex_item_id_example' # str | 経費科目idでフィルタ (optional)
    query_object_office_member_id = 'query_object_office_member_id_example' # str | メンバーidでフィルタ (optional)
    query_object_number = 56 # int | 経費明細番号でフィルタ (optional)
    query_object_number_from = 56 # int | 指定番号以上の経費明細番号でフィルタ (optional)
    query_object_number_to = 56 # int | 指定番号以下の経費明細番号でフィルタ (optional)
    query_object_value_min = 3.4 # float | 金額下限でフィルタ (optional)
    query_object_value_max = 3.4 # float | 金額上限でフィルタ (optional)
    query_object_is_exported = True # bool | 仕訳出力済みかどうかでフィルタ (optional)
    query_object_is_reported = True # bool | 経費申請に含まれるかどうかでフィルタ (optional)
    query_object_approved_at_from = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以降でフィルタ ex.`2018-09-30 00:00:00 +0900` (optional)
    query_object_approved_at_to = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以前でフィルタ ex.`2018-09-30 23:59:59 +0900` (optional)
    query_object_recognized_at_from = '2013-10-20' # date | 日付に指定日付以降でフィルタ ex.`2018-09-30` (optional)
    query_object_recognized_at_to = '2013-10-20' # date | 日付に指定日付以前でフィルタ ex.`2018-09-30` (optional)
    query_object_is_recognized_at_blank = True # bool | 日付が空でフィルタ (optional)

    try:
        # 自分の経費明細リストを返す
        api_response = api_instance.find_ex_transactions(office_id, page=page, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_value_min=query_object_value_min, query_object_value_max=query_object_value_max, query_object_is_exported=query_object_is_exported, query_object_is_reported=query_object_is_reported, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to, query_object_is_recognized_at_blank=query_object_is_recognized_at_blank)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_ex_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **page** | **int**| ページ番号 | [optional]
 **query_object_dept_id** | **str**| 部門idでフィルタ | [optional]
 **query_object_project_code_id** | **str**| プロジェクトidでフィルタ | [optional]
 **query_object_ex_item_id** | **str**| 経費科目idでフィルタ | [optional]
 **query_object_office_member_id** | **str**| メンバーidでフィルタ | [optional]
 **query_object_number** | **int**| 経費明細番号でフィルタ | [optional]
 **query_object_number_from** | **int**| 指定番号以上の経費明細番号でフィルタ | [optional]
 **query_object_number_to** | **int**| 指定番号以下の経費明細番号でフィルタ | [optional]
 **query_object_value_min** | [**float**](.md)| 金額下限でフィルタ | [optional]
 **query_object_value_max** | [**float**](.md)| 金額上限でフィルタ | [optional]
 **query_object_is_exported** | **bool**| 仕訳出力済みかどうかでフィルタ | [optional]
 **query_object_is_reported** | **bool**| 経費申請に含まれるかどうかでフィルタ | [optional]
 **query_object_approved_at_from** | [**datetime**](.md)| 申請の承認時刻について指定時刻以降でフィルタ ex.&#x60;2018-09-30 00:00:00 +0900&#x60; | [optional]
 **query_object_approved_at_to** | [**datetime**](.md)| 申請の承認時刻について指定時刻以前でフィルタ ex.&#x60;2018-09-30 23:59:59 +0900&#x60; | [optional]
 **query_object_recognized_at_from** | [**date**](.md)| 日付に指定日付以降でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_recognized_at_to** | [**date**](.md)| 日付に指定日付以前でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_is_recognized_at_blank** | **bool**| 日付が空でフィルタ | [optional]

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

# **find_office_ex_journals_by_ex_transactions**
> object find_office_ex_journals_by_ex_transactions(office_id, page=page, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)

事業所全体の明細に紐づく仕訳リストを返す

事業所全体の明細に紐づく仕訳リストを返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    page = 56 # int | ページ番号 (optional)
    query_object_recognized_at_from = '2013-10-20' # date | 仕訳の計上日について指定日以降でフィルタ (recognized_at_to との期間は最大で 3 ヶ月) ex.`2019-09-30` (optional)
    query_object_recognized_at_to = '2013-10-20' # date | 仕訳の計上日について指定日以前でフィルタ (recognized_at_from との期間は最大で 3 ヶ月) ex.`2019-09-30` (optional)

    try:
        # 事業所全体の明細に紐づく仕訳リストを返す
        api_response = api_instance.find_office_ex_journals_by_ex_transactions(office_id, page=page, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_office_ex_journals_by_ex_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **page** | **int**| ページ番号 | [optional]
 **query_object_recognized_at_from** | [**date**](.md)| 仕訳の計上日について指定日以降でフィルタ (recognized_at_to との期間は最大で 3 ヶ月) ex.&#x60;2019-09-30&#x60; | [optional]
 **query_object_recognized_at_to** | [**date**](.md)| 仕訳の計上日について指定日以前でフィルタ (recognized_at_from との期間は最大で 3 ヶ月) ex.&#x60;2019-09-30&#x60; | [optional]

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

# **find_office_ex_transaction**
> ExTransaction find_office_ex_transaction(office_id, id)

事業所全体の指定idの経費明細を返す

事業所全体の指定idの経費明細を返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id

    try:
        # 事業所全体の指定idの経費明細を返す
        api_response = api_instance.find_office_ex_transaction(office_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_office_ex_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |

### Return type

[**ExTransaction**](ExTransaction.md)

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

# **find_office_ex_transaction_journal**
> ExJournal find_office_ex_transaction_journal(office_id, ex_transaction_id)

経費明細に対応する仕訳を返す

経費明細に対応する仕訳を返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    ex_transaction_id = 'ex_transaction_id_example' # str | 経費明細id

    try:
        # 経費明細に対応する仕訳を返す
        api_response = api_instance.find_office_ex_transaction_journal(office_id, ex_transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_office_ex_transaction_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **ex_transaction_id** | **str**| 経費明細id |

### Return type

[**ExJournal**](ExJournal.md)

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

# **find_office_ex_transaction_mf_file**
> file find_office_ex_transaction_mf_file(office_id, ex_transaction_id)

経費明細に紐づく添付ファイルを返す

経費明細に紐づく添付ファイルを返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    ex_transaction_id = 'ex_transaction_id_example' # str | 経費明細id

    try:
        # 経費明細に紐づく添付ファイルを返す
        api_response = api_instance.find_office_ex_transaction_mf_file(office_id, ex_transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_office_ex_transaction_mf_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **ex_transaction_id** | **str**| 経費明細id |

### Return type

**file**

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

# **find_office_ex_transaction_mf_file_me**
> file find_office_ex_transaction_mf_file_me(office_id, ex_transaction_id)

経費明細に紐づく添付ファイルを返す

経費明細に紐づく添付ファイルを返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    ex_transaction_id = 'ex_transaction_id_example' # str | 経費明細id

    try:
        # 経費明細に紐づく添付ファイルを返す
        api_response = api_instance.find_office_ex_transaction_mf_file_me(office_id, ex_transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_office_ex_transaction_mf_file_me: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **ex_transaction_id** | **str**| 経費明細id |

### Return type

**file**

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

# **find_office_ex_transactions**
> object find_office_ex_transactions(office_id, page=page, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_value_min=query_object_value_min, query_object_value_max=query_object_value_max, query_object_is_exported=query_object_is_exported, query_object_is_reported=query_object_is_reported, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to, query_object_is_recognized_at_blank=query_object_is_recognized_at_blank)

事業所全体の経費明細リストを返す

事業所全体の経費明細リストを返す

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    page = 56 # int | ページ番号 (optional)
    query_object_dept_id = 'query_object_dept_id_example' # str | 部門idでフィルタ (optional)
    query_object_project_code_id = 'query_object_project_code_id_example' # str | プロジェクトidでフィルタ (optional)
    query_object_ex_item_id = 'query_object_ex_item_id_example' # str | 経費科目idでフィルタ (optional)
    query_object_office_member_id = 'query_object_office_member_id_example' # str | メンバーidでフィルタ (optional)
    query_object_number = 56 # int | 経費明細番号でフィルタ (optional)
    query_object_number_from = 56 # int | 指定番号以上の経費明細番号でフィルタ (optional)
    query_object_number_to = 56 # int | 指定番号以下の経費明細番号でフィルタ (optional)
    query_object_value_min = 3.4 # float | 金額下限でフィルタ (optional)
    query_object_value_max = 3.4 # float | 金額上限でフィルタ (optional)
    query_object_is_exported = True # bool | 仕訳出力済みかどうかでフィルタ (optional)
    query_object_is_reported = True # bool | 経費申請に含まれるかどうかでフィルタ (optional)
    query_object_approved_at_from = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以降でフィルタ ex.`2018-09-30 00:00:00 +0900` (optional)
    query_object_approved_at_to = '2013-10-20T19:20:30+01:00' # datetime | 申請の承認時刻について指定時刻以前でフィルタ ex.`2018-09-30 23:59:59 +0900` (optional)
    query_object_recognized_at_from = '2013-10-20' # date | 日付に指定日付以降でフィルタ ex.`2018-09-30` (optional)
    query_object_recognized_at_to = '2013-10-20' # date | 日付に指定日付以前でフィルタ ex.`2018-09-30` (optional)
    query_object_is_recognized_at_blank = True # bool | 日付が空でフィルタ (optional)

    try:
        # 事業所全体の経費明細リストを返す
        api_response = api_instance.find_office_ex_transactions(office_id, page=page, query_object_dept_id=query_object_dept_id, query_object_project_code_id=query_object_project_code_id, query_object_ex_item_id=query_object_ex_item_id, query_object_office_member_id=query_object_office_member_id, query_object_number=query_object_number, query_object_number_from=query_object_number_from, query_object_number_to=query_object_number_to, query_object_value_min=query_object_value_min, query_object_value_max=query_object_value_max, query_object_is_exported=query_object_is_exported, query_object_is_reported=query_object_is_reported, query_object_approved_at_from=query_object_approved_at_from, query_object_approved_at_to=query_object_approved_at_to, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to, query_object_is_recognized_at_blank=query_object_is_recognized_at_blank)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->find_office_ex_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **page** | **int**| ページ番号 | [optional]
 **query_object_dept_id** | **str**| 部門idでフィルタ | [optional]
 **query_object_project_code_id** | **str**| プロジェクトidでフィルタ | [optional]
 **query_object_ex_item_id** | **str**| 経費科目idでフィルタ | [optional]
 **query_object_office_member_id** | **str**| メンバーidでフィルタ | [optional]
 **query_object_number** | **int**| 経費明細番号でフィルタ | [optional]
 **query_object_number_from** | **int**| 指定番号以上の経費明細番号でフィルタ | [optional]
 **query_object_number_to** | **int**| 指定番号以下の経費明細番号でフィルタ | [optional]
 **query_object_value_min** | [**float**](.md)| 金額下限でフィルタ | [optional]
 **query_object_value_max** | [**float**](.md)| 金額上限でフィルタ | [optional]
 **query_object_is_exported** | **bool**| 仕訳出力済みかどうかでフィルタ | [optional]
 **query_object_is_reported** | **bool**| 経費申請に含まれるかどうかでフィルタ | [optional]
 **query_object_approved_at_from** | [**datetime**](.md)| 申請の承認時刻について指定時刻以降でフィルタ ex.&#x60;2018-09-30 00:00:00 +0900&#x60; | [optional]
 **query_object_approved_at_to** | [**datetime**](.md)| 申請の承認時刻について指定時刻以前でフィルタ ex.&#x60;2018-09-30 23:59:59 +0900&#x60; | [optional]
 **query_object_recognized_at_from** | [**date**](.md)| 日付に指定日付以降でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_recognized_at_to** | [**date**](.md)| 日付に指定日付以前でフィルタ ex.&#x60;2018-09-30&#x60; | [optional]
 **query_object_is_recognized_at_blank** | **bool**| 日付が空でフィルタ | [optional]

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

# **update_ex_transaction**
> ExTransaction update_ex_transaction(office_id, office_member_id, id, unknown_base_type)

自分の経費明細を更新する

自分の経費明細を更新する

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    office_member_id = 'office_member_id_example' # str | メンバーid
    id = 'id_example' # str | id
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 経費明細のパラメータ

    try:
        # 自分の経費明細を更新する
        api_response = api_instance.update_ex_transaction(office_id, office_member_id, id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->update_ex_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **office_member_id** | **str**| メンバーid |
 **id** | **str**| id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| 経費明細のパラメータ |

### Return type

[**ExTransaction**](ExTransaction.md)

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |
**422** | バリデーションエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_office_ex_transaction**
> ExTransaction update_office_ex_transaction(office_id, office_member_id, id, unknown_base_type)

事業所全体の指定idの経費明細を更新する

事業所全体の指定idの経費明細を更新する

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    office_member_id = 'office_member_id_example' # str | メンバーid
    id = 'id_example' # str | id
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 経費明細のパラメータ

    try:
        # 事業所全体の指定idの経費明細を更新する
        api_response = api_instance.update_office_ex_transaction(office_id, office_member_id, id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->update_office_ex_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **office_member_id** | **str**| メンバーid |
 **id** | **str**| id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| 経費明細のパラメータ |

### Return type

[**ExTransaction**](ExTransaction.md)

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |
**422** | バリデーションエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_member_receipt**
> object upload_member_receipt(office_id, office_member_id, receipt_input)

領収書をアップロードして経費登録する

領収書をアップロードして経費登録する

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    office_member_id = 'office_member_id_example' # str | メンバーid
    receipt_input = mfexapiclient.ReceiptInput() # ReceiptInput | 領収書像データ

    try:
        # 領収書をアップロードして経費登録する
        api_response = api_instance.upload_member_receipt(office_id, office_member_id, receipt_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->upload_member_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **office_member_id** | **str**| メンバーid |
 **receipt_input** | [**ReceiptInput**](ReceiptInput.md)| 領収書像データ |

### Return type

**object**

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |
**422** | バリデーションエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_receipt**
> object upload_receipt(office_id, receipt_input)

自分の領収書をアップロードして経費登録する

自分の領収書をアップロードして経費登録する

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
    api_instance = mfexapiclient.ExTransactionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    receipt_input = mfexapiclient.ReceiptInput() # ReceiptInput | 領収書像データ

    try:
        # 自分の領収書をアップロードして経費登録する
        api_response = api_instance.upload_receipt(office_id, receipt_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExTransactionApi->upload_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **receipt_input** | [**ReceiptInput**](ReceiptInput.md)| 領収書像データ |

### Return type

**object**

### Authorization

[mf_expense_oauth](../README.md#mf_expense_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 成功 |  -  |
**401** | 認証エラー |  -  |
**403** | 権限エラー |  -  |
**404** | 未検出エラー |  -  |
**422** | バリデーションエラー |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

