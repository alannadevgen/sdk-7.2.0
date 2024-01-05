# graalsystems.ApplicationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationApi.md#create_application) | **POST** /applications | Create a application
[**delete_application_by_id**](ApplicationApi.md#delete_application_by_id) | **DELETE** /applications/{applicationId} | Delete an application by an id
[**find_application_by_id**](ApplicationApi.md#find_application_by_id) | **GET** /applications/{applicationId} | Find application by Id
[**find_applications**](ApplicationApi.md#find_applications) | **GET** /applications | Retrieve all applications


# **create_application**
> Application create_application(x_tenant, application)

Create a application

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.application import Application
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
    api_instance = graalsystems.ApplicationApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    application = graalsystems.Application() # Application | The application to be created

    try:
        # Create a application
        api_response = api_instance.create_application(x_tenant, application)
        print("The response of ApplicationApi->create_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->create_application: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **application** | [**Application**](Application.md)| The application to be created | 

### Return type

[**Application**](Application.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.application+json
 - **Accept**: application/vnd.graal.systems.v1.application+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_by_id**
> delete_application_by_id(x_tenant, application_id)

Delete an application by an id

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
    api_instance = graalsystems.ApplicationApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    application_id = 'application_id_example' # str | Id of the application

    try:
        # Delete an application by an id
        api_instance.delete_application_by_id(x_tenant, application_id)
    except Exception as e:
        print("Exception when calling ApplicationApi->delete_application_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **application_id** | **str**| Id of the application | 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**404** | User not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_application_by_id**
> Application find_application_by_id(x_tenant, application_id)

Find application by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.application import Application
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
    api_instance = graalsystems.ApplicationApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    application_id = 'application_id_example' # str | Id of the application

    try:
        # Find application by Id
        api_response = api_instance.find_application_by_id(x_tenant, application_id)
        print("The response of ApplicationApi->find_application_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->find_application_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **application_id** | **str**| Id of the application | 

### Return type

[**Application**](Application.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.application+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Application not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_applications**
> List[Application] find_applications(x_tenant)

Retrieve all applications

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.application import Application
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
    api_instance = graalsystems.ApplicationApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all applications
        api_response = api_instance.find_applications(x_tenant)
        print("The response of ApplicationApi->find_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationApi->find_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Application]**](Application.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.application+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

