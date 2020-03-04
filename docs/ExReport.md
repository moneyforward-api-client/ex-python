# ExReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 申請id | 
**ex_report_type_id** | **str** | 申請種類id | [optional] 
**office_member_id** | **str** | メンバーid | [optional] 
**number** | **int** | 申請番号 | [optional] 
**title** | **str** | タイトル | [optional] 
**submitted_at** | [**Datetime**](Datetime.md) | 申請日時 | [optional] 
**approved_at** | [**Datetime**](Datetime.md) | 承認日時 | [optional] 
**created_at** | [**Datetime**](Datetime.md) | 登録日時 | [optional] 
**updated_at** | [**Datetime**](Datetime.md) | 更新日時 | [optional] 
**status** | **str** | unsubmitted: 下書き, waiting_step_one: 第一承認待ち, waiting_step_two: 第二承認待ち, waiting_step_three: 第三承認待ち, waiting_step_four: 第四承認待ち, waiting_step_five: 第五承認待ち, approved: 承認済み, paid: 支払済み, canceled: 取消済み, rejected: 却下済み | [optional] 
**ex_report_approvals** | [**list[ExReportApproval]**](ExReportApproval.md) | 承認レコードリスト | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


