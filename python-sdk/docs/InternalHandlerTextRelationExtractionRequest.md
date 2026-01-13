# InternalHandlerTextRelationExtractionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**llm_config** | [**InternalHandlerLLMConfig**](InternalHandlerLLMConfig.md) |  | [optional] 
**tags** | **List[str]** |  | 
**text** | **str** |  | 

## Example

```python
from weknora.models.internal_handler_text_relation_extraction_request import InternalHandlerTextRelationExtractionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerTextRelationExtractionRequest from a JSON string
internal_handler_text_relation_extraction_request_instance = InternalHandlerTextRelationExtractionRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerTextRelationExtractionRequest.to_json())

# convert the object into a dict
internal_handler_text_relation_extraction_request_dict = internal_handler_text_relation_extraction_request_instance.to_dict()
# create an instance of InternalHandlerTextRelationExtractionRequest from a dict
internal_handler_text_relation_extraction_request_from_dict = InternalHandlerTextRelationExtractionRequest.from_dict(internal_handler_text_relation_extraction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


