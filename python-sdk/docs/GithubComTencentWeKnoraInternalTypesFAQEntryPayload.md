# GithubComTencentWeKnoraInternalTypesFAQEntryPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer_strategy** | [**GithubComTencentWeKnoraInternalTypesAnswerStrategy**](GithubComTencentWeKnoraInternalTypesAnswerStrategy.md) |  | [optional] 
**answers** | **List[str]** |  | 
**is_enabled** | **bool** |  | [optional] 
**is_recommended** | **bool** |  | [optional] 
**negative_questions** | **List[str]** |  | [optional] 
**similar_questions** | **List[str]** |  | [optional] 
**standard_question** | **str** |  | 
**tag_id** | **str** |  | [optional] 
**tag_name** | **str** |  | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_faq_entry_payload import GithubComTencentWeKnoraInternalTypesFAQEntryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesFAQEntryPayload from a JSON string
github_com_tencent_we_knora_internal_types_faq_entry_payload_instance = GithubComTencentWeKnoraInternalTypesFAQEntryPayload.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesFAQEntryPayload.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_faq_entry_payload_dict = github_com_tencent_we_knora_internal_types_faq_entry_payload_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesFAQEntryPayload from a dict
github_com_tencent_we_knora_internal_types_faq_entry_payload_from_dict = GithubComTencentWeKnoraInternalTypesFAQEntryPayload.from_dict(github_com_tencent_we_knora_internal_types_faq_entry_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


