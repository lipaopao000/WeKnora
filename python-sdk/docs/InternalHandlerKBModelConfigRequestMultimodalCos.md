# InternalHandlerKBModelConfigRequestMultimodalCos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**bucket_name** | **str** |  | [optional] 
**path_prefix** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**secret_id** | **str** |  | [optional] 
**secret_key** | **str** |  | [optional] 

## Example

```python
from weknora.models.internal_handler_kb_model_config_request_multimodal_cos import InternalHandlerKBModelConfigRequestMultimodalCos

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerKBModelConfigRequestMultimodalCos from a JSON string
internal_handler_kb_model_config_request_multimodal_cos_instance = InternalHandlerKBModelConfigRequestMultimodalCos.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerKBModelConfigRequestMultimodalCos.to_json())

# convert the object into a dict
internal_handler_kb_model_config_request_multimodal_cos_dict = internal_handler_kb_model_config_request_multimodal_cos_instance.to_dict()
# create an instance of InternalHandlerKBModelConfigRequestMultimodalCos from a dict
internal_handler_kb_model_config_request_multimodal_cos_from_dict = InternalHandlerKBModelConfigRequestMultimodalCos.from_dict(internal_handler_kb_model_config_request_multimodal_cos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


