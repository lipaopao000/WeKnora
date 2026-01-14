# GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry_count** | **int** | Number of retries, default: 3 | [optional] 
**retry_delay** | **int** | Delay between retries in seconds, default: 1 | [optional] 
**timeout** | **int** | Timeout in seconds, default: 30 | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_mcp_advanced_config import GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig from a JSON string
github_com_tencent_we_knora_internal_types_mcp_advanced_config_instance = GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_mcp_advanced_config_dict = github_com_tencent_we_knora_internal_types_mcp_advanced_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig from a dict
github_com_tencent_we_knora_internal_types_mcp_advanced_config_from_dict = GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig.from_dict(github_com_tencent_we_knora_internal_types_mcp_advanced_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


