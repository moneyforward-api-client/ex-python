# OfficeMember

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | メンバーid | 
**identification_code** | **str** | メンバー識別番号 | [optional] 
**number** | **str** | 従業員番号 | [optional] 
**name** | **str** | メンバー名 | [optional] 
**created_at** | [**Datetime**](Datetime.md) | メンバー追加日時 | [optional] 
**updated_at** | [**Datetime**](Datetime.md) | メンバー更新日時 | [optional] 
**ex_activated_at** | [**Datetime**](Datetime.md) | 直近マネーフォワード クラウド経費利用開始日時 | [optional] 
**is_ex_user** | **bool** | マネーフォワード クラウド経費の一般権限を持つかどうか | [optional] 
**is_ex_authorizer** | **bool** | マネーフォワード クラウド経費の承認権限を持つかどうか | [optional] 
**is_ex_administrator** | **bool** | マネーフォワード クラウド経費の管理者権限を持つかどうか | [optional] 
**ex_office_member_setting** | [**ExOfficeMemberSetting**](ExOfficeMemberSetting.md) |  | [optional] 
**reimburse_bank_account** | [**ReimburseBankAccount**](ReimburseBankAccount.md) |  | [optional] 
**position** | [**Position**](Position.md) |  | [optional] 
**depts** | [**list[Dept]**](Dept.md) | メンバーの所属部門リスト | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


