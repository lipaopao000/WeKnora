# InternalHandlerUpdateChunkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_index** | **int** |  | [optional] 
**content** | **str** |  | [optional] 
**embedding** | **List[float]** |  | [optional] 
**end_at** | **int** |  | [optional] 
**image_info** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**start_at** | **int** |  | [optional] 

## Example

```python
from weknora.models.internal_handler_update_chunk_request import InternalHandlerUpdateChunkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerUpdateChunkRequest from a JSON string
internal_handler_update_chunk_request_instance = InternalHandlerUpdateChunkRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerUpdateChunkRequest.to_json())

# convert the object into a dict
internal_handler_update_chunk_request_dict = internal_handler_update_chunk_request_instance.to_dict()
# create an instance of InternalHandlerUpdateChunkRequest from a dict
internal_handler_update_chunk_request_from_dict = InternalHandlerUpdateChunkRequest.from_dict(internal_handler_update_chunk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


