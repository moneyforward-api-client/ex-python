# moneyforward_ex.ExJournalApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_office_ex_journals_by_ex_reports**](ExJournalApi.md#find_office_ex_journals_by_ex_reports) | **GET** /api/external/v1/offices/{office_id}/ex_journals_by_ex_reports | 事業所全体の申請に紐づく仕訳リストを返す
[**find_office_ex_journals_by_ex_transactions**](ExJournalApi.md#find_office_ex_journals_by_ex_transactions) | **GET** /api/external/v1/offices/{office_id}/ex_journals_by_ex_transactions | 事業所全体の明細に紐づく仕訳リストを返す
[**find_office_ex_report_journal**](ExJournalApi.md#find_office_ex_report_journal) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_id}/ex_journal | 申請に対応する仕訳を返す
[**find_office_ex_report_unit_journal**](ExJournalApi.md#find_office_ex_report_unit_journal) | **GET** /api/external/v1/offices/{office_id}/ex_reports/{ex_report_unit_id}/ex_journal | 集計に対応する仕訳を返す
[**find_office_ex_transaction_journal**](ExJournalApi.md#find_office_ex_transaction_journal) | **GET** /api/external/v1/offices/{office_id}/ex_transactions/{ex_transaction_id}/ex_journal | 経費明細に対応する仕訳を返す


# **find_office_ex_journals_by_ex_reports**
> object find_office_ex_journals_by_ex_reports(office_id, page=page, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)

事業所全体の申請に紐づく仕訳リストを返す

事業所全体の申請に紐づく仕訳リストを返す

### Example

* OAuth Authentication (mf_expense_oauth):
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
    api_instance = moneyforward_ex.ExJournalApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
page = 56 # int | ページ番号 (optional)
query_object_recognized_at_from = '2013-10-20' # date | 仕訳の計上日について指定日以降でフィルタ (recognized_at_to との期間は最大で 3 ヶ月) ex.`2019-09-30` (optional)
query_object_recognized_at_to = '2013-10-20' # date | 仕訳の計上日について指定日以前でフィルタ (recognized_at_from との期間は最大で 3 ヶ月) ex.`2019-09-30` (optional)

    try:
        # 事業所全体の申請に紐づく仕訳リストを返す
        api_response = api_instance.find_office_ex_journals_by_ex_reports(office_id, page=page, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExJournalApi->find_office_ex_journals_by_ex_reports: %s\n" % e)
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

# **find_office_ex_journals_by_ex_transactions**
> object find_office_ex_journals_by_ex_transactions(office_id, page=page, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)

事業所全体の明細に紐づく仕訳リストを返す

事業所全体の明細に紐づく仕訳リストを返す

### Example

* OAuth Authentication (mf_expense_oauth):
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
    api_instance = moneyforward_ex.ExJournalApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
page = 56 # int | ページ番号 (optional)
query_object_recognized_at_from = '2013-10-20' # date | 仕訳の計上日について指定日以降でフィルタ (recognized_at_to との期間は最大で 3 ヶ月) ex.`2019-09-30` (optional)
query_object_recognized_at_to = '2013-10-20' # date | 仕訳の計上日について指定日以前でフィルタ (recognized_at_from との期間は最大で 3 ヶ月) ex.`2019-09-30` (optional)

    try:
        # 事業所全体の明細に紐づく仕訳リストを返す
        api_response = api_instance.find_office_ex_journals_by_ex_transactions(office_id, page=page, query_object_recognized_at_from=query_object_recognized_at_from, query_object_recognized_at_to=query_object_recognized_at_to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExJournalApi->find_office_ex_journals_by_ex_transactions: %s\n" % e)
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

# **find_office_ex_report_journal**
> ExJournal find_office_ex_report_journal(office_id, ex_report_id)

申請に対応する仕訳を返す

申請に対応する仕訳を返す

### Example

* OAuth Authentication (mf_expense_oauth):
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
    api_instance = moneyforward_ex.ExJournalApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
ex_report_id = 'ex_report_id_example' # str | 申請id

    try:
        # 申請に対応する仕訳を返す
        api_response = api_instance.find_office_ex_report_journal(office_id, ex_report_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExJournalApi->find_office_ex_report_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **ex_report_id** | **str**| 申請id |

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

# **find_office_ex_report_unit_journal**
> ExJournal find_office_ex_report_unit_journal(office_id, ex_report_unit_id)

集計に対応する仕訳を返す

集計に対応する仕訳を返す

### Example

* OAuth Authentication (mf_expense_oauth):
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
    api_instance = moneyforward_ex.ExJournalApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
ex_report_unit_id = 'ex_report_unit_id_example' # str | 集計id

    try:
        # 集計に対応する仕訳を返す
        api_response = api_instance.find_office_ex_report_unit_journal(office_id, ex_report_unit_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExJournalApi->find_office_ex_report_unit_journal: %s\n" % e)
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

# **find_office_ex_transaction_journal**
> ExJournal find_office_ex_transaction_journal(office_id, ex_transaction_id)

経費明細に対応する仕訳を返す

経費明細に対応する仕訳を返す

### Example

* OAuth Authentication (mf_expense_oauth):
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
    api_instance = moneyforward_ex.ExJournalApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
ex_transaction_id = 'ex_transaction_id_example' # str | 経費明細id

    try:
        # 経費明細に対応する仕訳を返す
        api_response = api_instance.find_office_ex_transaction_journal(office_id, ex_transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExJournalApi->find_office_ex_transaction_journal: %s\n" % e)
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

