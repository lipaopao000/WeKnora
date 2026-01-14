# GithubComTencentWeKnoraInternalTypesRegisterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**tenant** | [**GithubComTencentWeKnoraInternalTypesTenant**](GithubComTencentWeKnoraInternalTypesTenant.md) |  | [optional] 
**user** | [**GithubComTencentWeKnoraInternalTypesUser**](GithubComTencentWeKnoraInternalTypesUser.md) |  | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_register_response import GithubComTencentWeKnoraInternalTypesRegisterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesRegisterResponse from a JSON string
github_com_tencent_we_knora_internal_types_register_response_instance = GithubComTencentWeKnoraInternalTypesRegisterResponse.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesRegisterResponse.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_register_response_dict = github_com_tencent_we_knora_internal_types_register_response_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesRegisterResponse from a dict
github_com_tencent_we_knora_internal_types_register_response_from_dict = GithubComTencentWeKnoraInternalTypesRegisterResponse.from_dict(github_com_tencent_we_knora_internal_types_register_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


