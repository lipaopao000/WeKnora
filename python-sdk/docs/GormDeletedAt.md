# GormDeletedAt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **str** |  | [optional] 
**valid** | **bool** | Valid is true if Time is not NULL | [optional] 

## Example

```python
from weknora.models.gorm_deleted_at import GormDeletedAt

# TODO update the JSON string below
json = "{}"
# create an instance of GormDeletedAt from a JSON string
gorm_deleted_at_instance = GormDeletedAt.from_json(json)
# print the JSON string representation of the object
print(GormDeletedAt.to_json())

# convert the object into a dict
gorm_deleted_at_dict = gorm_deleted_at_instance.to_dict()
# create an instance of GormDeletedAt from a dict
gorm_deleted_at_from_dict = GormDeletedAt.from_dict(gorm_deleted_at_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


