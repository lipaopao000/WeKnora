# InternalHandlerKBModelConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_splitting** | [**InternalHandlerKBModelConfigRequestDocumentSplitting**](InternalHandlerKBModelConfigRequestDocumentSplitting.md) |  | [optional] 
**embedding_model_id** | **str** |  | 
**llm_model_id** | **str** |  | 
**multimodal** | [**InternalHandlerKBModelConfigRequestMultimodal**](InternalHandlerKBModelConfigRequestMultimodal.md) |  | [optional] 
**node_extract** | [**InternalHandlerKBModelConfigRequestNodeExtract**](InternalHandlerKBModelConfigRequestNodeExtract.md) |  | [optional] 
**question_generation** | [**InternalHandlerKBModelConfigRequestQuestionGeneration**](InternalHandlerKBModelConfigRequestQuestionGeneration.md) |  | [optional] 
**vlm_config** | [**GithubComTencentWeKnoraInternalTypesVLMConfig**](GithubComTencentWeKnoraInternalTypesVLMConfig.md) |  | [optional] 

## Example

```python
from weknora.models.internal_handler_kb_model_config_request import InternalHandlerKBModelConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerKBModelConfigRequest from a JSON string
internal_handler_kb_model_config_request_instance = InternalHandlerKBModelConfigRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerKBModelConfigRequest.to_json())

# convert the object into a dict
internal_handler_kb_model_config_request_dict = internal_handler_kb_model_config_request_instance.to_dict()
# create an instance of InternalHandlerKBModelConfigRequest from a dict
internal_handler_kb_model_config_request_from_dict = InternalHandlerKBModelConfigRequest.from_dict(internal_handler_kb_model_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


