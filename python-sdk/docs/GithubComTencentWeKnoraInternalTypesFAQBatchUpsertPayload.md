# GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[GithubComTencentWeKnoraInternalTypesFAQEntryPayload]**](GithubComTencentWeKnoraInternalTypesFAQEntryPayload.md) |  | 
**knowledge_id** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_faq_batch_upsert_payload import GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload from a JSON string
github_com_tencent_we_knora_internal_types_faq_batch_upsert_payload_instance = GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_faq_batch_upsert_payload_dict = github_com_tencent_we_knora_internal_types_faq_batch_upsert_payload_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload from a dict
github_com_tencent_we_knora_internal_types_faq_batch_upsert_payload_from_dict = GithubComTencentWeKnoraInternalTypesFAQBatchUpsertPayload.from_dict(github_com_tencent_we_knora_internal_types_faq_batch_upsert_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


