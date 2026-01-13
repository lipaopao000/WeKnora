# InternalHandlerGetSystemInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_time** | **str** |  | [optional] 
**commit_id** | **str** |  | [optional] 
**go_version** | **str** |  | [optional] 
**graph_database_engine** | **str** |  | [optional] 
**keyword_index_engine** | **str** |  | [optional] 
**minio_enabled** | **bool** |  | [optional] 
**vector_store_engine** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from weknora.models.internal_handler_get_system_info_response import InternalHandlerGetSystemInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerGetSystemInfoResponse from a JSON string
internal_handler_get_system_info_response_instance = InternalHandlerGetSystemInfoResponse.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerGetSystemInfoResponse.to_json())

# convert the object into a dict
internal_handler_get_system_info_response_dict = internal_handler_get_system_info_response_instance.to_dict()
# create an instance of InternalHandlerGetSystemInfoResponse from a dict
internal_handler_get_system_info_response_from_dict = InternalHandlerGetSystemInfoResponse.from_dict(internal_handler_get_system_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


