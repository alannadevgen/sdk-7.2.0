# MariaDBOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'maria']

## Example

```python
from graalsystems.models.maria_db_options import MariaDBOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MariaDBOptions from a JSON string
maria_db_options_instance = MariaDBOptions.from_json(json)
# print the JSON string representation of the object
print MariaDBOptions.to_json()

# convert the object into a dict
maria_db_options_dict = maria_db_options_instance.to_dict()
# create an instance of MariaDBOptions from a dict
maria_db_options_form_dict = maria_db_options.from_dict(maria_db_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


