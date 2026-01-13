# weknora.KnowledgeApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**knowledge_search_get**](KnowledgeApi.md#knowledge_search_get) | **GET** /knowledge/search | Search knowledge


# **knowledge_search_get**
> Dict[str, object] knowledge_search_get(keyword=keyword, offset=offset, limit=limit)

Search knowledge

Search knowledge files by keyword across all knowledge bases

### Example

* Api Key Authentication (ApiKeyAuth):
* Api Key Authentication (Bearer):

```python
import weknora
from weknora.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = weknora.Configuration(
    host = "/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with weknora.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = weknora.KnowledgeApi(api_client)
    keyword = 'keyword_example' # str | Keyword to search (optional)
    offset = 56 # int | Offset for pagination (optional)
    limit = 56 # int | Limit for pagination (default 20) (optional)

    try:
        # Search knowledge
        api_response = api_instance.knowledge_search_get(keyword=keyword, offset=offset, limit=limit)
        print("The response of KnowledgeApi->knowledge_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->knowledge_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword** | **str**| Keyword to search | [optional] 
 **offset** | **int**| Offset for pagination | [optional] 
 **limit** | **int**| Limit for pagination (default 20) | [optional] 

### Return type

**Dict[str, object]**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search results |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

