# GithubComTencentWeKnoraInternalTypesSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_config** | [**GithubComTencentWeKnoraInternalTypesSessionAgentConfig**](GithubComTencentWeKnoraInternalTypesSessionAgentConfig.md) | Agent 配置（会话级别，仅存储enabled和knowledge_bases） | [optional] 
**context_config** | [**GithubComTencentWeKnoraInternalTypesContextConfig**](GithubComTencentWeKnoraInternalTypesContextConfig.md) | 上下文管理配置（可选） | [optional] 
**created_at** | **str** |  | [optional] 
**deleted_at** | [**GormDeletedAt**](GormDeletedAt.md) |  | [optional] 
**description** | **str** | Description | [optional] 
**embedding_top_k** | **int** | 向量召回TopK | [optional] 
**enable_rewrite** | **bool** | 多轮改写开关 | [optional] 
**fallback_response** | **str** | 固定回复内容 | [optional] 
**fallback_strategy** | [**GithubComTencentWeKnoraInternalTypesFallbackStrategy**](GithubComTencentWeKnoraInternalTypesFallbackStrategy.md) | 兜底策略 | [optional] 
**id** | **str** | ID | [optional] 
**keyword_threshold** | **float** | 关键词召回阈值 | [optional] 
**knowledge_base_id** | **str** | Strategy configuration | [optional] 
**max_rounds** | **int** | 多轮保持轮数 | [optional] 
**rerank_model_id** | **str** | 排序模型ID | [optional] 
**rerank_threshold** | **float** | 排序阈值 | [optional] 
**rerank_top_k** | **int** | 排序TopK | [optional] 
**summary_model_id** | **str** | 总结模型ID | [optional] 
**summary_parameters** | [**GithubComTencentWeKnoraInternalTypesSummaryConfig**](GithubComTencentWeKnoraInternalTypesSummaryConfig.md) | 总结模型参数 | [optional] 
**tenant_id** | **int** | Tenant ID | [optional] 
**title** | **str** | Title | [optional] 
**updated_at** | **str** |  | [optional] 
**vector_threshold** | **float** | 向量召回阈值 | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_session import GithubComTencentWeKnoraInternalTypesSession

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesSession from a JSON string
github_com_tencent_we_knora_internal_types_session_instance = GithubComTencentWeKnoraInternalTypesSession.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesSession.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_session_dict = github_com_tencent_we_knora_internal_types_session_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesSession from a dict
github_com_tencent_we_knora_internal_types_session_from_dict = GithubComTencentWeKnoraInternalTypesSession.from_dict(github_com_tencent_we_knora_internal_types_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


