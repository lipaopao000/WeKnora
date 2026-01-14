# GithubComTencentWeKnoraInternalTypesTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_config** | [**GithubComTencentWeKnoraInternalTypesAgentConfig**](GithubComTencentWeKnoraInternalTypesAgentConfig.md) | Global Agent configuration for this tenant (default for all sessions) | [optional] 
**api_key** | **str** | API key | [optional] 
**business** | **str** | Business | [optional] 
**context_config** | [**GithubComTencentWeKnoraInternalTypesContextConfig**](GithubComTencentWeKnoraInternalTypesContextConfig.md) | Global Context configuration for this tenant (default for all sessions) | [optional] 
**conversation_config** | [**GithubComTencentWeKnoraInternalTypesConversationConfig**](GithubComTencentWeKnoraInternalTypesConversationConfig.md) | Global Conversation configuration for this tenant (default for normal mode sessions) | [optional] 
**created_at** | **str** | Creation time | [optional] 
**deleted_at** | [**GormDeletedAt**](GormDeletedAt.md) | Deletion time | [optional] 
**description** | **str** | Description | [optional] 
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**retriever_engines** | [**GithubComTencentWeKnoraInternalTypesRetrieverEngines**](GithubComTencentWeKnoraInternalTypesRetrieverEngines.md) | Retriever engines | [optional] 
**status** | **str** | Status | [optional] 
**storage_quota** | **int** | Storage quota (Bytes), default is 10GB, including vector, original file, text, index, etc. | [optional] 
**storage_used** | **int** | Storage used (Bytes) | [optional] 
**updated_at** | **str** | Last updated time | [optional] 
**web_search_config** | [**GithubComTencentWeKnoraInternalTypesWebSearchConfig**](GithubComTencentWeKnoraInternalTypesWebSearchConfig.md) | Global WebSearch configuration for this tenant | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_tenant import GithubComTencentWeKnoraInternalTypesTenant

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesTenant from a JSON string
github_com_tencent_we_knora_internal_types_tenant_instance = GithubComTencentWeKnoraInternalTypesTenant.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesTenant.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_tenant_dict = github_com_tencent_we_knora_internal_types_tenant_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesTenant from a dict
github_com_tencent_we_knora_internal_types_tenant_from_dict = GithubComTencentWeKnoraInternalTypesTenant.from_dict(github_com_tencent_we_knora_internal_types_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


