# graalsystems.UsageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_usage**](UsageApi.md#create_usage) | **POST** /usages | Create an usage
[**find_usages**](UsageApi.md#find_usages) | **GET** /usages | Retrieve all usages


# **create_usage**
> Usage create_usage(x_tenant, usage)

Create an usage

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.usage import Usage
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
    api_instance = graalsystems.UsageApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    usage = graalsystems.Usage() # Usage | The usage to be created

    try:
        # Create an usage
        api_response = api_instance.create_usage(x_tenant, usage)
        print("The response of UsageApi->create_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->create_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **usage** | [**Usage**](Usage.md)| The usage to be created | 

### Return type

[**Usage**](Usage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.usage+json
 - **Accept**: application/vnd.graal.systems.v1.usage+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_usages**
> List[Usage] find_usages(x_tenant, var_from=var_from, to=to, var_for=var_for, params=params)

Retrieve all usages

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.usage import Usage
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
    api_instance = graalsystems.UsageApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    var_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    var_for = 'var_for_example' # str |  (optional)
    params = {'key': 'params_example'} # Dict[str, str] |  (optional)

    try:
        # Retrieve all usages
        api_response = api_instance.find_usages(x_tenant, var_from=var_from, to=to, var_for=var_for, params=params)
        print("The response of UsageApi->find_usages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->find_usages: %s\n" % e)
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

[**List[Usage]**](Usage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.usage+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

