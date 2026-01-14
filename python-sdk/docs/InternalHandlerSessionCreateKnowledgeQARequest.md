# InternalHandlerSessionCreateKnowledgeQARequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_enabled** | **bool** | Whether agent mode is enabled for this request | [optional] 
**knowledge_base_ids** | **List[str]** | Selected knowledge base ID for this request | [optional] 
**knowledge_ids** | **List[str]** | Selected knowledge ID for this request | [optional] 
**mentioned_items** | [**List[InternalHandlerSessionMentionedItemRequest]**](InternalHandlerSessionMentionedItemRequest.md) | @mentioned knowledge bases and files | [optional] 
**query** | **str** | Query text for knowledge base search | 
**summary_model_id** | **str** | Optional summary model ID for this request (overrides session default) | [optional] 
**web_search_enabled** | **bool** | Whether web search is enabled for this request | [optional] 

## Example

```python
from weknora_sdk.models.internal_handler_session_create_knowledge_qa_request import InternalHandlerSessionCreateKnowledgeQARequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerSessionCreateKnowledgeQARequest from a JSON string
internal_handler_session_create_knowledge_qa_request_instance = InternalHandlerSessionCreateKnowledgeQARequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerSessionCreateKnowledgeQARequest.to_json())

# convert the object into a dict
internal_handler_session_create_knowledge_qa_request_dict = internal_handler_session_create_knowledge_qa_request_instance.to_dict()
# create an instance of InternalHandlerSessionCreateKnowledgeQARequest from a dict
internal_handler_session_create_knowledge_qa_request_from_dict = InternalHandlerSessionCreateKnowledgeQARequest.from_dict(internal_handler_session_create_knowledge_qa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


