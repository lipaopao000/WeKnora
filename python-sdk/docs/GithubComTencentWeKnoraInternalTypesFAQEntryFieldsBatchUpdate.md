# GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**by_id** | [**Dict[str, GithubComTencentWeKnoraInternalTypesFAQEntryFieldsUpdate]**](GithubComTencentWeKnoraInternalTypesFAQEntryFieldsUpdate.md) | ByID 按条目ID更新，key为条目ID | [optional] 
**by_tag** | [**Dict[str, GithubComTencentWeKnoraInternalTypesFAQEntryFieldsUpdate]**](GithubComTencentWeKnoraInternalTypesFAQEntryFieldsUpdate.md) | ByTag 按Tag批量更新，key为TagID（空字符串表示未分类） | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_faq_entry_fields_batch_update import GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate from a JSON string
github_com_tencent_we_knora_internal_types_faq_entry_fields_batch_update_instance = GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_faq_entry_fields_batch_update_dict = github_com_tencent_we_knora_internal_types_faq_entry_fields_batch_update_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate from a dict
github_com_tencent_we_knora_internal_types_faq_entry_fields_batch_update_from_dict = GithubComTencentWeKnoraInternalTypesFAQEntryFieldsBatchUpdate.from_dict(github_com_tencent_we_knora_internal_types_faq_entry_fields_batch_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


