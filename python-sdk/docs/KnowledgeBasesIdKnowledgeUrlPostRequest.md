# KnowledgeBasesIdKnowledgeUrlPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_multimodel** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from weknora.models.knowledge_bases_id_knowledge_url_post_request import KnowledgeBasesIdKnowledgeUrlPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBasesIdKnowledgeUrlPostRequest from a JSON string
knowledge_bases_id_knowledge_url_post_request_instance = KnowledgeBasesIdKnowledgeUrlPostRequest.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBasesIdKnowledgeUrlPostRequest.to_json())

# convert the object into a dict
knowledge_bases_id_knowledge_url_post_request_dict = knowledge_bases_id_knowledge_url_post_request_instance.to_dict()
# create an instance of KnowledgeBasesIdKnowledgeUrlPostRequest from a dict
knowledge_bases_id_knowledge_url_post_request_from_dict = KnowledgeBasesIdKnowledgeUrlPostRequest.from_dict(knowledge_bases_id_knowledge_url_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


