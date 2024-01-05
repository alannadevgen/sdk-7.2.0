# Message


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** |  | [optional] 
**var_from** | **str** |  | [optional] 
**subject** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**importance** | **str** |  | [optional] 
**vars** | **Dict[str, str]** |  | [optional] 

## Example

```python
from graalsystems.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print Message.to_json()

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_form_dict = message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


