# GithubComTencentWeKnoraInternalTypesSessionAgentConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_mode_enabled** | **bool** | Whether agent mode is enabled for this session | [optional] 
**knowledge_bases** | **List[str]** | Accessible knowledge base IDs for this session | [optional] 
**knowledge_ids** | **List[str]** | Accessible knowledge IDs (individual documents) for this session | [optional] 
**web_search_enabled** | **bool** | Whether web search is enabled for this session | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_session_agent_config import GithubComTencentWeKnoraInternalTypesSessionAgentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesSessionAgentConfig from a JSON string
github_com_tencent_we_knora_internal_types_session_agent_config_instance = GithubComTencentWeKnoraInternalTypesSessionAgentConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesSessionAgentConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_session_agent_config_dict = github_com_tencent_we_knora_internal_types_session_agent_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesSessionAgentConfig from a dict
github_com_tencent_we_knora_internal_types_session_agent_config_from_dict = GithubComTencentWeKnoraInternalTypesSessionAgentConfig.from_dict(github_com_tencent_we_knora_internal_types_session_agent_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


