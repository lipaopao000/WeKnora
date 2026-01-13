# InternalHandlerRemoteModelCheckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**base_url** | **str** |  | 
**model_name** | **str** |  | 

## Example

```python
from weknora.models.internal_handler_remote_model_check_request import InternalHandlerRemoteModelCheckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerRemoteModelCheckRequest from a JSON string
internal_handler_remote_model_check_request_instance = InternalHandlerRemoteModelCheckRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerRemoteModelCheckRequest.to_json())

# convert the object into a dict
internal_handler_remote_model_check_request_dict = internal_handler_remote_model_check_request_instance.to_dict()
# create an instance of InternalHandlerRemoteModelCheckRequest from a dict
internal_handler_remote_model_check_request_from_dict = InternalHandlerRemoteModelCheckRequest.from_dict(internal_handler_remote_model_check_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


