# graalsystems.PaymentmethodApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method**](PaymentmethodApi.md#create_payment_method) | **POST** /paymentmethods | Create an payment method
[**delete_payment_method_by_id**](PaymentmethodApi.md#delete_payment_method_by_id) | **DELETE** /paymentmethods/{paymentMethodId} | Delete a payment method by its id
[**find_favorite_or_random_valid_payment_method**](PaymentmethodApi.md#find_favorite_or_random_valid_payment_method) | **GET** /paymentmethods?favorite|random | Retrieve the favorite payment method and a random valid
[**find_payment_method_by_id**](PaymentmethodApi.md#find_payment_method_by_id) | **GET** /paymentmethods/{paymentMethodId} | Find paymentmethod by Id
[**find_payment_methods**](PaymentmethodApi.md#find_payment_methods) | **GET** /paymentmethods | Retrieve all payment methods
[**update_payment_method**](PaymentmethodApi.md#update_payment_method) | **PATCH** /paymentmethods/{paymentMethodId} | Update a payment method


# **create_payment_method**
> PaymentMethod create_payment_method(x_tenant, payment_method)

Create an payment method

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.payment_method import PaymentMethod
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
    api_instance = graalsystems.PaymentmethodApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    payment_method = graalsystems.PaymentMethod() # PaymentMethod | The paymentmethod to be created

    try:
        # Create an payment method
        api_response = api_instance.create_payment_method(x_tenant, payment_method)
        print("The response of PaymentmethodApi->create_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentmethodApi->create_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **payment_method** | [**PaymentMethod**](PaymentMethod.md)| The paymentmethod to be created | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.paymentmethod+json
 - **Accept**: application/vnd.graal.systems.v1.paymentmethod+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_method_by_id**
> delete_payment_method_by_id(x_tenant, payment_method_id)

Delete a payment method by its id

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
    api_instance = graalsystems.PaymentmethodApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | Id of the PaymentMethod

    try:
        # Delete a payment method by its id
        api_instance.delete_payment_method_by_id(x_tenant, payment_method_id)
    except Exception as e:
        print("Exception when calling PaymentmethodApi->delete_payment_method_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **payment_method_id** | **str**| Id of the PaymentMethod | 

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
**404** | PaymentMethod not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_favorite_or_random_valid_payment_method**
> PaymentMethod find_favorite_or_random_valid_payment_method(x_tenant)

Retrieve the favorite payment method and a random valid

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.payment_method import PaymentMethod
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
    api_instance = graalsystems.PaymentmethodApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve the favorite payment method and a random valid
        api_response = api_instance.find_favorite_or_random_valid_payment_method(x_tenant)
        print("The response of PaymentmethodApi->find_favorite_or_random_valid_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentmethodApi->find_favorite_or_random_valid_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.paymentmethod+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_payment_method_by_id**
> PaymentMethod find_payment_method_by_id(x_tenant, payment_method_id)

Find paymentmethod by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.payment_method import PaymentMethod
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
    api_instance = graalsystems.PaymentmethodApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | Id of the payment method

    try:
        # Find paymentmethod by Id
        api_response = api_instance.find_payment_method_by_id(x_tenant, payment_method_id)
        print("The response of PaymentmethodApi->find_payment_method_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentmethodApi->find_payment_method_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **payment_method_id** | **str**| Id of the payment method | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.paymentmethod+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | PaymentMethod not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_payment_methods**
> List[PaymentMethod] find_payment_methods(x_tenant)

Retrieve all payment methods

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.payment_method import PaymentMethod
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
    api_instance = graalsystems.PaymentmethodApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all payment methods
        api_response = api_instance.find_payment_methods(x_tenant)
        print("The response of PaymentmethodApi->find_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentmethodApi->find_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[PaymentMethod]**](PaymentMethod.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.paymentmethod+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_method**
> PaymentMethod update_payment_method(x_tenant, payment_method_id, patch)

Update a payment method

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.patch import Patch
from graalsystems.models.payment_method import PaymentMethod
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
    api_instance = graalsystems.PaymentmethodApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    payment_method_id = 'payment_method_id_example' # str | Id of the PaymentMethod
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a payment method
        api_response = api_instance.update_payment_method(x_tenant, payment_method_id, patch)
        print("The response of PaymentmethodApi->update_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentmethodApi->update_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **payment_method_id** | **str**| Id of the PaymentMethod | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.paymentmethod+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Usage not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

