# FirewallRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**ports** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.firewall_rule import FirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRule from a JSON string
firewall_rule_instance = FirewallRule.from_json(json)
# print the JSON string representation of the object
print FirewallRule.to_json()

# convert the object into a dict
firewall_rule_dict = firewall_rule_instance.to_dict()
# create an instance of FirewallRule from a dict
firewall_rule_form_dict = firewall_rule.from_dict(firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


