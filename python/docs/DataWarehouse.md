# DataWarehouse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**options** | [**DataWarehouseOptions**](DataWarehouseOptions.md) |  | [optional] 
**owner** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**identity_id** | **str** |  | [optional] 
**infrastructure_id** | **str** |  | [optional] 
**public_url** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from graalsystems.models.data_warehouse import DataWarehouse

# TODO update the JSON string below
json = "{}"
# create an instance of DataWarehouse from a JSON string
data_warehouse_instance = DataWarehouse.from_json(json)
# print the JSON string representation of the object
print DataWarehouse.to_json()

# convert the object into a dict
data_warehouse_dict = data_warehouse_instance.to_dict()
# create an instance of DataWarehouse from a dict
data_warehouse_form_dict = data_warehouse.from_dict(data_warehouse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


