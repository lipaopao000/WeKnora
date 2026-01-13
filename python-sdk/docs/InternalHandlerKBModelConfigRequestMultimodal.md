# InternalHandlerKBModelConfigRequestMultimodal

多模态配置

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cos** | [**InternalHandlerKBModelConfigRequestMultimodalCos**](InternalHandlerKBModelConfigRequestMultimodalCos.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**minio** | [**InternalHandlerKBModelConfigRequestMultimodalMinio**](InternalHandlerKBModelConfigRequestMultimodalMinio.md) |  | [optional] 
**storage_type** | **str** | \&quot;cos\&quot; or \&quot;minio\&quot; | [optional] 

## Example

```python
from weknora.models.internal_handler_kb_model_config_request_multimodal import InternalHandlerKBModelConfigRequestMultimodal

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerKBModelConfigRequestMultimodal from a JSON string
internal_handler_kb_model_config_request_multimodal_instance = InternalHandlerKBModelConfigRequestMultimodal.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerKBModelConfigRequestMultimodal.to_json())

# convert the object into a dict
internal_handler_kb_model_config_request_multimodal_dict = internal_handler_kb_model_config_request_multimodal_instance.to_dict()
# create an instance of InternalHandlerKBModelConfigRequestMultimodal from a dict
internal_handler_kb_model_config_request_multimodal_from_dict = InternalHandlerKBModelConfigRequestMultimodal.from_dict(internal_handler_kb_model_config_request_multimodal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


