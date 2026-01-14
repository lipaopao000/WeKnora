# InternalHandlerSessionGenerateTitleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[GithubComTencentWeKnoraInternalTypesMessage]**](GithubComTencentWeKnoraInternalTypesMessage.md) | Messages to use as context for title generation | 

## Example

```python
from weknora_sdk.models.internal_handler_session_generate_title_request import InternalHandlerSessionGenerateTitleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerSessionGenerateTitleRequest from a JSON string
internal_handler_session_generate_title_request_instance = InternalHandlerSessionGenerateTitleRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerSessionGenerateTitleRequest.to_json())

# convert the object into a dict
internal_handler_session_generate_title_request_dict = internal_handler_session_generate_title_request_instance.to_dict()
# create an instance of InternalHandlerSessionGenerateTitleRequest from a dict
internal_handler_session_generate_title_request_from_dict = InternalHandlerSessionGenerateTitleRequest.from_dict(internal_handler_session_generate_title_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


