# moneyforward_ex.DeptApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dept**](DeptApi.md#create_dept) | **POST** /api/external/v1/offices/{office_id}/depts | 部門を作成する
[**delete_dept**](DeptApi.md#delete_dept) | **DELETE** /api/external/v1/offices/{office_id}/depts/{id} | 部門を削除する
[**find_dept**](DeptApi.md#find_dept) | **GET** /api/external/v1/offices/{office_id}/depts/{id} | 部門を返す
[**find_depts**](DeptApi.md#find_depts) | **GET** /api/external/v1/offices/{office_id}/depts | 部門一覧を返す
[**update_dept**](DeptApi.md#update_dept) | **PUT** /api/external/v1/offices/{office_id}/depts/{id} | 部門を更新する


# **create_dept**
> Dept create_dept(office_id, unknown_base_type)

部門を作成する

部門を作成する

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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| 部門のパラメータ |

### Return type

[**Dept**](Dept.md)

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

# **delete_dept**
> delete_dept(office_id, id)

部門を削除する

部門を削除する

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
    api_instance = moneyforward_ex.DeptApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id

    try:
        # 部門を削除する
        api_instance.delete_dept(office_id, id)
    except ApiException as e:
        print("Exception when calling DeptApi->delete_dept: %s\n" % e)
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

# **find_dept**
> Dept find_dept(office_id, id, page=page)

部門を返す

部門を返す

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
    api_instance = moneyforward_ex.DeptApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id
page = 56 # int | ページ番号 (optional)

    try:
        # 部門を返す
        api_response = api_instance.find_dept(office_id, id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeptApi->find_dept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **page** | **int**| ページ番号 | [optional]

### Return type

[**Dept**](Dept.md)

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

# **find_depts**
> object find_depts(office_id, page=page, query_object_search_keyword=query_object_search_keyword)

部門一覧を返す

部門一覧を返す

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
    api_instance = moneyforward_ex.DeptApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
page = 56 # int | ページ番号 (optional)
query_object_search_keyword = 'query_object_search_keyword_example' # str | 部門名称または部門コードで部分一致検索する (optional)

    try:
        # 部門一覧を返す
        api_response = api_instance.find_depts(office_id, page=page, query_object_search_keyword=query_object_search_keyword)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeptApi->find_depts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **page** | **int**| ページ番号 | [optional]
 **query_object_search_keyword** | **str**| 部門名称または部門コードで部分一致検索する | [optional]

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

# **update_dept**
> Dept update_dept(office_id, id, unknown_base_type)

部門を更新する

部門を更新する

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
    api_instance = moneyforward_ex.DeptApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id
unknown_base_type = moneyforward_ex.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 部門のパラメータ

    try:
        # 部門を更新する
        api_response = api_instance.update_dept(office_id, id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DeptApi->update_dept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| 部門のパラメータ |

### Return type

[**Dept**](Dept.md)

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

