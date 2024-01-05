# DataWarehousePage

typed Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**content** | [**List[DataWarehouse]**](DataWarehouse.md) |  | [optional] 

## Example

```python
from graalsystems.models.data_warehouse_page import DataWarehousePage

# TODO update the JSON string below
json = "{}"
# create an instance of DataWarehousePage from a JSON string
data_warehouse_page_instance = DataWarehousePage.from_json(json)
# print the JSON string representation of the object
print DataWarehousePage.to_json()

# convert the object into a dict
data_warehouse_page_dict = data_warehouse_page_instance.to_dict()
# create an instance of DataWarehousePage from a dict
data_warehouse_page_form_dict = data_warehouse_page.from_dict(data_warehouse_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


