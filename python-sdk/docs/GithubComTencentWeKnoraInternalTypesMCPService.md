# GithubComTencentWeKnoraInternalTypesMCPService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_config** | [**GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig**](GithubComTencentWeKnoraInternalTypesMCPAdvancedConfig.md) |  | [optional] 
**auth_config** | [**GithubComTencentWeKnoraInternalTypesMCPAuthConfig**](GithubComTencentWeKnoraInternalTypesMCPAuthConfig.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**deleted_at** | [**GormDeletedAt**](GormDeletedAt.md) |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**env_vars** | **Dict[str, str]** | Environment variables for stdio | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**stdio_config** | [**GithubComTencentWeKnoraInternalTypesMCPStdioConfig**](GithubComTencentWeKnoraInternalTypesMCPStdioConfig.md) | Required for stdio transport | [optional] 
**tenant_id** | **int** |  | [optional] 
**transport_type** | [**GithubComTencentWeKnoraInternalTypesMCPTransportType**](GithubComTencentWeKnoraInternalTypesMCPTransportType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** | Optional: required for SSE/HTTP Streamable | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_mcp_service import GithubComTencentWeKnoraInternalTypesMCPService

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesMCPService from a JSON string
github_com_tencent_we_knora_internal_types_mcp_service_instance = GithubComTencentWeKnoraInternalTypesMCPService.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesMCPService.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_mcp_service_dict = github_com_tencent_we_knora_internal_types_mcp_service_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesMCPService from a dict
github_com_tencent_we_knora_internal_types_mcp_service_from_dict = GithubComTencentWeKnoraInternalTypesMCPService.from_dict(github_com_tencent_we_knora_internal_types_mcp_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


