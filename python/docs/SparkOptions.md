# SparkOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'spark']
**libraries** | **List[str]** |  | [optional] 
**conf** | **Dict[str, object]** |  | [optional] 
**main_library** | [**Library**](Library.md) |  | [optional] 
**py_files** | [**List[Library]**](Library.md) |  | [optional] 
**main_class_name** | **str** |  | [optional] 
**loggers** | **List[str]** |  | [optional] 
**executor_instance_type** | **str** |  | [optional] 
**driver_instance_type** | **str** |  | [optional] 
**number_executors** | **float** |  | [optional] 

## Example

```python
from graalsystems.models.spark_options import SparkOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SparkOptions from a JSON string
spark_options_instance = SparkOptions.from_json(json)
# print the JSON string representation of the object
print SparkOptions.to_json()

# convert the object into a dict
spark_options_dict = spark_options_instance.to_dict()
# create an instance of SparkOptions from a dict
spark_options_form_dict = spark_options.from_dict(spark_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


