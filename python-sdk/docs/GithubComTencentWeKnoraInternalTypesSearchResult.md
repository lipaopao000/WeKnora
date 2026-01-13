# GithubComTencentWeKnoraInternalTypesSearchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_index** | **int** | Chunk index | [optional] 
**chunk_metadata** | **List[int]** | ChunkMetadata stores chunk-level metadata (e.g., generated questions) | [optional] 
**chunk_type** | **str** | Chunk 类型 | [optional] 
**content** | **str** | Content | [optional] 
**end_at** | **int** | End at | [optional] 
**id** | **str** | ID | [optional] 
**image_info** | **str** | 图片信息 (JSON 格式) | [optional] 
**knowledge_filename** | **str** | Knowledge file name Used for file type knowledge, contains the original file name | [optional] 
**knowledge_id** | **str** | Knowledge ID | [optional] 
**knowledge_source** | **str** | Knowledge source Used to indicate the source of the knowledge, such as \&quot;url\&quot; | [optional] 
**knowledge_title** | **str** | Knowledge title | [optional] 
**match_type** | [**GithubComTencentWeKnoraInternalTypesMatchType**](GithubComTencentWeKnoraInternalTypesMatchType.md) | Match type | [optional] 
**metadata** | **Dict[str, str]** | Metadata | [optional] 
**parent_chunk_id** | **str** | 父 Chunk ID | [optional] 
**score** | **float** | Score | [optional] 
**seq** | **int** | Seq | [optional] 
**start_at** | **int** | Start at | [optional] 
**sub_chunk_id** | **List[str]** | SubChunkIndex | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_search_result import GithubComTencentWeKnoraInternalTypesSearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesSearchResult from a JSON string
github_com_tencent_we_knora_internal_types_search_result_instance = GithubComTencentWeKnoraInternalTypesSearchResult.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesSearchResult.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_search_result_dict = github_com_tencent_we_knora_internal_types_search_result_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesSearchResult from a dict
github_com_tencent_we_knora_internal_types_search_result_from_dict = GithubComTencentWeKnoraInternalTypesSearchResult.from_dict(github_com_tencent_we_knora_internal_types_search_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


