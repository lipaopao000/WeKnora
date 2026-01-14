# GithubComTencentWeKnoraInternalTypesExtractConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**nodes** | [**List[GithubComTencentWeKnoraInternalTypesGraphNode]**](GithubComTencentWeKnoraInternalTypesGraphNode.md) |  | [optional] 
**relations** | [**List[GithubComTencentWeKnoraInternalTypesGraphRelation]**](GithubComTencentWeKnoraInternalTypesGraphRelation.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_extract_config import GithubComTencentWeKnoraInternalTypesExtractConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesExtractConfig from a JSON string
github_com_tencent_we_knora_internal_types_extract_config_instance = GithubComTencentWeKnoraInternalTypesExtractConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesExtractConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_extract_config_dict = github_com_tencent_we_knora_internal_types_extract_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesExtractConfig from a dict
github_com_tencent_we_knora_internal_types_extract_config_from_dict = GithubComTencentWeKnoraInternalTypesExtractConfig.from_dict(github_com_tencent_we_knora_internal_types_extract_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


