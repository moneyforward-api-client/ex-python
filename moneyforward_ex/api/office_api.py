# coding: utf-8

"""
    マネーフォワード クラウド経費API

    このページは[マネーフォワード クラウド経費](https://expense.moneyforward.com)（クラウド型の経費精算・ワークフローサービス）のAPIドキュメントです。ご利用開始の手順については、[github](https://github.com/moneyforward/expense-api-doc) をご覧ください。バグ報告や改善要望はgithub上からissue登録をして頂ければ幸いです。このドキュメントは[Swagger](http://swagger.io)の仕様で作成されています。実際にこのページでAPIの試打を行うことができます。試打を行いたい場合は、APIを利用するアプリケーションの登録の際に、Redirect URIを`https://expense.moneyforward.com/api/oauth2-redirect.html`に指定してお試しください。  # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from moneyforward_ex.api_client import ApiClient
from moneyforward_ex.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class OfficeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def find_offices(self, **kwargs):  # noqa: E501
        """自分が所属する事業所一覧を返す  # noqa: E501

        自分が所属する事業所一覧を返す  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_offices(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: ページ番号
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_offices_with_http_info(**kwargs)  # noqa: E501

    def find_offices_with_http_info(self, **kwargs):  # noqa: E501
        """自分が所属する事業所一覧を返す  # noqa: E501

        自分が所属する事業所一覧を返す  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_offices_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int page: ページ番号
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(object, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_offices" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['mf_expense_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/external/v1/offices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
