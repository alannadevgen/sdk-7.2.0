# LogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **datetime** |  | [optional] 
**message** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from graalsystems.models.log_entry import LogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LogEntry from a JSON string
log_entry_instance = LogEntry.from_json(json)
# print the JSON string representation of the object
print LogEntry.to_json()

# convert the object into a dict
log_entry_dict = log_entry_instance.to_dict()
# create an instance of LogEntry from a dict
log_entry_form_dict = log_entry.from_dict(log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


