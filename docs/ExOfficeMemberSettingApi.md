# mfexapiclient.ExOfficeMemberSettingApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_ex_office_member_setting**](ExOfficeMemberSettingApi.md#find_ex_office_member_setting) | **GET** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/ex_office_member_setting | メンバーの経費設定を返す
[**update_ex_office_member_setting**](ExOfficeMemberSettingApi.md#update_ex_office_member_setting) | **PUT** /api/external/v1/offices/{office_id}/office_members/{office_member_id}/ex_office_member_setting | メンバーの経費設定を更新する


# **find_ex_office_member_setting**
> ExOfficeMemberSetting find_ex_office_member_setting(office_id, office_member_id)

メンバーの経費設定を返す

メンバーの経費設定を返す

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
    api_instance = mfexapiclient.ExOfficeMemberSettingApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    office_member_id = 'office_member_id_example' # str | メンバーid

    try:
        # メンバーの経費設定を返す
        api_response = api_instance.find_ex_office_member_setting(office_id, office_member_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExOfficeMemberSettingApi->find_ex_office_member_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **office_member_id** | **str**| メンバーid |

### Return type

[**ExOfficeMemberSetting**](ExOfficeMemberSetting.md)

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

# **update_ex_office_member_setting**
> ExOfficeMemberSetting update_ex_office_member_setting(office_id, office_member_id, unknown_base_type)

メンバーの経費設定を更新する

メンバーの経費設定を更新する

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
    api_instance = mfexapiclient.ExOfficeMemberSettingApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    office_member_id = 'office_member_id_example' # str | メンバーid
    unknown_base_type = mfexapiclient.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | メンバー経費設定のパラメータ

    try:
        # メンバーの経費設定を更新する
        api_response = api_instance.update_ex_office_member_setting(office_id, office_member_id, unknown_base_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExOfficeMemberSettingApi->update_ex_office_member_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **office_member_id** | **str**| メンバーid |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| メンバー経費設定のパラメータ |

### Return type

[**ExOfficeMemberSetting**](ExOfficeMemberSetting.md)

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

