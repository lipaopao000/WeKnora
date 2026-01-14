# GithubComTencentWeKnoraInternalTypesStorageConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | App ID | [optional] 
**bucket_name** | **str** | Bucket Name | [optional] 
**path_prefix** | **str** | Path Prefix | [optional] 
**provider** | **str** | Provider | [optional] 
**region** | **str** | Region | [optional] 
**secret_id** | **str** | Secret ID | [optional] 
**secret_key** | **str** | Secret Key | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_storage_config import GithubComTencentWeKnoraInternalTypesStorageConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesStorageConfig from a JSON string
github_com_tencent_we_knora_internal_types_storage_config_instance = GithubComTencentWeKnoraInternalTypesStorageConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesStorageConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_storage_config_dict = github_com_tencent_we_knora_internal_types_storage_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesStorageConfig from a dict
github_com_tencent_we_knora_internal_types_storage_config_from_dict = GithubComTencentWeKnoraInternalTypesStorageConfig.from_dict(github_com_tencent_we_knora_internal_types_storage_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


