# graalsystems.PriceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_price**](PriceApi.md#create_price) | **POST** /prices | Create an price
[**delete_price_by_id**](PriceApi.md#delete_price_by_id) | **DELETE** /prices/{priceId} | Delete a price by its id
[**find_price_by_id**](PriceApi.md#find_price_by_id) | **GET** /prices/{priceId} | Find price by Id
[**find_prices**](PriceApi.md#find_prices) | **GET** /prices | Retrieve all prices
[**update_price**](PriceApi.md#update_price) | **PATCH** /prices/{priceId} | Update a price


# **create_price**
> Price create_price(price)

Create an price

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.price import Price
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
    api_instance = graalsystems.PriceApi(api_client)
    price = graalsystems.Price() # Price | The price to be created

    try:
        # Create an price
        api_response = api_instance.create_price(price)
        print("The response of PriceApi->create_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceApi->create_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price** | [**Price**](Price.md)| The price to be created | 

### Return type

[**Price**](Price.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.price+json
 - **Accept**: application/vnd.graal.systems.v1.price+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_price_by_id**
> delete_price_by_id(x_tenant, price_id)

Delete a price by its id

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
    api_instance = graalsystems.PriceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    price_id = 'price_id_example' # str | Id of the Price

    try:
        # Delete a price by its id
        api_instance.delete_price_by_id(x_tenant, price_id)
    except Exception as e:
        print("Exception when calling PriceApi->delete_price_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **price_id** | **str**| Id of the Price | 

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
**404** | Price not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_price_by_id**
> Price find_price_by_id(x_tenant, price_id)

Find price by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.price import Price
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
    api_instance = graalsystems.PriceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    price_id = 'price_id_example' # str | Id of the price

    try:
        # Find price by Id
        api_response = api_instance.find_price_by_id(x_tenant, price_id)
        print("The response of PriceApi->find_price_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceApi->find_price_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **price_id** | **str**| Id of the price | 

### Return type

[**Price**](Price.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.price+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Price not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_prices**
> List[Price] find_prices(x_tenant)

Retrieve all prices

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.price import Price
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
    api_instance = graalsystems.PriceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all prices
        api_response = api_instance.find_prices(x_tenant)
        print("The response of PriceApi->find_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceApi->find_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Price]**](Price.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.price+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_price**
> Price update_price(x_tenant, price_id, patch)

Update a price

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.patch import Patch
from graalsystems.models.price import Price
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
    api_instance = graalsystems.PriceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    price_id = 'price_id_example' # str | Id of the Price
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a price
        api_response = api_instance.update_price(x_tenant, price_id, patch)
        print("The response of PriceApi->update_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceApi->update_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **price_id** | **str**| Id of the Price | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Price**](Price.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.price+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Price not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

