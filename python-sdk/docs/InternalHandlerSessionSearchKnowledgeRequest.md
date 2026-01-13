# InternalHandlerSessionSearchKnowledgeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_base_id** | **str** | Single knowledge base ID (for backward compatibility) | [optional] 
**knowledge_base_ids** | **List[str]** | IDs of knowledge bases to search (multi-KB support) | [optional] 
**knowledge_ids** | **List[str]** | IDs of specific knowledge (files) to search | [optional] 
**query** | **str** | Query text to search for | 

## Example

```python
from weknora.models.internal_handler_session_search_knowledge_request import InternalHandlerSessionSearchKnowledgeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerSessionSearchKnowledgeRequest from a JSON string
internal_handler_session_search_knowledge_request_instance = InternalHandlerSessionSearchKnowledgeRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerSessionSearchKnowledgeRequest.to_json())

# convert the object into a dict
internal_handler_session_search_knowledge_request_dict = internal_handler_session_search_knowledge_request_instance.to_dict()
# create an instance of InternalHandlerSessionSearchKnowledgeRequest from a dict
internal_handler_session_search_knowledge_request_from_dict = InternalHandlerSessionSearchKnowledgeRequest.from_dict(internal_handler_session_search_knowledge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


