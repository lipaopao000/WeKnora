import weknora
from weknora.rest import ApiException
from pprint import pprint

# 定义配置
configuration = weknora.Configuration(
    host="http://localhost/api/v1"
)

# 如果有 API Key，可以在这里配置
# configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'

# 进入上下文管理器创建 API 实例
with weknora.ApiClient(configuration) as api_client:
    # 创建 DefaultApi 实例（包含 /system/info）
    api_instance = weknora.DefaultApi(api_client)
    
    try:
        # 获取系统信息
        api_response = api_instance.system_info_get()
        print("The response of DefaultApi->system_info_get:")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->system_info_get: %s\n" % e)
    except Exception as e:
        # 因为服务可能没启动，捕获网络错误是预期的
        print(f"Captured expected error (service might not be running): {e}")
