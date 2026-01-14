# InternalHandlerUpdateKnowledgeBaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig**](GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig.md) |  | 
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from weknora_sdk.models.internal_handler_update_knowledge_base_request import InternalHandlerUpdateKnowledgeBaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerUpdateKnowledgeBaseRequest from a JSON string
internal_handler_update_knowledge_base_request_instance = InternalHandlerUpdateKnowledgeBaseRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerUpdateKnowledgeBaseRequest.to_json())

# convert the object into a dict
internal_handler_update_knowledge_base_request_dict = internal_handler_update_knowledge_base_request_instance.to_dict()
# create an instance of InternalHandlerUpdateKnowledgeBaseRequest from a dict
internal_handler_update_knowledge_base_request_from_dict = InternalHandlerUpdateKnowledgeBaseRequest.from_dict(internal_handler_update_knowledge_base_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


