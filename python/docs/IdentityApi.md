# graalsystems.IdentityApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_identity**](IdentityApi.md#create_identity) | **POST** /identities | Create a identity
[**delete_identity_by_id**](IdentityApi.md#delete_identity_by_id) | **DELETE** /identities/{identityId} | Delete an identity by an id
[**find_identities**](IdentityApi.md#find_identities) | **GET** /identities | Retrieve all identities
[**find_identity_by_id**](IdentityApi.md#find_identity_by_id) | **GET** /identities/{identityId} | Find identity by Id
[**find_roles_by_identity_id**](IdentityApi.md#find_roles_by_identity_id) | **GET** /identities/{identityId}/roles | Find roles by a identity id
[**update_identity**](IdentityApi.md#update_identity) | **PATCH** /identities/{identityId} | Update a identity


# **create_identity**
> Identity create_identity(x_tenant, identity)

Create a identity

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.identity import Identity
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
    api_instance = graalsystems.IdentityApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    identity = graalsystems.Identity() # Identity | The identity to be created

    try:
        # Create a identity
        api_response = api_instance.create_identity(x_tenant, identity)
        print("The response of IdentityApi->create_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->create_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **identity** | [**Identity**](Identity.md)| The identity to be created | 

### Return type

[**Identity**](Identity.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.identity+json
 - **Accept**: application/vnd.graal.systems.v1.identity+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_by_id**
> delete_identity_by_id(x_tenant, identity_id)

Delete an identity by an id

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
    api_instance = graalsystems.IdentityApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    identity_id = 'identity_id_example' # str | Id of the identity

    try:
        # Delete an identity by an id
        api_instance.delete_identity_by_id(x_tenant, identity_id)
    except Exception as e:
        print("Exception when calling IdentityApi->delete_identity_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **identity_id** | **str**| Id of the identity | 

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

# **find_identities**
> List[Identity] find_identities(x_tenant)

Retrieve all identities

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.identity import Identity
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
    api_instance = graalsystems.IdentityApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all identities
        api_response = api_instance.find_identities(x_tenant)
        print("The response of IdentityApi->find_identities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->find_identities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Identity]**](Identity.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.identity+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_identity_by_id**
> Identity find_identity_by_id(x_tenant, identity_id)

Find identity by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.identity import Identity
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
    api_instance = graalsystems.IdentityApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    identity_id = 'identity_id_example' # str | Id of the identity

    try:
        # Find identity by Id
        api_response = api_instance.find_identity_by_id(x_tenant, identity_id)
        print("The response of IdentityApi->find_identity_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->find_identity_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **identity_id** | **str**| Id of the identity | 

### Return type

[**Identity**](Identity.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.identity+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Identity not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_roles_by_identity_id**
> List[RoleAndAssignment] find_roles_by_identity_id(x_tenant, identity_id)

Find roles by a identity id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.role_and_assignment import RoleAndAssignment
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
    api_instance = graalsystems.IdentityApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    identity_id = 'identity_id_example' # str | Id of the identity

    try:
        # Find roles by a identity id
        api_response = api_instance.find_roles_by_identity_id(x_tenant, identity_id)
        print("The response of IdentityApi->find_roles_by_identity_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->find_roles_by_identity_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **identity_id** | **str**| Id of the identity | 

### Return type

[**List[RoleAndAssignment]**](RoleAndAssignment.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.roleassignment+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_identity**
> Identity update_identity(x_tenant, identity_id, patch)

Update a identity

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.identity import Identity
from graalsystems.models.patch import Patch
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
    api_instance = graalsystems.IdentityApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    identity_id = 'identity_id_example' # str | Id of the identity
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a identity
        api_response = api_instance.update_identity(x_tenant, identity_id, patch)
        print("The response of IdentityApi->update_identity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityApi->update_identity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **identity_id** | **str**| Id of the identity | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Identity**](Identity.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.identity+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | User not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

