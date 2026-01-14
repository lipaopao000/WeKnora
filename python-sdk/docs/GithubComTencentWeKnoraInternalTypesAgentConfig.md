# GithubComTencentWeKnoraInternalTypesAgentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_tools** | **List[str]** | List of allowed tool names | [optional] 
**knowledge_bases** | **List[str]** | Accessible knowledge base IDs | [optional] 
**knowledge_ids** | **List[str]** | Accessible knowledge IDs (individual documents) | [optional] 
**max_iterations** | **int** | Maximum number of ReAct iterations | [optional] 
**reflection_enabled** | **bool** | Whether to enable reflection | [optional] 
**system_prompt_web_disabled** | **str** | Custom prompt when web search is disabled | [optional] 
**system_prompt_web_enabled** | **str** | Custom prompt when web search is enabled | [optional] 
**temperature** | **float** | LLM temperature for agent | [optional] 
**use_custom_system_prompt** | **bool** | Whether to use custom system prompt instead of default | [optional] 
**web_search_enabled** | **bool** | Whether web search tool is enabled | [optional] 
**web_search_max_results** | **int** | Maximum number of web search results (default: 5) | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_agent_config import GithubComTencentWeKnoraInternalTypesAgentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesAgentConfig from a JSON string
github_com_tencent_we_knora_internal_types_agent_config_instance = GithubComTencentWeKnoraInternalTypesAgentConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesAgentConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_agent_config_dict = github_com_tencent_we_knora_internal_types_agent_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesAgentConfig from a dict
github_com_tencent_we_knora_internal_types_agent_config_from_dict = GithubComTencentWeKnoraInternalTypesAgentConfig.from_dict(github_com_tencent_we_knora_internal_types_agent_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


