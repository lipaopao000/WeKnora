# GithubComTencentWeKnoraInternalTypesSummaryConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_template** | **str** | Context template | [optional] 
**frequency_penalty** | **float** | Frequency penalty | [optional] 
**max_completion_tokens** | **int** | Max completion tokens | [optional] 
**max_tokens** | **int** | Max tokens | [optional] 
**no_match_prefix** | **str** | No match prefix | [optional] 
**presence_penalty** | **float** | Presence penalty | [optional] 
**prompt** | **str** | Prompt | [optional] 
**repeat_penalty** | **float** | Repeat penalty | [optional] 
**seed** | **int** | Seed | [optional] 
**temperature** | **float** | Temperature | [optional] 
**top_k** | **int** | TopK | [optional] 
**top_p** | **float** | TopP | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_summary_config import GithubComTencentWeKnoraInternalTypesSummaryConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesSummaryConfig from a JSON string
github_com_tencent_we_knora_internal_types_summary_config_instance = GithubComTencentWeKnoraInternalTypesSummaryConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesSummaryConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_summary_config_dict = github_com_tencent_we_knora_internal_types_summary_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesSummaryConfig from a dict
github_com_tencent_we_knora_internal_types_summary_config_from_dict = GithubComTencentWeKnoraInternalTypesSummaryConfig.from_dict(github_com_tencent_we_knora_internal_types_summary_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


