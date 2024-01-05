# DatabaseMigrationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'database-migration']
**datawarehouse_id** | **str** |  | [optional] 
**repository** | [**GitLibrary**](GitLibrary.md) |  | [optional] 

## Example

```python
from graalsystems.models.database_migration_options import DatabaseMigrationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseMigrationOptions from a JSON string
database_migration_options_instance = DatabaseMigrationOptions.from_json(json)
# print the JSON string representation of the object
print DatabaseMigrationOptions.to_json()

# convert the object into a dict
database_migration_options_dict = database_migration_options_instance.to_dict()
# create an instance of DatabaseMigrationOptions from a dict
database_migration_options_form_dict = database_migration_options.from_dict(database_migration_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


