# moneyforward_ex.PositionApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_position**](PositionApi.md#create_position) | **POST** /api/external/v1/offices/{office_id}/positions | 役職を作成する
[**delete_position**](PositionApi.md#delete_position) | **DELETE** /api/external/v1/offices/{office_id}/positions/{id} | 役職を削除する
[**find_position**](PositionApi.md#find_position) | **GET** /api/external/v1/offices/{office_id}/positions/{id} | 役職を返す
[**find_positions**](PositionApi.md#find_positions) | **GET** /api/external/v1/offices/{office_id}/positions | 役職一覧を返す
[**update_position**](PositionApi.md#update_position) | **PUT** /api/external/v1/offices/{office_id}/positions/{id} | 役職を更新する


# **create_position**
> Position create_position(office_id, unknown_base_type)

役職を作成する

役職を作成する

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
    api_instance = moneyforward_ex.PositionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
unknown_base_type = moneyforward_ex.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 役職のパラメータ

    try:
        # 役職を作成する
        api_response = api_instance.create_position(office_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PositionApi->create_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| 役職のパラメータ |

### Return type

[**Position**](Position.md)

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

# **delete_position**
> delete_position(office_id, id)

役職を削除する

役職を削除する

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
    api_instance = moneyforward_ex.PositionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id

    try:
        # 役職を削除する
        api_instance.delete_position(office_id, id)
    except ApiException as e:
        print("Exception when calling PositionApi->delete_position: %s\n" % e)
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

# **find_position**
> Position find_position(office_id, id, page=page)

役職を返す

役職を返す

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
    api_instance = moneyforward_ex.PositionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id
page = 56 # int | ページ番号 (optional)

    try:
        # 役職を返す
        api_response = api_instance.find_position(office_id, id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PositionApi->find_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **page** | **int**| ページ番号 | [optional]

### Return type

[**Position**](Position.md)

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

# **find_positions**
> object find_positions(office_id, page=page)

役職一覧を返す

役職一覧を返す

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
    api_instance = moneyforward_ex.PositionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
page = 56 # int | ページ番号 (optional)

    try:
        # 役職一覧を返す
        api_response = api_instance.find_positions(office_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PositionApi->find_positions: %s\n" % e)
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

# **update_position**
> Position update_position(office_id, id, unknown_base_type)

役職を更新する

役職を更新する

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
    api_instance = moneyforward_ex.PositionApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
id = 'id_example' # str | id
unknown_base_type = moneyforward_ex.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 役職のパラメータ

    try:
        # 役職を更新する
        api_response = api_instance.update_position(office_id, id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PositionApi->update_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| 役職のパラメータ |

### Return type

[**Position**](Position.md)

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

