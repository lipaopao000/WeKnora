# GithubComTencentWeKnoraInternalTypesContextConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression_strategy** | [**GithubComTencentWeKnoraInternalTypesContextCompressionStrategy**](GithubComTencentWeKnoraInternalTypesContextCompressionStrategy.md) | Compression strategy: \&quot;sliding_window\&quot; or \&quot;smart\&quot; | [optional] 
**max_tokens** | **int** | Maximum tokens allowed in LLM context | [optional] 
**recent_message_count** | **int** | For sliding_window: number of messages to keep For smart: number of recent messages to keep uncompressed | [optional] 
**summarize_threshold** | **int** | Summarize threshold: number of messages before summarization | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_context_config import GithubComTencentWeKnoraInternalTypesContextConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesContextConfig from a JSON string
github_com_tencent_we_knora_internal_types_context_config_instance = GithubComTencentWeKnoraInternalTypesContextConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesContextConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_context_config_dict = github_com_tencent_we_knora_internal_types_context_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesContextConfig from a dict
github_com_tencent_we_knora_internal_types_context_config_from_dict = GithubComTencentWeKnoraInternalTypesContextConfig.from_dict(github_com_tencent_we_knora_internal_types_context_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


