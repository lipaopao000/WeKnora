# GithubComTencentWeKnoraInternalTypesKnowledge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Creation time of the knowledge | [optional] 
**deleted_at** | [**GormDeletedAt**](GormDeletedAt.md) | Deletion time of the knowledge | [optional] 
**description** | **str** | Description of the knowledge | [optional] 
**embedding_model_id** | **str** | ID of the embedding model | [optional] 
**enable_status** | **str** | Enable status of the knowledge | [optional] 
**error_message** | **str** | Error message of the knowledge | [optional] 
**file_hash** | **str** | File hash of the knowledge | [optional] 
**file_name** | **str** | File name of the knowledge | [optional] 
**file_path** | **str** | File path of the knowledge | [optional] 
**file_size** | **int** | File size of the knowledge | [optional] 
**file_type** | **str** | File type of the knowledge | [optional] 
**id** | **str** | Unique identifier of the knowledge | [optional] 
**knowledge_base_id** | **str** | ID of the knowledge base | [optional] 
**knowledge_base_name** | **str** | Knowledge base name (not stored in database, populated on query) | [optional] 
**metadata** | **List[int]** | Metadata of the knowledge | [optional] 
**parse_status** | **str** | Parse status of the knowledge | [optional] 
**processed_at** | **str** | Processed time of the knowledge | [optional] 
**source** | **str** | Source of the knowledge | [optional] 
**storage_size** | **int** | Storage size of the knowledge | [optional] 
**summary_status** | **str** | Summary status for async summary generation | [optional] 
**tag_id** | **str** | Optional tag ID for categorization within a knowledge base | [optional] 
**tenant_id** | **int** | Tenant ID | [optional] 
**title** | **str** | Title of the knowledge | [optional] 
**type** | **str** | Type of the knowledge | [optional] 
**updated_at** | **str** | Last updated time of the knowledge | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_knowledge import GithubComTencentWeKnoraInternalTypesKnowledge

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesKnowledge from a JSON string
github_com_tencent_we_knora_internal_types_knowledge_instance = GithubComTencentWeKnoraInternalTypesKnowledge.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesKnowledge.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_knowledge_dict = github_com_tencent_we_knora_internal_types_knowledge_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesKnowledge from a dict
github_com_tencent_we_knora_internal_types_knowledge_from_dict = GithubComTencentWeKnoraInternalTypesKnowledge.from_dict(github_com_tencent_we_knora_internal_types_knowledge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


