# InternalHandlerCopyKnowledgeBaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** |  | 
**target_id** | **str** |  | [optional] 

## Example

```python
from weknora_sdk.models.internal_handler_copy_knowledge_base_request import InternalHandlerCopyKnowledgeBaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerCopyKnowledgeBaseRequest from a JSON string
internal_handler_copy_knowledge_base_request_instance = InternalHandlerCopyKnowledgeBaseRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerCopyKnowledgeBaseRequest.to_json())

# convert the object into a dict
internal_handler_copy_knowledge_base_request_dict = internal_handler_copy_knowledge_base_request_instance.to_dict()
# create an instance of InternalHandlerCopyKnowledgeBaseRequest from a dict
internal_handler_copy_knowledge_base_request_from_dict = InternalHandlerCopyKnowledgeBaseRequest.from_dict(internal_handler_copy_knowledge_base_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


