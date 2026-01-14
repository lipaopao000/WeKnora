# InternalHandlerSessionMentionedItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**kb_type** | **str** | \&quot;document\&quot; or \&quot;faq\&quot; (only for kb type) | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** | \&quot;kb\&quot; for knowledge base, \&quot;file\&quot; for file | [optional] 

## Example

```python
from weknora_sdk.models.internal_handler_session_mentioned_item_request import InternalHandlerSessionMentionedItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerSessionMentionedItemRequest from a JSON string
internal_handler_session_mentioned_item_request_instance = InternalHandlerSessionMentionedItemRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerSessionMentionedItemRequest.to_json())

# convert the object into a dict
internal_handler_session_mentioned_item_request_dict = internal_handler_session_mentioned_item_request_instance.to_dict()
# create an instance of InternalHandlerSessionMentionedItemRequest from a dict
internal_handler_session_mentioned_item_request_from_dict = InternalHandlerSessionMentionedItemRequest.from_dict(internal_handler_session_mentioned_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


