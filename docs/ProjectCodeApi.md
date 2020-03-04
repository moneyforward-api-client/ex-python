# mfexapiclient.ProjectCodeApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_code**](ProjectCodeApi.md#create_project_code) | **POST** /api/external/v1/offices/{office_id}/project_codes | プロジェクトコードを作成する
[**delete_project_code**](ProjectCodeApi.md#delete_project_code) | **DELETE** /api/external/v1/offices/{office_id}/project_codes/{id} | プロジェクトコードを削除する
[**find_project_code**](ProjectCodeApi.md#find_project_code) | **GET** /api/external/v1/offices/{office_id}/project_codes/{id} | プロジェクトコードを返す
[**find_project_codes**](ProjectCodeApi.md#find_project_codes) | **GET** /api/external/v1/offices/{office_id}/project_codes | プロジェクト一覧を返す
[**update_project_code**](ProjectCodeApi.md#update_project_code) | **PUT** /api/external/v1/offices/{office_id}/project_codes/{id} | プロジェクトコードを更新する


# **create_project_code**
> ProjectCode create_project_code(office_id, unknown_base_type)

プロジェクトコードを作成する

プロジェクトコードを作成する

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
    api_instance = mfexapiclient.ProjectCodeApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | プロジェクトのパラメータ

    try:
        # プロジェクトコードを作成する
        api_response = api_instance.create_project_code(office_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectCodeApi->create_project_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| プロジェクトのパラメータ |

### Return type

[**ProjectCode**](ProjectCode.md)

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

# **delete_project_code**
> delete_project_code(office_id, id)

プロジェクトコードを削除する

プロジェクトコードを削除する

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
    api_instance = mfexapiclient.ProjectCodeApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id

    try:
        # プロジェクトコードを削除する
        api_instance.delete_project_code(office_id, id)
    except ApiException as e:
        print("Exception when calling ProjectCodeApi->delete_project_code: %s\n" % e)
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

# **find_project_code**
> ProjectCode find_project_code(office_id, id, page=page)

プロジェクトコードを返す

プロジェクトコードを返す

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
    api_instance = mfexapiclient.ProjectCodeApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id
    page = 56 # int | ページ番号 (optional)

    try:
        # プロジェクトコードを返す
        api_response = api_instance.find_project_code(office_id, id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectCodeApi->find_project_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **page** | **int**| ページ番号 | [optional]

### Return type

[**ProjectCode**](ProjectCode.md)

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

# **find_project_codes**
> object find_project_codes(office_id, page=page, query_object_search_keyword=query_object_search_keyword, query_object_name=query_object_name, query_object_code=query_object_code)

プロジェクト一覧を返す

プロジェクト一覧を返す

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
    api_instance = mfexapiclient.ProjectCodeApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    page = 56 # int | ページ番号 (optional)
    query_object_search_keyword = 'query_object_search_keyword_example' # str | プロジェクト名称またはプロジェクトコードで前方一致検索する (optional)
    query_object_name = 'query_object_name_example' # str | プロジェクト名称で前方一致検索する (optional)
    query_object_code = 'query_object_code_example' # str | プロジェクトコードで前方一致検索する (optional)

    try:
        # プロジェクト一覧を返す
        api_response = api_instance.find_project_codes(office_id, page=page, query_object_search_keyword=query_object_search_keyword, query_object_name=query_object_name, query_object_code=query_object_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectCodeApi->find_project_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **page** | **int**| ページ番号 | [optional]
 **query_object_search_keyword** | **str**| プロジェクト名称またはプロジェクトコードで前方一致検索する | [optional]
 **query_object_name** | **str**| プロジェクト名称で前方一致検索する | [optional]
 **query_object_code** | **str**| プロジェクトコードで前方一致検索する | [optional]

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

# **update_project_code**
> ProjectCode update_project_code(office_id, id, unknown_base_type)

プロジェクトコードを更新する

プロジェクトコードを更新する

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
    api_instance = mfexapiclient.ProjectCodeApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | プロジェクトのパラメータ

    try:
        # プロジェクトコードを更新する
        api_response = api_instance.update_project_code(office_id, id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectCodeApi->update_project_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| プロジェクトのパラメータ |

### Return type

[**ProjectCode**](ProjectCode.md)

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

