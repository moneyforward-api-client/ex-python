# ExDestination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 支配先id | 
**name** | **str** | 名称 | 
**code** | **str** | 支払先コード | [optional] 
**pay_day** | **int** | 支払日（月末は31） | 
**number_of_months_later** | **int** | 支払が通常請求書を受け取ったタイミングから何ヶ月後か | 
**exclude_holiday_kind** | **int** | 休日調整（0:調整しない, 1:前倒し, 2:後ろ倒し | 
**is_withholding_tax** | **bool** | 源泉徴収対象支払先かどうか | [default to False]
**default_ex_item_id** | **str** | デフォルト経費科目id | [optional] 
**default_cr_item_id** | **str** | デフォルト貸方科目id | [optional] 
**default_cr_sub_item_id** | **str** | デフォルト貸方補助科目id | [optional] 
**default_dept_id** | **str** | デフォルト部門id | [optional] 
**default_project_code_id** | **str** | デフォルトプロジェクトid | [optional] 
**withholding_tax_cr_item_id** | **str** | デフォルト源泉徴収用貸方科目id | [optional] 
**withholding_tax_cr_sub_item_id** | **str** | デフォルト源泉徴収用貸方補助科目id | [optional] 
**is_tax_include** | **bool** | 税込入力フラグ | [optional] [default to False]
**is_active** | **bool** | 表示フラグ。オフで新規の登録等の選択肢に表示されなくなります | [default to True]
**priority** | **int** | 表示優先順（昇順） | [default to 100]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


