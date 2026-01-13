# AuthChangePasswordPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_password** | **str** |  | [optional] 
**old_password** | **str** |  | [optional] 

## Example

```python
from weknora.models.auth_change_password_post_request import AuthChangePasswordPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthChangePasswordPostRequest from a JSON string
auth_change_password_post_request_instance = AuthChangePasswordPostRequest.from_json(json)
# print the JSON string representation of the object
print(AuthChangePasswordPostRequest.to_json())

# convert the object into a dict
auth_change_password_post_request_dict = auth_change_password_post_request_instance.to_dict()
# create an instance of AuthChangePasswordPostRequest from a dict
auth_change_password_post_request_from_dict = AuthChangePasswordPostRequest.from_dict(auth_change_password_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


