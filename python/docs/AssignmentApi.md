# graalsystems.AssignmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_assignment**](AssignmentApi.md#create_role_assignment) | **POST** /assignments | Create a assignment
[**delete_role_assignment_by_id**](AssignmentApi.md#delete_role_assignment_by_id) | **DELETE** /assignments/{assignmentId} | Delete an assignment by an id
[**find_role_assignment_by_id**](AssignmentApi.md#find_role_assignment_by_id) | **GET** /assignments/{assignmentId} | Find assignment by Id
[**find_role_assignments**](AssignmentApi.md#find_role_assignments) | **GET** /assignments | Retrieve all assignments for a resource


# **create_role_assignment**
> RoleAssignment create_role_assignment(x_tenant, role_assignment)

Create a assignment

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.role_assignment import RoleAssignment
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
    api_instance = graalsystems.AssignmentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    role_assignment = graalsystems.RoleAssignment() # RoleAssignment | The assignment to be created

    try:
        # Create a assignment
        api_response = api_instance.create_role_assignment(x_tenant, role_assignment)
        print("The response of AssignmentApi->create_role_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentApi->create_role_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **role_assignment** | [**RoleAssignment**](RoleAssignment.md)| The assignment to be created | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.assignment+json
 - **Accept**: application/vnd.graal.systems.v1.assignment+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_assignment_by_id**
> delete_role_assignment_by_id(x_tenant, assignment_id)

Delete an assignment by an id

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
    api_instance = graalsystems.AssignmentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    assignment_id = 'assignment_id_example' # str | Id of the assignment

    try:
        # Delete an assignment by an id
        api_instance.delete_role_assignment_by_id(x_tenant, assignment_id)
    except Exception as e:
        print("Exception when calling AssignmentApi->delete_role_assignment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **assignment_id** | **str**| Id of the assignment | 

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

# **find_role_assignment_by_id**
> RoleAssignment find_role_assignment_by_id(x_tenant, assignment_id)

Find assignment by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.role_assignment import RoleAssignment
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
    api_instance = graalsystems.AssignmentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    assignment_id = 'assignment_id_example' # str | Id of the assignment

    try:
        # Find assignment by Id
        api_response = api_instance.find_role_assignment_by_id(x_tenant, assignment_id)
        print("The response of AssignmentApi->find_role_assignment_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentApi->find_role_assignment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **assignment_id** | **str**| Id of the assignment | 

### Return type

[**RoleAssignment**](RoleAssignment.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.assignment+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | RoleAssignment not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_role_assignments**
> List[RoleAndPrincipalAndAssignment] find_role_assignments(x_tenant, resource_type=resource_type, resource_id=resource_id)

Retrieve all assignments for a resource

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.role_and_principal_and_assignment import RoleAndPrincipalAndAssignment
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
    api_instance = graalsystems.AssignmentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    resource_type = 'resource_type_example' # str |  (optional)
    resource_id = 'resource_id_example' # str |  (optional)

    try:
        # Retrieve all assignments for a resource
        api_response = api_instance.find_role_assignments(x_tenant, resource_type=resource_type, resource_id=resource_id)
        print("The response of AssignmentApi->find_role_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentApi->find_role_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **resource_type** | **str**|  | [optional] 
 **resource_id** | **str**|  | [optional] 

### Return type

[**List[RoleAndPrincipalAndAssignment]**](RoleAndPrincipalAndAssignment.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.roleprincipalassignment+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

