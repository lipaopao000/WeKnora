# GithubComTencentWeKnoraInternalTypesKnowledgeBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_count** | **int** | Chunk count (not stored in database, calculated on query) | [optional] 
**chunking_config** | [**GithubComTencentWeKnoraInternalTypesChunkingConfig**](GithubComTencentWeKnoraInternalTypesChunkingConfig.md) | Chunking configuration | [optional] 
**cos_config** | [**GithubComTencentWeKnoraInternalTypesStorageConfig**](GithubComTencentWeKnoraInternalTypesStorageConfig.md) | Storage config | [optional] 
**created_at** | **str** | Creation time of the knowledge base | [optional] 
**deleted_at** | [**GormDeletedAt**](GormDeletedAt.md) | Deletion time of the knowledge base | [optional] 
**description** | **str** | Description of the knowledge base | [optional] 
**embedding_model_id** | **str** | ID of the embedding model | [optional] 
**extract_config** | [**GithubComTencentWeKnoraInternalTypesExtractConfig**](GithubComTencentWeKnoraInternalTypesExtractConfig.md) | Extract config | [optional] 
**faq_config** | [**GithubComTencentWeKnoraInternalTypesFAQConfig**](GithubComTencentWeKnoraInternalTypesFAQConfig.md) | FAQConfig stores FAQ specific configuration such as indexing strategy | [optional] 
**id** | **str** | Unique identifier of the knowledge base | [optional] 
**image_processing_config** | [**GithubComTencentWeKnoraInternalTypesImageProcessingConfig**](GithubComTencentWeKnoraInternalTypesImageProcessingConfig.md) | Image processing configuration | [optional] 
**is_processing** | **bool** | IsProcessing indicates if there is a processing import task (for FAQ type knowledge bases) | [optional] 
**is_temporary** | **bool** | Whether this knowledge base is temporary (ephemeral) and should be hidden from UI | [optional] 
**knowledge_count** | **int** | Knowledge count (not stored in database, calculated on query) | [optional] 
**name** | **str** | Name of the knowledge base | [optional] 
**processing_count** | **int** | ProcessingCount indicates the number of knowledge items being processed (for document type knowledge bases) | [optional] 
**question_generation_config** | [**GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig**](GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig.md) | QuestionGenerationConfig stores question generation configuration for document knowledge bases | [optional] 
**summary_model_id** | **str** | Summary model ID | [optional] 
**tenant_id** | **int** | Tenant ID | [optional] 
**type** | **str** | Type of the knowledge base (document, faq, etc.) | [optional] 
**updated_at** | **str** | Last updated time of the knowledge base | [optional] 
**vlm_config** | [**GithubComTencentWeKnoraInternalTypesVLMConfig**](GithubComTencentWeKnoraInternalTypesVLMConfig.md) | VLM config | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_knowledge_base import GithubComTencentWeKnoraInternalTypesKnowledgeBase

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesKnowledgeBase from a JSON string
github_com_tencent_we_knora_internal_types_knowledge_base_instance = GithubComTencentWeKnoraInternalTypesKnowledgeBase.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesKnowledgeBase.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_knowledge_base_dict = github_com_tencent_we_knora_internal_types_knowledge_base_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesKnowledgeBase from a dict
github_com_tencent_we_knora_internal_types_knowledge_base_from_dict = GithubComTencentWeKnoraInternalTypesKnowledgeBase.from_dict(github_com_tencent_we_knora_internal_types_knowledge_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


