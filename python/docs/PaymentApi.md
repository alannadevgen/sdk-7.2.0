# graalsystems.PaymentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_payments**](PaymentApi.md#find_payments) | **GET** /payments | Retrieve all payments


# **find_payments**
> List[Payment] find_payments(x_tenant)

Retrieve all payments

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.payment import Payment
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
    api_instance = graalsystems.PaymentApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all payments
        api_response = api_instance.find_payments(x_tenant)
        print("The response of PaymentApi->find_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->find_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[Payment]**](Payment.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.payment+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

