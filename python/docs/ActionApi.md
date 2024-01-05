# graalsystems.ActionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_action**](ActionApi.md#execute_action) | **POST** /actions | Execute an action


# **execute_action**
> execute_action(x_tenant, action)

Execute an action

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.action import Action
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
    api_instance = graalsystems.ActionApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    action = graalsystems.Action() # Action | 

    try:
        # Execute an action
        api_instance.execute_action(x_tenant, action)
    except Exception as e:
        print("Exception when calling ActionApi->execute_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **action** | [**Action**](Action.md)|  | 

### Return type

void (empty response body)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/vnd.graal.systems.v1.action+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

