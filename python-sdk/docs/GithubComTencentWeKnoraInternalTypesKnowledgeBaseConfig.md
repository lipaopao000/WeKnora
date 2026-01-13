# GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunking_config** | [**GithubComTencentWeKnoraInternalTypesChunkingConfig**](GithubComTencentWeKnoraInternalTypesChunkingConfig.md) | Chunking configuration | [optional] 
**faq_config** | [**GithubComTencentWeKnoraInternalTypesFAQConfig**](GithubComTencentWeKnoraInternalTypesFAQConfig.md) | FAQ configuration (only for FAQ type knowledge bases) | [optional] 
**image_processing_config** | [**GithubComTencentWeKnoraInternalTypesImageProcessingConfig**](GithubComTencentWeKnoraInternalTypesImageProcessingConfig.md) | Image processing configuration | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_knowledge_base_config import GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig from a JSON string
github_com_tencent_we_knora_internal_types_knowledge_base_config_instance = GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_knowledge_base_config_dict = github_com_tencent_we_knora_internal_types_knowledge_base_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig from a dict
github_com_tencent_we_knora_internal_types_knowledge_base_config_from_dict = GithubComTencentWeKnoraInternalTypesKnowledgeBaseConfig.from_dict(github_com_tencent_we_knora_internal_types_knowledge_base_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


