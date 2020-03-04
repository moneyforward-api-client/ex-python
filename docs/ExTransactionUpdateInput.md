# ExTransactionUpdateInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remark** | **str** | 支払先・内容 | [optional] 
**recognized_at** | **date** | 日付 | [optional] 
**value** | **float** | 金額 | [optional] 
**memo** | **str** | メモ | [optional] 
**report_number** | **str** | 事前申請番号 | [optional] 
**jpyrate** | **float** | 為替レート | [optional] 
**currency** | **str** | 通貨 | [optional] [default to 'JPY']
**use_custom_jpy_rate** | **bool** | 為替レートを手動設定するかどうか | [optional] [default to False]
**ex_item_id** | **str** | 経費科目id | [optional] 
**dr_excise_id** | **str** | 税区分id | [optional] 
**dept_id** | **str** | 部門id | [optional] 
**project_code_id** | **str** | プロジェクトid | [optional] 
**cr_item_id** | **str** | 貸方勘定科目id | [optional] 
**cr_sub_item_id** | **str** | 貸方補助科目id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


