# graalsystems.StripeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stripe_create_setup_intent**](StripeApi.md#stripe_create_setup_intent) | **POST** /stripe/create-setup-intent | create setup intent on Stripe
[**stripe_public_key**](StripeApi.md#stripe_public_key) | **GET** /stripe/public-key | get Stripe public key


# **stripe_create_setup_intent**
> StripeCreateSetupIntent200Response stripe_create_setup_intent(x_tenant)

create setup intent on Stripe

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.stripe_create_setup_intent200_response import StripeCreateSetupIntent200Response
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
    api_instance = graalsystems.StripeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # create setup intent on Stripe
        api_response = api_instance.stripe_create_setup_intent(x_tenant)
        print("The response of StripeApi->stripe_create_setup_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_create_setup_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**StripeCreateSetupIntent200Response**](StripeCreateSetupIntent200Response.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stripe_public_key**
> StripePublicKey200Response stripe_public_key(x_tenant)

get Stripe public key

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.stripe_public_key200_response import StripePublicKey200Response
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
    api_instance = graalsystems.StripeApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # get Stripe public key
        api_response = api_instance.stripe_public_key(x_tenant)
        print("The response of StripeApi->stripe_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StripeApi->stripe_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**StripePublicKey200Response**](StripePublicKey200Response.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

