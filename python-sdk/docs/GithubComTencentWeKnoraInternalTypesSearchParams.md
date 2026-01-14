# GithubComTencentWeKnoraInternalTypesSearchParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_keywords_match** | **bool** |  | [optional] 
**disable_vector_match** | **bool** |  | [optional] 
**keyword_threshold** | **float** |  | [optional] 
**knowledge_ids** | **List[str]** |  | [optional] 
**match_count** | **int** |  | [optional] 
**query_text** | **str** |  | [optional] 
**vector_threshold** | **float** |  | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_search_params import GithubComTencentWeKnoraInternalTypesSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesSearchParams from a JSON string
github_com_tencent_we_knora_internal_types_search_params_instance = GithubComTencentWeKnoraInternalTypesSearchParams.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesSearchParams.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_search_params_dict = github_com_tencent_we_knora_internal_types_search_params_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesSearchParams from a dict
github_com_tencent_we_knora_internal_types_search_params_from_dict = GithubComTencentWeKnoraInternalTypesSearchParams.from_dict(github_com_tencent_we_knora_internal_types_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


