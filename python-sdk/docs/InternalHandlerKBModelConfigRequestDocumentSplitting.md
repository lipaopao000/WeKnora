# InternalHandlerKBModelConfigRequestDocumentSplitting

文档分块配置

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_overlap** | **int** |  | [optional] 
**chunk_size** | **int** |  | [optional] 
**separators** | **List[str]** |  | [optional] 

## Example

```python
from weknora.models.internal_handler_kb_model_config_request_document_splitting import InternalHandlerKBModelConfigRequestDocumentSplitting

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerKBModelConfigRequestDocumentSplitting from a JSON string
internal_handler_kb_model_config_request_document_splitting_instance = InternalHandlerKBModelConfigRequestDocumentSplitting.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerKBModelConfigRequestDocumentSplitting.to_json())

# convert the object into a dict
internal_handler_kb_model_config_request_document_splitting_dict = internal_handler_kb_model_config_request_document_splitting_instance.to_dict()
# create an instance of InternalHandlerKBModelConfigRequestDocumentSplitting from a dict
internal_handler_kb_model_config_request_document_splitting_from_dict = InternalHandlerKBModelConfigRequestDocumentSplitting.from_dict(internal_handler_kb_model_config_request_document_splitting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


