# GithubComTencentWeKnoraInternalTypesVLMConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API Key | [optional] 
**base_url** | **str** | Base URL | [optional] 
**enabled** | **bool** |  | [optional] 
**interface_type** | **str** | Interface Type: \&quot;ollama\&quot; or \&quot;openai\&quot; | [optional] 
**model_id** | **str** |  | [optional] 
**model_name** | **str** | 兼容老版本 Model Name | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_vlm_config import GithubComTencentWeKnoraInternalTypesVLMConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesVLMConfig from a JSON string
github_com_tencent_we_knora_internal_types_vlm_config_instance = GithubComTencentWeKnoraInternalTypesVLMConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesVLMConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_vlm_config_dict = github_com_tencent_we_knora_internal_types_vlm_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesVLMConfig from a dict
github_com_tencent_we_knora_internal_types_vlm_config_from_dict = GithubComTencentWeKnoraInternalTypesVLMConfig.from_dict(github_com_tencent_we_knora_internal_types_vlm_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


