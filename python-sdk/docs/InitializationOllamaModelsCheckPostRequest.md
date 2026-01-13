# InitializationOllamaModelsCheckPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **List[str]** |  | [optional] 

## Example

```python
from weknora.models.initialization_ollama_models_check_post_request import InitializationOllamaModelsCheckPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InitializationOllamaModelsCheckPostRequest from a JSON string
initialization_ollama_models_check_post_request_instance = InitializationOllamaModelsCheckPostRequest.from_json(json)
# print the JSON string representation of the object
print(InitializationOllamaModelsCheckPostRequest.to_json())

# convert the object into a dict
initialization_ollama_models_check_post_request_dict = initialization_ollama_models_check_post_request_instance.to_dict()
# create an instance of InitializationOllamaModelsCheckPostRequest from a dict
initialization_ollama_models_check_post_request_from_dict = InitializationOllamaModelsCheckPostRequest.from_dict(initialization_ollama_models_check_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


