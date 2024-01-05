# PickleReader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Name of the path. | 
**type** | **str** | Define file type for Pickle. | [optional] [default to 'pickle']

## Example

```python
from graalsystems.models.pickle_reader import PickleReader

# TODO update the JSON string below
json = "{}"
# create an instance of PickleReader from a JSON string
pickle_reader_instance = PickleReader.from_json(json)
# print the JSON string representation of the object
print PickleReader.to_json()

# convert the object into a dict
pickle_reader_dict = pickle_reader_instance.to_dict()
# create an instance of PickleReader from a dict
pickle_reader_form_dict = pickle_reader.from_dict(pickle_reader_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


