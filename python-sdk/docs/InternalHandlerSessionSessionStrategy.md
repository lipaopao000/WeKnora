# InternalHandlerSessionSessionStrategy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding_top_k** | **int** | Number of top results to retrieve from vector search | [optional] 
**enable_rewrite** | **bool** | Whether to enable query rewrite for multi-round conversations | [optional] 
**fallback_response** | **str** | Fixed response content for fallback | [optional] 
**fallback_strategy** | [**GithubComTencentWeKnoraInternalTypesFallbackStrategy**](GithubComTencentWeKnoraInternalTypesFallbackStrategy.md) | Strategy to use when no relevant knowledge is found | [optional] 
**keyword_threshold** | **float** | Threshold for keyword-based retrieval | [optional] 
**max_rounds** | **int** | Maximum number of conversation rounds to maintain | [optional] 
**no_match_prefix** | **str** | Prefix for responses when no match is found | [optional] 
**rerank_model_id** | **str** | ID of the model used for reranking results | [optional] 
**rerank_threshold** | **float** | Threshold for reranking results | [optional] 
**rerank_top_k** | **int** | Number of top results after reranking | [optional] 
**summary_model_id** | **str** | ID of the model used for summarization | [optional] 
**summary_parameters** | [**GithubComTencentWeKnoraInternalTypesSummaryConfig**](GithubComTencentWeKnoraInternalTypesSummaryConfig.md) | Parameters for the summary model | [optional] 
**vector_threshold** | **float** | Threshold for vector-based retrieval | [optional] 

## Example

```python
from weknora.models.internal_handler_session_session_strategy import InternalHandlerSessionSessionStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerSessionSessionStrategy from a JSON string
internal_handler_session_session_strategy_instance = InternalHandlerSessionSessionStrategy.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerSessionSessionStrategy.to_json())

# convert the object into a dict
internal_handler_session_session_strategy_dict = internal_handler_session_session_strategy_instance.to_dict()
# create an instance of InternalHandlerSessionSessionStrategy from a dict
internal_handler_session_session_strategy_from_dict = InternalHandlerSessionSessionStrategy.from_dict(internal_handler_session_session_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


