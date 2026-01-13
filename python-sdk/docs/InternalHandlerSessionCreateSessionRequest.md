# InternalHandlerSessionCreateSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_config** | [**GithubComTencentWeKnoraInternalTypesSessionAgentConfig**](GithubComTencentWeKnoraInternalTypesSessionAgentConfig.md) | Agent configuration (optional, session-level config only: enabled and knowledge_bases) | [optional] 
**knowledge_base_id** | **str** | ID of the associated knowledge base (optional, can be set/changed during queries) | [optional] 
**session_strategy** | [**InternalHandlerSessionSessionStrategy**](InternalHandlerSessionSessionStrategy.md) | Session strategy configuration | [optional] 

## Example

```python
from weknora.models.internal_handler_session_create_session_request import InternalHandlerSessionCreateSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerSessionCreateSessionRequest from a JSON string
internal_handler_session_create_session_request_instance = InternalHandlerSessionCreateSessionRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerSessionCreateSessionRequest.to_json())

# convert the object into a dict
internal_handler_session_create_session_request_dict = internal_handler_session_create_session_request_instance.to_dict()
# create an instance of InternalHandlerSessionCreateSessionRequest from a dict
internal_handler_session_create_session_request_from_dict = InternalHandlerSessionCreateSessionRequest.from_dict(internal_handler_session_create_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


