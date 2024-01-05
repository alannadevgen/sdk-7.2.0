# graalsystems.InvoiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invoice**](InvoiceApi.md#create_invoice) | **POST** /invoices | Create an invoice
[**delete_invoice_by_id**](InvoiceApi.md#delete_invoice_by_id) | **DELETE** /invoices/{invoiceId} | Delete a invoice by its id
[**download_invoice_by_id**](InvoiceApi.md#download_invoice_by_id) | **GET** /invoices/{invoiceId}?download | Download invoice by Id
[**find_invoice_by_id**](InvoiceApi.md#find_invoice_by_id) | **GET** /invoices/{invoiceId} | Find invoice by Id
[**find_invoices**](InvoiceApi.md#find_invoices) | **GET** /invoices | Retrieve all invoices
[**update_invoice**](InvoiceApi.md#update_invoice) | **PATCH** /invoices/{invoiceId} | Update a invoice


# **create_invoice**
> Invoice create_invoice(invoice)

Create an invoice

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.invoice import Invoice
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
    api_instance = graalsystems.InvoiceApi(api_client)
    invoice = graalsystems.Invoice() # Invoice | The invoice to be created

    try:
        # Create an invoice
        api_response = api_instance.create_invoice(invoice)
        print("The response of InvoiceApi->create_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->create_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice** | [**Invoice**](Invoice.md)| The invoice to be created | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.invoice+json
 - **Accept**: application/vnd.graal.systems.v1.invoice+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invoice_by_id**
> delete_invoice_by_id(x_tenant, invoice_id)

Delete a invoice by its id

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
    api_instance = graalsystems.InvoiceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    invoice_id = 'invoice_id_example' # str | Id of the Invoice

    try:
        # Delete a invoice by its id
        api_instance.delete_invoice_by_id(x_tenant, invoice_id)
    except Exception as e:
        print("Exception when calling InvoiceApi->delete_invoice_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **invoice_id** | **str**| Id of the Invoice | 

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
**404** | Invoice not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_invoice_by_id**
> bytearray download_invoice_by_id(x_tenant, invoice_id)

Download invoice by Id

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
    api_instance = graalsystems.InvoiceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    invoice_id = 'invoice_id_example' # str | Id of the invoice

    try:
        # Download invoice by Id
        api_response = api_instance.download_invoice_by_id(x_tenant, invoice_id)
        print("The response of InvoiceApi->download_invoice_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->download_invoice_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **invoice_id** | **str**| Id of the invoice | 

### Return type

**bytearray**

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Invoice not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_invoice_by_id**
> Invoice find_invoice_by_id(x_tenant, invoice_id)

Find invoice by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.invoice import Invoice
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
    api_instance = graalsystems.InvoiceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    invoice_id = 'invoice_id_example' # str | Id of the invoice

    try:
        # Find invoice by Id
        api_response = api_instance.find_invoice_by_id(x_tenant, invoice_id)
        print("The response of InvoiceApi->find_invoice_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->find_invoice_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **invoice_id** | **str**| Id of the invoice | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.invoice+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Invoice not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_invoices**
> List[Invoice] find_invoices(x_tenant)

Retrieve all invoices

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.invoice import Invoice
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
    api_instance = graalsystems.InvoiceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all invoices
        api_response = api_instance.find_invoices(x_tenant)
        print("The response of InvoiceApi->find_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->find_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Invoice]**](Invoice.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.invoice+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> Invoice update_invoice(x_tenant, invoice_id, patch)

Update a invoice

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.invoice import Invoice
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
    api_instance = graalsystems.InvoiceApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    invoice_id = 'invoice_id_example' # str | Id of the Invoice
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a invoice
        api_response = api_instance.update_invoice(x_tenant, invoice_id, patch)
        print("The response of InvoiceApi->update_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoiceApi->update_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **invoice_id** | **str**| Id of the Invoice | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.invoice+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Invoice not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

