# ExItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 経費科目id | 
**name** | **str** | 経費科目名称 | [optional] 
**code** | **str** | コード | [optional] 
**is_active** | **bool** | 利用可否フラグ。新規の経費登録等で利用できるかどうかを表す。 | [optional] [default to True]
**item_id** | **str** | 勘定科目id | [optional] 
**sub_item_id** | **str** | 補助科目id | [optional] 
**default_excise_id** | **str** | デフォルト税区分id | [optional] 
**item** | [**Item**](Item.md) |  | [optional] 
**sub_item** | [**SubItem**](SubItem.md) |  | [optional] 
**default_dr_excise** | [**Excise**](Excise.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


