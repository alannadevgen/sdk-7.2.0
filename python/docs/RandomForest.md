# RandomForest

Define a logical operator for train a model.  Attributes ---------- type : str     Type of model (Random Forest, ...).  Methods ------- accept(visitor)     Enables the visitor to visit the task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | Random Forest model. | [optional] [default to 'random_forest']
**test_size** | **float** | Represent the proportion of the dataset to include in the test split. [0, 1.0] | 
**predict_column** | **str** | The column of the dataset to predict. | 
**features_column** | **List[str]** | The features columns . | 
**number_trees** | **int** | The number of trees in the forest. | 
**max_depth** | **int** | The maximum depth of the tree. | 
**seed** | **int** | Seed to set in order to have reproducible results. | [optional] [default to 42]

## Example

```python
from graalsystems.models.random_forest import RandomForest

# TODO update the JSON string below
json = "{}"
# create an instance of RandomForest from a JSON string
random_forest_instance = RandomForest.from_json(json)
# print the JSON string representation of the object
print RandomForest.to_json()

# convert the object into a dict
random_forest_dict = random_forest_instance.to_dict()
# create an instance of RandomForest from a dict
random_forest_form_dict = random_forest.from_dict(random_forest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


