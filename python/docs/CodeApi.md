# graalsystems.CodeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_code**](CodeApi.md#download_code) | **POST** /code?download | Download code
[**verify_code**](CodeApi.md#verify_code) | **POST** /code?verify | Verify code


# **download_code**
> bytearray download_code(x_tenant, source=source, destination=destination, filename=filename)

Download code

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
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
    api_instance = graalsystems.CodeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    source = 'source_example' # str |  (optional)
    destination = 'destination_example' # str |  (optional)
    filename = None # List[bytearray] |  (optional)

    try:
        # Download code
        api_response = api_instance.download_code(x_tenant, source=source, destination=destination, filename=filename)
        print("The response of CodeApi->download_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeApi->download_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **source** | **str**|  | [optional] 
 **destination** | **str**|  | [optional] 
 **filename** | **List[bytearray]**|  | [optional] 

### Return type

**bytearray**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_code**
> verify_code(x_tenant, source=source, destination=destination, filename=filename)

Verify code

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
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
    api_instance = graalsystems.CodeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    source = 'source_example' # str |  (optional)
    destination = 'destination_example' # str |  (optional)
    filename = None # List[bytearray] |  (optional)

    try:
        # Verify code
        api_instance.verify_code(x_tenant, source=source, destination=destination, filename=filename)
    except Exception as e:
        print("Exception when calling CodeApi->verify_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **source** | **str**|  | [optional] 
 **destination** | **str**|  | [optional] 
 **filename** | **List[bytearray]**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

