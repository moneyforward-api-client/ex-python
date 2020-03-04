# mfexapiclient.OfficeMemberApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_office_member**](OfficeMemberApi.md#create_office_member) | **POST** /api/external/v1/offices/{office_id}/office_members | メンバーを追加する
[**destroy_office_member**](OfficeMemberApi.md#destroy_office_member) | **DELETE** /api/external/v1/offices/{office_id}/office_members/{id} | メンバーを削除する
[**destroy_reimburse_bank_account**](OfficeMemberApi.md#destroy_reimburse_bank_account) | **DELETE** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/reimburse_bank_account | メンバーの振込口座を削除する
[**find_office_member**](OfficeMemberApi.md#find_office_member) | **GET** /api/external/v1/offices/{office_id}/office_members/{id} | 事業所に所属するメンバーを返す
[**find_office_members**](OfficeMemberApi.md#find_office_members) | **GET** /api/external/v1/offices/{office_id}/office_members | 事業所に所属するメンバー一覧を返す
[**save_reimburse_bank_account**](OfficeMemberApi.md#save_reimburse_bank_account) | **PUT** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/reimburse_bank_account | メンバーの振込口座を登録／更新する
[**update_office_member**](OfficeMemberApi.md#update_office_member) | **PUT** /api/external/v1/offices/{office_id}/office_members/{id} | メンバーを更新する


# **create_office_member**
> OfficeMember create_office_member(office_id, unknown_base_type)

メンバーを追加する

メンバーを追加する

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
    api_instance = mfexapiclient.OfficeMemberApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | メンバーのパラメータ

    try:
        # メンバーを追加する
        api_response = api_instance.create_office_member(office_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficeMemberApi->create_office_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| メンバーのパラメータ |

### Return type

[**OfficeMember**](OfficeMember.md)

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

# **destroy_office_member**
> destroy_office_member(office_id, id)

メンバーを削除する

メンバーを削除する

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
    api_instance = mfexapiclient.OfficeMemberApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id

    try:
        # メンバーを削除する
        api_instance.destroy_office_member(office_id, id)
    except ApiException as e:
        print("Exception when calling OfficeMemberApi->destroy_office_member: %s\n" % e)
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

# **destroy_reimburse_bank_account**
> destroy_reimburse_bank_account(office_id, office_member_id)

メンバーの振込口座を削除する

メンバーの振込口座を削除する

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
    api_instance = mfexapiclient.OfficeMemberApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    office_member_id = 'office_member_id_example' # str | メンバーid

    try:
        # メンバーの振込口座を削除する
        api_instance.destroy_reimburse_bank_account(office_id, office_member_id)
    except ApiException as e:
        print("Exception when calling OfficeMemberApi->destroy_reimburse_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **office_member_id** | **str**| メンバーid |

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

# **find_office_member**
> OfficeMember find_office_member(office_id, id)

事業所に所属するメンバーを返す

事業所に所属するメンバーを返す

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
    api_instance = mfexapiclient.OfficeMemberApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id

    try:
        # 事業所に所属するメンバーを返す
        api_response = api_instance.find_office_member(office_id, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficeMemberApi->find_office_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |

### Return type

[**OfficeMember**](OfficeMember.md)

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

# **find_office_members**
> object find_office_members(office_id, page=page)

事業所に所属するメンバー一覧を返す

事業所に所属するメンバー一覧を返す

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
    api_instance = mfexapiclient.OfficeMemberApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    page = 56 # int | ページ番号 (optional)

    try:
        # 事業所に所属するメンバー一覧を返す
        api_response = api_instance.find_office_members(office_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficeMemberApi->find_office_members: %s\n" % e)
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

# **save_reimburse_bank_account**
> ReimburseBankAccount save_reimburse_bank_account(office_id, office_member_id, unknown_base_type)

メンバーの振込口座を登録／更新する

メンバーの振込口座を登録／更新する

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
    api_instance = mfexapiclient.OfficeMemberApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    office_member_id = 'office_member_id_example' # str | メンバーid
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | メンバーの振込口座のパラメータ

    try:
        # メンバーの振込口座を登録／更新する
        api_response = api_instance.save_reimburse_bank_account(office_id, office_member_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficeMemberApi->save_reimburse_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **office_member_id** | **str**| メンバーid |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| メンバーの振込口座のパラメータ |

### Return type

[**ReimburseBankAccount**](ReimburseBankAccount.md)

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

# **update_office_member**
> OfficeMember update_office_member(office_id, id, unknown_base_type)

メンバーを更新する

メンバーを更新する

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
    api_instance = mfexapiclient.OfficeMemberApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    id = 'id_example' # str | id
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | メンバーのパラメータ

    try:
        # メンバーを更新する
        api_response = api_instance.update_office_member(office_id, id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OfficeMemberApi->update_office_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **id** | **str**| id |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| メンバーのパラメータ |

### Return type

[**OfficeMember**](OfficeMember.md)

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

