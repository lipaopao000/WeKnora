# GithubComTencentWeKnoraInternalTypesChunkingConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_overlap** | **int** | Chunk overlap | [optional] 
**chunk_size** | **int** | Chunk size | [optional] 
**enable_multimodal** | **bool** | EnableMultimodal (deprecated, kept for backward compatibility with old data) | [optional] 
**separators** | **List[str]** | Separators | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_chunking_config import GithubComTencentWeKnoraInternalTypesChunkingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesChunkingConfig from a JSON string
github_com_tencent_we_knora_internal_types_chunking_config_instance = GithubComTencentWeKnoraInternalTypesChunkingConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesChunkingConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_chunking_config_dict = github_com_tencent_we_knora_internal_types_chunking_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesChunkingConfig from a dict
github_com_tencent_we_knora_internal_types_chunking_config_from_dict = GithubComTencentWeKnoraInternalTypesChunkingConfig.from_dict(github_com_tencent_we_knora_internal_types_chunking_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


