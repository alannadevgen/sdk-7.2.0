# graalsystems.VerificationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_verification**](VerificationApi.md#create_verification) | **POST** /verifications | Create a verification
[**find_verification_by_code**](VerificationApi.md#find_verification_by_code) | **GET** /verifications | Find a verification by code


# **create_verification**
> create_verification(type, value)

Create a verification

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
    api_instance = graalsystems.VerificationApi(api_client)
    type = 'type_example' # str | 
    value = 'value_example' # str | 

    try:
        # Create a verification
        api_instance.create_verification(type, value)
    except Exception as e:
        print("Exception when calling VerificationApi->create_verification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **value** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_verification_by_code**
> FindVerificationByCode200Response find_verification_by_code(type, value, code)

Find a verification by code

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.find_verification_by_code200_response import FindVerificationByCode200Response
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
    api_instance = graalsystems.VerificationApi(api_client)
    type = 'type_example' # str | 
    value = 'value_example' # str | 
    code = 'code_example' # str | 

    try:
        # Find a verification by code
        api_response = api_instance.find_verification_by_code(type, value, code)
        print("The response of VerificationApi->find_verification_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerificationApi->find_verification_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **value** | **str**|  | 
 **code** | **str**|  | 

### Return type

[**FindVerificationByCode200Response**](FindVerificationByCode200Response.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

