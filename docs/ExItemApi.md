# moneyforward_ex.ExItemApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_ex_item**](ExItemApi.md#find_ex_item) | **GET** /api/external/v1/offices/{office_id}/ex_items/{id} | 経費科目を返す
[**find_ex_items**](ExItemApi.md#find_ex_items) | **GET** /api/external/v1/offices/{office_id}/ex_items | 経費科目一覧を返す


# **find_ex_item**
> ExItem find_ex_item(office_id, id, page=page)

経費科目を返す

経費科目を返す

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
    api_instance = moneyforward_ex.ExItemApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id
page = 56 # int | ページ番号 (optional)

    try:
        # 経費科目を返す
        api_response = api_instance.find_ex_item(office_id, id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExItemApi->find_ex_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **page** | **int**| ページ番号 | [optional]

### Return type

[**ExItem**](ExItem.md)

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

# **find_ex_items**
> object find_ex_items(office_id, page=page)

経費科目一覧を返す

経費科目一覧を返す

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
    api_instance = moneyforward_ex.ExItemApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
page = 56 # int | ページ番号 (optional)

    try:
        # 経費科目一覧を返す
        api_response = api_instance.find_ex_items(office_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExItemApi->find_ex_items: %s\n" % e)
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

