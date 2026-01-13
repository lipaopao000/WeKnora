# GithubComTencentWeKnoraInternalTypesToolCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **Dict[str, object]** | Tool arguments | [optional] 
**duration** | **int** | Execution time in milliseconds | [optional] 
**id** | **str** | Function call ID from LLM | [optional] 
**name** | **str** | Tool name | [optional] 
**reflection** | **str** | Agent&#39;s reflection on this tool call result (if enabled) | [optional] 
**result** | [**GithubComTencentWeKnoraInternalTypesToolResult**](GithubComTencentWeKnoraInternalTypesToolResult.md) | Execution result (contains Output) | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_tool_call import GithubComTencentWeKnoraInternalTypesToolCall

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesToolCall from a JSON string
github_com_tencent_we_knora_internal_types_tool_call_instance = GithubComTencentWeKnoraInternalTypesToolCall.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesToolCall.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_tool_call_dict = github_com_tencent_we_knora_internal_types_tool_call_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesToolCall from a dict
github_com_tencent_we_knora_internal_types_tool_call_from_dict = GithubComTencentWeKnoraInternalTypesToolCall.from_dict(github_com_tencent_we_knora_internal_types_tool_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


