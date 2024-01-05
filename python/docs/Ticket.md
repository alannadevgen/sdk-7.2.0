# Ticket


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**details** | [**Details**](Details.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.ticket import Ticket

# TODO update the JSON string below
json = "{}"
# create an instance of Ticket from a JSON string
ticket_instance = Ticket.from_json(json)
# print the JSON string representation of the object
print Ticket.to_json()

# convert the object into a dict
ticket_dict = ticket_instance.to_dict()
# create an instance of Ticket from a dict
ticket_form_dict = ticket.from_dict(ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


