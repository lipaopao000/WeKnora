# InternalHandlerLLMConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**base_url** | **str** |  | [optional] 
**model_name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from weknora.models.internal_handler_llm_config import InternalHandlerLLMConfig

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerLLMConfig from a JSON string
internal_handler_llm_config_instance = InternalHandlerLLMConfig.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerLLMConfig.to_json())

# convert the object into a dict
internal_handler_llm_config_dict = internal_handler_llm_config_instance.to_dict()
# create an instance of InternalHandlerLLMConfig from a dict
internal_handler_llm_config_from_dict = InternalHandlerLLMConfig.from_dict(internal_handler_llm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


