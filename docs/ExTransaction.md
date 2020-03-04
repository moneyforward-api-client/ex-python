# ExTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 経費明細id | 
**number** | **int** | 明細番号 | [optional] 
**remark** | **str** | 支払先・内容 | [optional] 
**recognized_at** | **date** | 日付 | [optional] 
**value** | **float** | 金額 | [optional] 
**memo** | **str** | メモ | [optional] 
**report_number** | **str** | 事前申請番号 | [optional] 
**jpyrate** | **float** | 為替レート | [optional] 
**currency** | **str** | 通貨 | [optional] [default to 'JPY']
**use_custom_jpy_rate** | **bool** | 為替レートを手動設定するかどうか | [optional] [default to False]
**automatic_status** | **str** | manual: 手動登録, waiting_for_ocr_input: OCR処理待ち, waiting_for_streamed_upload: 画像アップロード待ち,  waiting_for_streamed_input: STREAMEDオペレーター入力待ち, waiting_for_input: オペレーター入力待ち, input_done: 入力完了, canceled: キャンセル | [optional] 
**error_message** | **str** | エラーメッセージ | [optional] 
**warning_message** | **str** | ワーニングメッセージ | [optional] 
**waiting_message** | **str** | 待機メッセージ | [optional] 
**office_member_id** | **str** | メンバーid | [optional] 
**ex_item_id** | **str** | 経費科目id | [optional] 
**dr_excise_id** | **str** | 税区分id | [optional] 
**dept_id** | **str** | 部門id | [optional] 
**project_code_id** | **str** | プロジェクトid | [optional] 
**cr_item_id** | **str** | 貸方勘定科目id | [optional] 
**cr_sub_item_id** | **str** | 貸方補助科目id | [optional] 
**created_at** | [**Datetime**](Datetime.md) | 登録日時 | [optional] 
**updated_at** | [**Datetime**](Datetime.md) | 更新日時 | [optional] 
**office_member** | [**OfficeMember**](OfficeMember.md) |  | [optional] 
**ex_item** | [**ExItem**](ExItem.md) |  | [optional] 
**dr_excise** | [**Excise**](Excise.md) |  | [optional] 
**dept** | [**Dept**](Dept.md) |  | [optional] 
**project_code** | [**ProjectCode**](ProjectCode.md) |  | [optional] 
**ex_report** | [**ExReport**](ExReport.md) |  | [optional] 
**ex_report_unit** | [**ExReportUnit**](ExReportUnit.md) |  | [optional] 
**mf_file** | [**MfFile**](MfFile.md) |  | [optional] 
**attendants** | [**list[Attendant]**](Attendant.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


