# graalsystems.PermissionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_permissions**](PermissionApi.md#find_permissions) | **GET** /permissions | Retrieve permissions for a specific principal
[**has_permission**](PermissionApi.md#has_permission) | **GET** /permissions?metadata | Retrieve permissions for a specific principal


# **find_permissions**
> List[str] find_permissions(x_tenant, resource_type, resource_id, principal_type, principal_id)

Retrieve permissions for a specific principal

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
    api_instance = graalsystems.PermissionApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    resource_type = 'resource_type_example' # str | 
    resource_id = 'resource_id_example' # str | 
    principal_type = 'principal_type_example' # str | 
    principal_id = 'principal_id_example' # str | 

    try:
        # Retrieve permissions for a specific principal
        api_response = api_instance.find_permissions(x_tenant, resource_type, resource_id, principal_type, principal_id)
        print("The response of PermissionApi->find_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->find_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_id** | **str**|  | 
 **principal_type** | **str**|  | 
 **principal_id** | **str**|  | 

### Return type

**List[str]**

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

# **has_permission**
> bool has_permission(x_tenant, resource_type, resource_id, permission)

Retrieve permissions for a specific principal

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
    api_instance = graalsystems.PermissionApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    resource_type = 'resource_type_example' # str | 
    resource_id = 'resource_id_example' # str | 
    permission = 'permission_example' # str | 

    try:
        # Retrieve permissions for a specific principal
        api_response = api_instance.has_permission(x_tenant, resource_type, resource_id, permission)
        print("The response of PermissionApi->has_permission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PermissionApi->has_permission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **resource_type** | **str**|  | 
 **resource_id** | **str**|  | 
 **permission** | **str**|  | 

### Return type

**bool**

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

