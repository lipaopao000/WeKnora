# GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**question_count** | **int** | Number of questions to generate per chunk (default: 3, max: 10) | [optional] 

## Example

```python
from weknora.models.github_com_tencent_we_knora_internal_types_question_generation_config import GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig from a JSON string
github_com_tencent_we_knora_internal_types_question_generation_config_instance = GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_question_generation_config_dict = github_com_tencent_we_knora_internal_types_question_generation_config_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig from a dict
github_com_tencent_we_knora_internal_types_question_generation_config_from_dict = GithubComTencentWeKnoraInternalTypesQuestionGenerationConfig.from_dict(github_com_tencent_we_knora_internal_types_question_generation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


