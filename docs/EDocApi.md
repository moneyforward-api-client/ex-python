# mfexapiclient.EDocApi

All URIs are relative to *https://expense.moneyforward.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_e_docs**](EDocApi.md#find_e_docs) | **GET** /api/external/v1/offices/{office_id}/e_docs | 電子帳簿保存法書類情報を返す
[**send_mf_file_belongs_to_e_doc**](EDocApi.md#send_mf_file_belongs_to_e_doc) | **GET** /api/external/v1/offices/{office_id}/e_docs/{e_doc_id}/mf_file | 電子帳簿保存法書類データに紐づく画像ファイルを返す


# **find_e_docs**
> object find_e_docs(office_id, page=page)

電子帳簿保存法書類情報を返す

電子帳簿保存法書類情報を返す

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
    api_instance = mfexapiclient.EDocApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
    page = 56 # int | ページ番号 (optional)

    try:
        # 電子帳簿保存法書類情報を返す
        api_response = api_instance.find_e_docs(office_id, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EDocApi->find_e_docs: %s\n" % e)
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

# **send_mf_file_belongs_to_e_doc**
> file send_mf_file_belongs_to_e_doc(office_id, e_doc_id)

電子帳簿保存法書類データに紐づく画像ファイルを返す

電子帳簿保存法書類データに紐づく画像ファイルを返す

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
    api_instance = mfexapiclient.EDocApi(api_client)
    office_id = 'office_id_example' # str | 事業所id
e_doc_id = 'e_doc_id_example' # str | e_doc id

    try:
        # 電子帳簿保存法書類データに紐づく画像ファイルを返す
        api_response = api_instance.send_mf_file_belongs_to_e_doc(office_id, e_doc_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EDocApi->send_mf_file_belongs_to_e_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **office_id** | **str**| 事業所id |
 **e_doc_id** | **str**| e_doc id |

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

