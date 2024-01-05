# JoblibReader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Name of the path. | 
**type** | **str** | Define file type for Joblib. | [optional] [default to 'joblib']

## Example

```python
from graalsystems.models.joblib_reader import JoblibReader

# TODO update the JSON string below
json = "{}"
# create an instance of JoblibReader from a JSON string
joblib_reader_instance = JoblibReader.from_json(json)
# print the JSON string representation of the object
print JoblibReader.to_json()

# convert the object into a dict
joblib_reader_dict = joblib_reader_instance.to_dict()
# create an instance of JoblibReader from a dict
joblib_reader_form_dict = joblib_reader.from_dict(joblib_reader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


