# InternalHandlerKBModelConfigRequestNodeExtract

知识图谱配置

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**nodes** | [**List[GithubComTencentWeKnoraInternalTypesGraphNode]**](GithubComTencentWeKnoraInternalTypesGraphNode.md) |  | [optional] 
**relations** | [**List[GithubComTencentWeKnoraInternalTypesGraphRelation]**](GithubComTencentWeKnoraInternalTypesGraphRelation.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from weknora_sdk.models.internal_handler_kb_model_config_request_node_extract import InternalHandlerKBModelConfigRequestNodeExtract

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerKBModelConfigRequestNodeExtract from a JSON string
internal_handler_kb_model_config_request_node_extract_instance = InternalHandlerKBModelConfigRequestNodeExtract.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerKBModelConfigRequestNodeExtract.to_json())

# convert the object into a dict
internal_handler_kb_model_config_request_node_extract_dict = internal_handler_kb_model_config_request_node_extract_instance.to_dict()
# create an instance of InternalHandlerKBModelConfigRequestNodeExtract from a dict
internal_handler_kb_model_config_request_node_extract_from_dict = InternalHandlerKBModelConfigRequestNodeExtract.from_dict(internal_handler_kb_model_config_request_node_extract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


