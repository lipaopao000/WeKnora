# KnowledgeBasesIdTagsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from weknora_sdk.models.knowledge_bases_id_tags_post_request import KnowledgeBasesIdTagsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBasesIdTagsPostRequest from a JSON string
knowledge_bases_id_tags_post_request_instance = KnowledgeBasesIdTagsPostRequest.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBasesIdTagsPostRequest.to_json())

# convert the object into a dict
knowledge_bases_id_tags_post_request_dict = knowledge_bases_id_tags_post_request_instance.to_dict()
# create an instance of KnowledgeBasesIdTagsPostRequest from a dict
knowledge_bases_id_tags_post_request_from_dict = KnowledgeBasesIdTagsPostRequest.from_dict(knowledge_bases_id_tags_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


