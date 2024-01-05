# graalsystems.DeviceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DeviceApi.md#create_device) | **POST** /devices | Create device
[**delete_device_by_id**](DeviceApi.md#delete_device_by_id) | **DELETE** /devices/{deviceId} | Delete a device by an id
[**find_device_by_device_id**](DeviceApi.md#find_device_by_device_id) | **GET** /devices/{deviceId} | Find device by Id
[**find_devices**](DeviceApi.md#find_devices) | **GET** /devices | Retrieve all device
[**update_device**](DeviceApi.md#update_device) | **PATCH** /devices/{deviceId} | Update an device


# **create_device**
> Device create_device(x_tenant, filename=filename)

Create device

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.device import Device
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
    api_instance = graalsystems.DeviceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    filename = None # List[bytearray] |  (optional)

    try:
        # Create device
        api_response = api_instance.create_device(x_tenant, filename=filename)
        print("The response of DeviceApi->create_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->create_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **filename** | **List[bytearray]**|  | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/vnd.graal.systems.v1.device+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_by_id**
> delete_device_by_id(x_tenant, device_id)

Delete a device by an id

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
    api_instance = graalsystems.DeviceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    device_id = 'device_id_example' # str | Id of the device

    try:
        # Delete a device by an id
        api_instance.delete_device_by_id(x_tenant, device_id)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_device_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **device_id** | **str**| Id of the device | 

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

# **find_device_by_device_id**
> Device find_device_by_device_id(x_tenant, device_id)

Find device by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.device import Device
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
    api_instance = graalsystems.DeviceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    device_id = 'device_id_example' # str | Id of the device

    try:
        # Find device by Id
        api_response = api_instance.find_device_by_device_id(x_tenant, device_id)
        print("The response of DeviceApi->find_device_by_device_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->find_device_by_device_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **device_id** | **str**| Id of the device | 

### Return type

[**Device**](Device.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.device+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Device not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_devices**
> DevicePage find_devices(x_tenant, page=page, size=size)

Retrieve all device

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.device_page import DevicePage
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
    api_instance = graalsystems.DeviceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    page = 0 # int |  (optional) (default to 0)
    size = 200 # int |  (optional) (default to 200)

    try:
        # Retrieve all device
        api_response = api_instance.find_devices(x_tenant, page=page, size=size)
        print("The response of DeviceApi->find_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->find_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 200]

### Return type

[**DevicePage**](DevicePage.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.device+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> Device update_device(x_tenant, device_id, patch)

Update an device

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.device import Device
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
    api_instance = graalsystems.DeviceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    device_id = 'device_id_example' # str | Id of the device
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update an device
        api_response = api_instance.update_device(x_tenant, device_id, patch)
        print("The response of DeviceApi->update_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->update_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **device_id** | **str**| Id of the device | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Device**](Device.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.device+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Project not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

