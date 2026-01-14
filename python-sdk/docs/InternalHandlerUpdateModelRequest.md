# InternalHandlerUpdateModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parameters** | [**GithubComTencentWeKnoraInternalTypesModelParameters**](GithubComTencentWeKnoraInternalTypesModelParameters.md) |  | [optional] 
**source** | [**GithubComTencentWeKnoraInternalTypesModelSource**](GithubComTencentWeKnoraInternalTypesModelSource.md) |  | [optional] 
**type** | [**GithubComTencentWeKnoraInternalTypesModelType**](GithubComTencentWeKnoraInternalTypesModelType.md) |  | [optional] 

## Example

```python
from weknora_sdk.models.internal_handler_update_model_request import InternalHandlerUpdateModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerUpdateModelRequest from a JSON string
internal_handler_update_model_request_instance = InternalHandlerUpdateModelRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerUpdateModelRequest.to_json())

# convert the object into a dict
internal_handler_update_model_request_dict = internal_handler_update_model_request_instance.to_dict()
# create an instance of InternalHandlerUpdateModelRequest from a dict
internal_handler_update_model_request_from_dict = InternalHandlerUpdateModelRequest.from_dict(internal_handler_update_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


