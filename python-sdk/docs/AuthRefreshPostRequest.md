# AuthRefreshPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refresh_token** | **str** |  | [optional] 

## Example

```python
from weknora_sdk.models.auth_refresh_post_request import AuthRefreshPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthRefreshPostRequest from a JSON string
auth_refresh_post_request_instance = AuthRefreshPostRequest.from_json(json)
# print the JSON string representation of the object
print(AuthRefreshPostRequest.to_json())

# convert the object into a dict
auth_refresh_post_request_dict = auth_refresh_post_request_instance.to_dict()
# create an instance of AuthRefreshPostRequest from a dict
auth_refresh_post_request_from_dict = AuthRefreshPostRequest.from_dict(auth_refresh_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


