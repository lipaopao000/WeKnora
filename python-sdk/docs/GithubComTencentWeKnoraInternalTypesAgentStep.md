# GithubComTencentWeKnoraInternalTypesAgentStep


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iteration** | **int** | Iteration number (0-indexed) | [optional] 
**thought** | **str** | LLM&#39;s reasoning/thinking (Think phase) | [optional] 
**timestamp** | **str** | When this step occurred | [optional] 
**tool_calls** | [**List[GithubComTencentWeKnoraInternalTypesToolCall]**](GithubComTencentWeKnoraInternalTypesToolCall.md) | Tools called in this step (Act phase) | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_agent_step import GithubComTencentWeKnoraInternalTypesAgentStep

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesAgentStep from a JSON string
github_com_tencent_we_knora_internal_types_agent_step_instance = GithubComTencentWeKnoraInternalTypesAgentStep.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesAgentStep.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_agent_step_dict = github_com_tencent_we_knora_internal_types_agent_step_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesAgentStep from a dict
github_com_tencent_we_knora_internal_types_agent_step_from_dict = GithubComTencentWeKnoraInternalTypesAgentStep.from_dict(github_com_tencent_we_knora_internal_types_agent_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


