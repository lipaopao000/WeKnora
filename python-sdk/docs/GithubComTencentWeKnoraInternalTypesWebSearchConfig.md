# GithubComTencentWeKnoraInternalTypesWebSearchConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API密钥（如果需要） | [optional] 
**blacklist** | **List[str]** | 黑名单规则列表 | [optional] 
**compression_method** | **str** | 压缩方法：none, summary, extract, rag | [optional] 
**document_fragments** | **int** | 文档片段数量（用于RAG压缩） | [optional] 
**embedding_dimension** | **int** | 嵌入维度（用于RAG压缩） | [optional] 
**embedding_model_id** | **str** | RAG压缩相关配置 | [optional] 
**include_date** | **bool** | 是否包含日期 | [optional] 
**max_results** | **int** | 最大搜索结果数 | [optional] 
**provider** | **str** | 搜索引擎提供商ID | [optional] 
**rerank_model_id** | **str** | 重排模型ID（用于RAG压缩） | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_web_search_config import GithubComTencentWeKnoraInternalTypesWebSearchConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesWebSearchConfig from a JSON string
github_com_tencent_we_knora_internal_types_web_search_config_instance = GithubComTencentWeKnoraInternalTypesWebSearchConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesWebSearchConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_web_search_config_dict = github_com_tencent_we_knora_internal_types_web_search_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesWebSearchConfig from a dict
github_com_tencent_we_knora_internal_types_web_search_config_from_dict = GithubComTencentWeKnoraInternalTypesWebSearchConfig.from_dict(github_com_tencent_we_knora_internal_types_web_search_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


