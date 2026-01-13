# GithubComTencentWeKnoraInternalTypesLoginResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 
**tenant** | [**GithubComTencentWeKnoraInternalTypesTenant**](GithubComTencentWeKnoraInternalTypesTenant.md) |  | [optional] 
**token** | **str** |  | [optional] 
**user** | [**GithubComTencentWeKnoraInternalTypesUser**](GithubComTencentWeKnoraInternalTypesUser.md) |  | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_login_response import GithubComTencentWeKnoraInternalTypesLoginResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesLoginResponse from a JSON string
github_com_tencent_we_knora_internal_types_login_response_instance = GithubComTencentWeKnoraInternalTypesLoginResponse.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesLoginResponse.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_login_response_dict = github_com_tencent_we_knora_internal_types_login_response_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesLoginResponse from a dict
github_com_tencent_we_knora_internal_types_login_response_from_dict = GithubComTencentWeKnoraInternalTypesLoginResponse.from_dict(github_com_tencent_we_knora_internal_types_login_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


