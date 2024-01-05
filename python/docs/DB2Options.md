# DB2Options


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**database** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'db2']

## Example

```python
from graalsystems.models.db2_options import DB2Options

# TODO update the JSON string below
json = "{}"
# create an instance of DB2Options from a JSON string
db2_options_instance = DB2Options.from_json(json)
# print the JSON string representation of the object
print DB2Options.to_json()

# convert the object into a dict
db2_options_dict = db2_options_instance.to_dict()
# create an instance of DB2Options from a dict
db2_options_form_dict = db2_options.from_dict(db2_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


