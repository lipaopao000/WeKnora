# InternalHandlerEvaluationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_id** | **str** | ID of chat model to use | [optional] 
**dataset_id** | **str** | ID of dataset to evaluate | [optional] 
**knowledge_base_id** | **str** | ID of knowledge base to use | [optional] 
**rerank_id** | **str** | ID of rerank model to use | [optional] 

## Example

```python
from weknora_sdk.models.internal_handler_evaluation_request import InternalHandlerEvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InternalHandlerEvaluationRequest from a JSON string
internal_handler_evaluation_request_instance = InternalHandlerEvaluationRequest.from_json(json)
# print the JSON string representation of the object
print(InternalHandlerEvaluationRequest.to_json())

# convert the object into a dict
internal_handler_evaluation_request_dict = internal_handler_evaluation_request_instance.to_dict()
# create an instance of InternalHandlerEvaluationRequest from a dict
internal_handler_evaluation_request_from_dict = InternalHandlerEvaluationRequest.from_dict(internal_handler_evaluation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


