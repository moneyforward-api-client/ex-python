# moneyforward_ex.ExDestinationApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ex_destination**](ExDestinationApi.md#create_ex_destination) | **POST** /api/external/v1/offices/{office_id}/ex_destinations | 支払先マスタを作成する
[**delete_ex_destination**](ExDestinationApi.md#delete_ex_destination) | **DELETE** /api/external/v1/offices/{office_id}/ex_destinations/{id} | 支払先マスタを削除する
[**find_ex_destination**](ExDestinationApi.md#find_ex_destination) | **GET** /api/external/v1/offices/{office_id}/ex_destinations/{id} | 支払先マスタを返す
[**find_ex_destinations**](ExDestinationApi.md#find_ex_destinations) | **GET** /api/external/v1/offices/{office_id}/ex_destinations | 支払先マスタ一覧を返す
[**update_ex_destination**](ExDestinationApi.md#update_ex_destination) | **PUT** /api/external/v1/offices/{office_id}/ex_destinations/{id} | 支払先マスタを更新する


# **create_ex_destination**
> ExDestination create_ex_destination(office_id, unknown_base_type)

支払先マスタを作成する

支払先マスタを作成する

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
    api_instance = moneyforward_ex.ExDestinationApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
unknown_base_type = moneyforward_ex.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | プロジェクトのパラメータ

    try:
        # 支払先マスタを作成する
        api_response = api_instance.create_ex_destination(office_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExDestinationApi->create_ex_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| プロジェクトのパラメータ |

### Return type

[**ExDestination**](ExDestination.md)

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

# **delete_ex_destination**
> delete_ex_destination(office_id, id)

支払先マスタを削除する

支払先マスタを削除する

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
    api_instance = moneyforward_ex.ExDestinationApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id

    try:
        # 支払先マスタを削除する
        api_instance.delete_ex_destination(office_id, id)
    except ApiException as e:
        print("Exception when calling ExDestinationApi->delete_ex_destination: %s\n" % e)
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

# **find_ex_destination**
> ExDestination find_ex_destination(office_id, id, page=page)

支払先マスタを返す

支払先マスタを返す

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
    api_instance = moneyforward_ex.ExDestinationApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id
page = 56 # int | ページ番号 (optional)

    try:
        # 支払先マスタを返す
        api_response = api_instance.find_ex_destination(office_id, id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExDestinationApi->find_ex_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **page** | **int**| ページ番号 | [optional]

### Return type

[**ExDestination**](ExDestination.md)

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

# **find_ex_destinations**
> object find_ex_destinations(office_id, page=page)

支払先マスタ一覧を返す

支払先マスタ一覧を返す

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
    api_instance = moneyforward_ex.ExDestinationApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
page = 56 # int | ページ番号 (optional)

    try:
        # 支払先マスタ一覧を返す
        api_response = api_instance.find_ex_destinations(office_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExDestinationApi->find_ex_destinations: %s\n" % e)
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

# **update_ex_destination**
> ExDestination update_ex_destination(office_id, id, unknown_base_type)

支払先マスタを更新する

支払先マスタを更新する

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
    api_instance = moneyforward_ex.ExDestinationApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id
unknown_base_type = moneyforward_ex.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | プロジェクトのパラメータ

    try:
        # 支払先マスタを更新する
        api_response = api_instance.update_ex_destination(office_id, id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExDestinationApi->update_ex_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| プロジェクトのパラメータ |

### Return type

[**ExDestination**](ExDestination.md)

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

