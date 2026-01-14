# GithubComTencentWeKnoraInternalTypesUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **str** | Avatar URL of the user | [optional] 
**can_access_all_tenants** | **bool** | Whether the user can access all tenants (cross-tenant access) | [optional] 
**created_at** | **str** | Creation time of the user | [optional] 
**deleted_at** | [**GormDeletedAt**](GormDeletedAt.md) | Deletion time of the user | [optional] 
**email** | **str** | Email address of the user | [optional] 
**id** | **str** | Unique identifier of the user | [optional] 
**is_active** | **bool** | Whether the user is active | [optional] 
**tenant** | [**GithubComTencentWeKnoraInternalTypesTenant**](GithubComTencentWeKnoraInternalTypesTenant.md) | Association relationship, not stored in the database | [optional] 
**tenant_id** | **int** | Tenant ID that the user belongs to | [optional] 
**updated_at** | **str** | Last updated time of the user | [optional] 
**username** | **str** | Username of the user | [optional] 

## Example

```python
from weknora_sdk.models.github_com_tencent_we_knora_internal_types_user import GithubComTencentWeKnoraInternalTypesUser

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComTencentWeKnoraInternalTypesUser from a JSON string
github_com_tencent_we_knora_internal_types_user_instance = GithubComTencentWeKnoraInternalTypesUser.from_json(json)
# print the JSON string representation of the object
print(GithubComTencentWeKnoraInternalTypesUser.to_json())

# convert the object into a dict
github_com_tencent_we_knora_internal_types_user_dict = github_com_tencent_we_knora_internal_types_user_instance.to_dict()
# create an instance of GithubComTencentWeKnoraInternalTypesUser from a dict
github_com_tencent_we_knora_internal_types_user_from_dict = GithubComTencentWeKnoraInternalTypesUser.from_dict(github_com_tencent_we_knora_internal_types_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


