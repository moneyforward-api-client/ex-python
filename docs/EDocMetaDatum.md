# EDocMetaDatum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | e_doc id | 
**number** | **int** | 書類番号（シーケンスで採番） | 
**business_partner_name** | **str** | 支払先 | [optional] 
**trade_date** | **date** | 取引日 | [optional] 
**amount** | **float** | 取引金額 | [optional] 
**ex_transactionable_type_text** | **str** | 明細または申請種別 | [optional] 
**ex_transactionable_number** | **int** | 明細または申請番号 | [optional] 
**name** | **str** | ファイル名 | 
**document_type_text** | **str** | 書類の種類 | 
**image_width** | **int** | 画像サイズ幅（ピクセル） | [optional] 
**image_height** | **int** | 画像サイズ縦（ピクセル） | [optional] 
**page_width** | **float** | ページサイズ幅（ポイント） | [optional] 
**page_height** | **float** | ページサイズ縦（ピクセル） | [optional] 
**iso216_paper_size** | **str** | ページサイズ(ISO216規格) | [optional] 
**dpi** | **int** | 解像度（dpi） | [optional] 
**image_depth** | **int** | 階調（色） | [optional] 
**timestamp_serial** | **int** | タイムスタンプシリアル番号 | 
**timestamp_at** | [**Datetime**](Datetime.md) | タイムスタンプ時刻 | 
**timestamp_version** | **int** | タイムスタンプバージョン | 
**timestamp_station_name** | **str** | タイムスタンプ局情報 | 
**timestamp_expires_at** | [**Datetime**](Datetime.md) | タイムスタンプ有効期限 | 
**scan_office_member_name** | **str** | 登録者氏名 | [optional] 
**scan_office_member_number** | **str** | 登録者番号 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


