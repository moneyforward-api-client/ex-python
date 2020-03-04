# mfexapiclient.ExReportUnitApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_ex_report_unit_ex_transactions**](ExReportUnitApi.md#find_ex_report_unit_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_report_units/{ex_report_unit_id}/ex_transactions | 経費集計に含まれる経費明細リストを返す
[**find_office_ex_report_unit**](ExReportUnitApi.md#find_office_ex_report_unit) | **GET** /api/external/v1/offices/{office_id}/ex_report_units/{id} | 集計を返す
[**find_office_ex_report_unit_journal**](ExReportUnitApi.md#find_office_ex_report_unit_journal) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_unit_id}/ex_journal | 集計に対応する仕訳を返す
[**find_office_ex_report_units**](ExReportUnitApi.md#find_office_ex_report_units) | **GET** /api/external/v1/offices/{office_id}/ex_report_units | 集計のリストを返す


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
    api_instance = mfexapiclient.ExReportUnitApi(api_client)
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
        print("Exception when calling ExReportUnitApi->find_ex_report_unit_ex_transactions: %s\n" % e)
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

# **find_office_ex_report_unit**
> ExReportUnit find_office_ex_report_unit(office_id, id)

集計を返す

集計を返す

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
    api_instance = mfexapiclient.ExReportUnitApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id

    try:
        # 集計を返す
        api_response = api_instance.find_office_ex_report_unit(office_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExReportUnitApi->find_office_ex_report_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |

### Return type

[**ExReportUnit**](ExReportUnit.md)

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

# **find_office_ex_report_unit_journal**
> ExJournal find_office_ex_report_unit_journal(office_id, ex_report_unit_id)

集計に対応する仕訳を返す

集計に対応する仕訳を返す

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
    api_instance = mfexapiclient.ExReportUnitApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    ex_report_unit_id = 'ex_report_unit_id_example' # str | 集計id

    try:
        # 集計に対応する仕訳を返す
        api_response = api_instance.find_office_ex_report_unit_journal(office_id, ex_report_unit_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExReportUnitApi->find_office_ex_report_unit_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **ex_report_unit_id** | **str**| 集計id |

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

# **find_office_ex_report_units**
> object find_office_ex_report_units(office_id, page=page)

集計のリストを返す

集計のリストを返す

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
    api_instance = mfexapiclient.ExReportUnitApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    page = 56 # int | ページ番号 (optional)

    try:
        # 集計のリストを返す
        api_response = api_instance.find_office_ex_report_units(office_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExReportUnitApi->find_office_ex_report_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **page** | **int**| ページ番号 | [optional]

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

