# ExInvoiceTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 支払明細id | 
**office_id** | **str** | 事業所id | 
**office_member_id** | **str** | メンバーid | 
**ex_report_id** | **str** | 申請id | 
**ex_destination_id** | **str** | 支払先id | [optional] 
**dept_id** | **str** | 部門id | [optional] 
**project_code_id** | **str** | プロジェクトid | [optional] 
**ex_item_id** | **str** | 経費科目id | [optional] 
**dr_excise_id** | **str** | 税区分id | [optional] 
**cr_item_id** | **str** | 貸方勘定科目id | [optional] 
**cr_sub_item_id** | **str** | 貸方補助科目id | [optional] 
**number** | **int** | 明細番号 | 
**name** | **str** | 品目 | [optional] 
**unit_value** | **float** | 単価 | [optional] 
**quantity** | **float** | 数量 | 
**total_value** | **int** | 合計金額 | 
**excise_value** | **int** | 消費税額 | 
**has_withholding_income_tax** | **bool** | 源泉徴収有無 | [optional] [default to False]
**withholding_income_tax_value** | **int** | 源泉徴収税額 | [optional] 
**memo** | **str** | メモ | [optional] 
**currency** | **str** | 通貨 | [optional] [default to 'JPY']
**jpyrate** | **float** | 為替レート | 
**use_custom_jpy_rate** | **bool** | 為替レートを手動設定するかどうか | [default to False]
**created_at** | [**Datetime**](Datetime.md) | 登録日時 | [optional] 
**updated_at** | [**Datetime**](Datetime.md) | 更新日時 | [optional] 
**office_member** | [**OfficeMember**](OfficeMember.md) |  | [optional] 
**ex_report** | [**ExReport**](ExReport.md) |  | [optional] 
**ex_destination** | [**ExDestination**](ExDestination.md) |  | [optional] 
**dept** | [**Dept**](Dept.md) |  | [optional] 
**project_code** | [**ProjectCode**](ProjectCode.md) |  | [optional] 
**ex_item** | [**ExItem**](ExItem.md) |  | [optional] 
**dr_excise** | [**Excise**](Excise.md) |  | [optional] 
**cr_item** | [**Item**](Item.md) |  | [optional] 
**cr_sub_item** | [**SubItem**](SubItem.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


