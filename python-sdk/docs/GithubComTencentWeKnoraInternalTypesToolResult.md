# GithubComTencentWeKnoraInternalTypesToolResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Dict[str, object]** | Structured data for programmatic use | [optional] 
**error** | **str** | Error message if execution failed | [optional] 
**output** | **str** | Human-readable output | [optional] 
**success** | **bool** | Whether the tool executed successfully | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_tool_result import GithubComTencentWeKnoraInternalTypesToolResult

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesToolResult from a JSON string
github_com_tencent_we_knora_internal_types_tool_result_instance = GithubComTencentWeKnoraInternalTypesToolResult.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesToolResult.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_tool_result_dict = github_com_tencent_we_knora_internal_types_tool_result_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesToolResult from a dict
github_com_tencent_we_knora_internal_types_tool_result_from_dict = GithubComTencentWeKnoraInternalTypesToolResult.from_dict(github_com_tencent_we_knora_internal_types_tool_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


