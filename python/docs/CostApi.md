# graalsystems.CostApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_costs**](CostApi.md#get_costs) | **GET** /costs | Find the costs


# **get_costs**
> CostStats get_costs(x_tenant, var_from=var_from, to=to, var_for=var_for, params=params)

Find the costs

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.cost_stats import CostStats
from graalsystems.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = graalsystems.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with graalsystems.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = graalsystems.CostApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    var_for = 'var_for_example' # str |  (optional)
    params = {'key': 'params_example'} # Dict[str, str] |  (optional)

    try:
        # Find the costs
        api_response = api_instance.get_costs(x_tenant, var_from=var_from, to=to, var_for=var_for, params=params)
        print("The response of CostApi->get_costs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostApi->get_costs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **var_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 
 **var_for** | **str**|  | [optional] 
 **params** | [**Dict[str, str]**](str.md)|  | [optional] 

### Return type

[**CostStats**](CostStats.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.costs+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

