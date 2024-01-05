# graalsystems.EnrollmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_enrollment**](EnrollmentApi.md#create_enrollment) | **POST** /enrollments | Create enrollment
[**delete_enrollment_by_id**](EnrollmentApi.md#delete_enrollment_by_id) | **DELETE** /enrollments/{enrollmentId} | Delete a enrollment by an id
[**find_enrollment_by_enrollment_id**](EnrollmentApi.md#find_enrollment_by_enrollment_id) | **GET** /enrollments/{enrollmentId} | Find enrollment by Id
[**find_enrollments**](EnrollmentApi.md#find_enrollments) | **GET** /enrollments | Retrieve all enrollment


# **create_enrollment**
> Enrollment create_enrollment(x_tenant, enrollment)

Create enrollment

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.enrollment import Enrollment
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
    api_instance = graalsystems.EnrollmentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    enrollment = graalsystems.Enrollment() # Enrollment | The enrollment to be created

    try:
        # Create enrollment
        api_response = api_instance.create_enrollment(x_tenant, enrollment)
        print("The response of EnrollmentApi->create_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentApi->create_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **enrollment** | [**Enrollment**](Enrollment.md)| The enrollment to be created | 

### Return type

[**Enrollment**](Enrollment.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.enrollment+json
 - **Accept**: application/vnd.graal.systems.v1.enrollment+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enrollment_by_id**
> delete_enrollment_by_id(x_tenant, enrollment_id)

Delete a enrollment by an id

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
    api_instance = graalsystems.EnrollmentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | Id of the enrollment

    try:
        # Delete a enrollment by an id
        api_instance.delete_enrollment_by_id(x_tenant, enrollment_id)
    except Exception as e:
        print("Exception when calling EnrollmentApi->delete_enrollment_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **enrollment_id** | **str**| Id of the enrollment | 

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
**404** | Project not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_enrollment_by_enrollment_id**
> Enrollment find_enrollment_by_enrollment_id(x_tenant, enrollment_id)

Find enrollment by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.enrollment import Enrollment
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
    api_instance = graalsystems.EnrollmentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    enrollment_id = 'enrollment_id_example' # str | Id of the enrollment

    try:
        # Find enrollment by Id
        api_response = api_instance.find_enrollment_by_enrollment_id(x_tenant, enrollment_id)
        print("The response of EnrollmentApi->find_enrollment_by_enrollment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentApi->find_enrollment_by_enrollment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **enrollment_id** | **str**| Id of the enrollment | 

### Return type

[**Enrollment**](Enrollment.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.enrollment+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Enrollment not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_enrollments**
> EnrollmentPage find_enrollments(x_tenant, page=page, size=size)

Retrieve all enrollment

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.enrollment_page import EnrollmentPage
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
    api_instance = graalsystems.EnrollmentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    page = 0 # int |  (optional) (default to 0)
    size = 200 # int |  (optional) (default to 200)

    try:
        # Retrieve all enrollment
        api_response = api_instance.find_enrollments(x_tenant, page=page, size=size)
        print("The response of EnrollmentApi->find_enrollments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentApi->find_enrollments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 200]

### Return type

[**EnrollmentPage**](EnrollmentPage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.enrollment+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

