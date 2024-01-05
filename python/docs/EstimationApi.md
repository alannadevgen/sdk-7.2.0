# graalsystems.EstimationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_estimation**](EstimationApi.md#create_estimation) | **POST** /estimations | Create an estimation


# **create_estimation**
> Estimation create_estimation(x_tenant, estimation)

Create an estimation

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.estimation import Estimation
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
    api_instance = graalsystems.EstimationApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    estimation = graalsystems.Estimation() # Estimation | The estimation to be calculated

    try:
        # Create an estimation
        api_response = api_instance.create_estimation(x_tenant, estimation)
        print("The response of EstimationApi->create_estimation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EstimationApi->create_estimation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **estimation** | [**Estimation**](Estimation.md)| The estimation to be calculated | 

### Return type

[**Estimation**](Estimation.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.estimation+json
 - **Accept**: application/vnd.graal.systems.v1.estimation+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

