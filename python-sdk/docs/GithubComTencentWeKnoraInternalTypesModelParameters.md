# GithubComTencentWeKnoraInternalTypesModelParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**base_url** | **str** |  | [optional] 
**embedding_parameters** | [**GithubComTencentWeKnoraInternalTypesEmbeddingParameters**](GithubComTencentWeKnoraInternalTypesEmbeddingParameters.md) |  | [optional] 
**interface_type** | **str** |  | [optional] 
**parameter_size** | **str** | Ollama model parameter size (e.g., \&quot;7B\&quot;, \&quot;13B\&quot;, \&quot;70B\&quot;) | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_model_parameters import GithubComTencentWeKnoraInternalTypesModelParameters

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesModelParameters from a JSON string
github_com_tencent_we_knora_internal_types_model_parameters_instance = GithubComTencentWeKnoraInternalTypesModelParameters.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesModelParameters.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_model_parameters_dict = github_com_tencent_we_knora_internal_types_model_parameters_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesModelParameters from a dict
github_com_tencent_we_knora_internal_types_model_parameters_from_dict = GithubComTencentWeKnoraInternalTypesModelParameters.from_dict(github_com_tencent_we_knora_internal_types_model_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


