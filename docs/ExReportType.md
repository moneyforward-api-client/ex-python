# ExReportType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 申請種別id | 
**name** | **str** | 申請種別名称 | [optional] 
**use_ex_transaction_reserves** | **bool** | 明細を添付するかどうかのフラグ | [optional] [default to False]
**use_transaction_action_after_approval** | **str** | 明細を添付した場合に申請承認後の処理。transfer_to_ex_transaction: 立替の経費明細にコピー, create_journal: 仕訳を作成, none: 何もしない | [optional] [default to 'none']
**is_active** | **bool** | 使用フラグ | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


