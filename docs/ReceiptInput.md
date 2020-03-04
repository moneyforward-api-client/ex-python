# ReceiptInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | 領収書画像バイナリをBase64エンコードしたもの | 
**content_type** | **str** | 領収書画像ファイルのcontent type（MIME type） | 
**filename** | **str** | 領収書画像ファイルのファイル名 | 
**process_type** | **str** | 0:何もしない、1:オペレーター入力, 2:OCR処理, 指定なしの場合何もしない | [optional] 
**split_pdf** | **bool** | trueの場合にPDFファイルであればページ分割をする | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


