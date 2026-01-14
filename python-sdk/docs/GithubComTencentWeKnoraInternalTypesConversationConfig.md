# GithubComTencentWeKnoraInternalTypesConversationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_template** | **str** | ContextTemplate is the prompt template for summarizing retrieval results | [optional] 
**embedding_top_k** | **int** |  | [optional] 
**enable_query_expansion** | **bool** |  | [optional] 
**enable_rewrite** | **bool** |  | [optional] 
**fallback_prompt** | **str** |  | [optional] 
**fallback_response** | **str** |  | [optional] 
**fallback_strategy** | **str** | Fallback strategy | [optional] 
**keyword_threshold** | **float** |  | [optional] 
**max_completion_tokens** | **int** | MaxTokens is the maximum number of tokens to generate | [optional] 
**max_rounds** | **int** | Retrieval &amp; strategy parameters | [optional] 
**prompt** | **str** |  | [optional] 
**rerank_model_id** | **str** |  | [optional] 
**rerank_threshold** | **float** |  | [optional] 
**rerank_top_k** | **int** |  | [optional] 
**rewrite_prompt_system** | **str** | Rewrite prompts | [optional] 
**rewrite_prompt_user** | **str** |  | [optional] 
**summary_model_id** | **str** | Model configuration | [optional] 
**temperature** | **float** | Temperature controls the randomness of the model output | [optional] 
**use_custom_context_template** | **bool** |  | [optional] 
**use_custom_system_prompt** | **bool** | Prompt is the system prompt for normal mode | [optional] 
**vector_threshold** | **float** |  | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_conversation_config import GithubComTencentWeKnoraInternalTypesConversationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesConversationConfig from a JSON string
github_com_tencent_we_knora_internal_types_conversation_config_instance = GithubComTencentWeKnoraInternalTypesConversationConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesConversationConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_conversation_config_dict = github_com_tencent_we_knora_internal_types_conversation_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesConversationConfig from a dict
github_com_tencent_we_knora_internal_types_conversation_config_from_dict = GithubComTencentWeKnoraInternalTypesConversationConfig.from_dict(github_com_tencent_we_knora_internal_types_conversation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


