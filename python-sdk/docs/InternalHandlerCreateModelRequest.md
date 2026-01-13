# InternalHandlerCreateModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**parameters** | [**GithubComTencentWeKnoraInternalTypesModelParameters**](GithubComTencentWeKnoraInternalTypesModelParameters.md) |  | 
**source** | [**GithubComTencentWeKnoraInternalTypesModelSource**](GithubComTencentWeKnoraInternalTypesModelSource.md) |  | 
**type** | [**GithubComTencentWeKnoraInternalTypesModelType**](GithubComTencentWeKnoraInternalTypesModelType.md) |  | 

## Example

```python
from weknora.models.internal_handler_create_model_request import InternalHandlerCreateModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerCreateModelRequest from a JSON string
internal_handler_create_model_request_instance = InternalHandlerCreateModelRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerCreateModelRequest.to_json())

# convert the object into a dict
internal_handler_create_model_request_dict = internal_handler_create_model_request_instance.to_dict()
# create an instance of InternalHandlerCreateModelRequest from a dict
internal_handler_create_model_request_from_dict = InternalHandlerCreateModelRequest.from_dict(internal_handler_create_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


