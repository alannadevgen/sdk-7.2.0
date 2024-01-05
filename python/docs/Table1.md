# Table1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**technical_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**public_uri** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.table1 import Table1

# TODO update the JSON string below
json = "{}"
# create an instance of Table1 from a JSON string
table1_instance = Table1.from_json(json)
# print the JSON string representation of the object
print Table1.to_json()

# convert the object into a dict
table1_dict = table1_instance.to_dict()
# create an instance of Table1 from a dict
table1_form_dict = table1.from_dict(table1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


