# Database


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**technical_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.database import Database

# TODO update the JSON string below
json = "{}"
# create an instance of Database from a JSON string
database_instance = Database.from_json(json)
# print the JSON string representation of the object
print Database.to_json()

# convert the object into a dict
database_dict = database_instance.to_dict()
# create an instance of Database from a dict
database_form_dict = database.from_dict(database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


