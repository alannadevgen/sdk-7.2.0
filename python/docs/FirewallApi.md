# graalsystems.FirewallApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_access_by_ip**](FirewallApi.md#check_access_by_ip) | **GET** /firewall/rules/check/{ip} | check access for firewall
[**delete_firewall_rule_by_id**](FirewallApi.md#delete_firewall_rule_by_id) | **DELETE** /firewall/rules/{ruleId} | Delete a rule by its id
[**find_firewall_rule_by_firewall_rule_id**](FirewallApi.md#find_firewall_rule_by_firewall_rule_id) | **GET** /firewall/rules/{ruleId} | Find rule by Id
[**find_firewall_rules**](FirewallApi.md#find_firewall_rules) | **GET** /firewall/rules | Retrieve all firewall rules
[**update_firewall_rule**](FirewallApi.md#update_firewall_rule) | **PATCH** /firewall/rules/{ruleId} | Update a rule


# **check_access_by_ip**
> FirewallCheckStatus check_access_by_ip(x_tenant, ip)

check access for firewall

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.firewall_check_status import FirewallCheckStatus
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
    api_instance = graalsystems.FirewallApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    ip = 'ip_example' # str | Input IP

    try:
        # check access for firewall
        api_response = api_instance.check_access_by_ip(x_tenant, ip)
        print("The response of FirewallApi->check_access_by_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->check_access_by_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **ip** | **str**| Input IP | 

### Return type

[**FirewallCheckStatus**](FirewallCheckStatus.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.firewall.rule+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | FirewallRule not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_rule_by_id**
> delete_firewall_rule_by_id(x_tenant, rule_id)

Delete a rule by its id

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
    api_instance = graalsystems.FirewallApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    rule_id = 'rule_id_example' # str | Id of the FirewallRule

    try:
        # Delete a rule by its id
        api_instance.delete_firewall_rule_by_id(x_tenant, rule_id)
    except Exception as e:
        print("Exception when calling FirewallApi->delete_firewall_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **rule_id** | **str**| Id of the FirewallRule | 

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
**404** | FirewallRule not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_firewall_rule_by_firewall_rule_id**
> FirewallRule find_firewall_rule_by_firewall_rule_id(x_tenant, rule_id)

Find rule by Id

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.firewall_rule import FirewallRule
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
    api_instance = graalsystems.FirewallApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    rule_id = 'rule_id_example' # str | Id of the FirewallRule

    try:
        # Find rule by Id
        api_response = api_instance.find_firewall_rule_by_firewall_rule_id(x_tenant, rule_id)
        print("The response of FirewallApi->find_firewall_rule_by_firewall_rule_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->find_firewall_rule_by_firewall_rule_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **rule_id** | **str**| Id of the FirewallRule | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.firewall.rule+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | FirewallRule not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_firewall_rules**
> List[FirewallRule] find_firewall_rules(x_tenant)

Retrieve all firewall rules

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.firewall_rule import FirewallRule
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
    api_instance = graalsystems.FirewallApi(api_client)
    x_tenant = 'x_tenant_example' # str | 

    try:
        # Retrieve all firewall rules
        api_response = api_instance.find_firewall_rules(x_tenant)
        print("The response of FirewallApi->find_firewall_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->find_firewall_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 

### Return type

[**List[FirewallRule]**](FirewallRule.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.graal.systems.v1.firewall.rule+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_rule**
> FirewallRule update_firewall_rule(x_tenant, rule_id, patch)

Update a rule

### Example

* OAuth Authentication (internal):

```python
import time
import os
import graalsystems
from graalsystems.models.firewall_rule import FirewallRule
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
    api_instance = graalsystems.FirewallApi(api_client)
    x_tenant = 'x_tenant_example' # str | 
    rule_id = 'rule_id_example' # str | Id of the FirewallRule
    patch = [graalsystems.Patch()] # List[Patch] | The patch

    try:
        # Update a rule
        api_response = api_instance.update_firewall_rule(x_tenant, rule_id, patch)
        print("The response of FirewallApi->update_firewall_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->update_firewall_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_tenant** | **str**|  | 
 **rule_id** | **str**| Id of the FirewallRule | 
 **patch** | [**List[Patch]**](Patch.md)| The patch | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[internal](../README.md#internal)

### HTTP request headers

 - **Content-Type**: application/json-patch+json;charset=UTF-8
 - **Accept**: application/vnd.graal.systems.v1.firewall.rule+json, application/vnd.graal.systems.v1.error+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**404** | Job not found |  -  |
**405** | Method Not Allowed |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

