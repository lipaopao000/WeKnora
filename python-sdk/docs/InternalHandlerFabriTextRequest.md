# InternalHandlerFabriTextRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_config** | [**InternalHandlerLLMConfig**](InternalHandlerLLMConfig.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from weknora_sdk.models.internal_handler_fabri_text_request import InternalHandlerFabriTextRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerFabriTextRequest from a JSON string
internal_handler_fabri_text_request_instance = InternalHandlerFabriTextRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerFabriTextRequest.to_json())

# convert the object into a dict
internal_handler_fabri_text_request_dict = internal_handler_fabri_text_request_instance.to_dict()
# create an instance of InternalHandlerFabriTextRequest from a dict
internal_handler_fabri_text_request_from_dict = InternalHandlerFabriTextRequest.from_dict(internal_handler_fabri_text_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


