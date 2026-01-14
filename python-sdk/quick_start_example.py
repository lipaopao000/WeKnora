#!/usr/bin/env python3
"""
WeKnora Python SDK 快速开始示例
演示如何使用SDK进行基本操作
"""

from weknora_sdk.client import WeKnoraClient
from weknora_sdk.shortcuts import AgentConfig
from weknora_sdk.exceptions import ApiException

def main():
    # 1. 创建客户端
    print("1. 创建WeKnora客户端...")
    client = WeKnoraClient(
        host="http://localhost:8080/api/v1",
        verify_ssl=False,  # 开发环境可以关闭SSL验证
        debug=False
    )
    print("✓ 客户端创建成功\n")
    
    try:
        # 2. 用户登录
        print("2. 用户登录...")
        login_response = client.login(
            username="your_username",
            password="your_password"
        )
        print(f"✓ 登录成功，Token: {login_response.token[:20]}...\n")
        
        # 3. 获取知识库列表
        print("3. 获取知识库列表...")
        knowledge_bases = client.get_knowledge_bases(page=1, page_size=10)
        print(f"✓ 共有 {len(knowledge_bases)} 个知识库")
        for kb in knowledge_bases[:3]:  # 只显示前3个
            print(f"  - {kb.name} (ID: {kb.id})")
        print()
        
        # 4. 创建会话
        print("4. 创建会话...")
        if knowledge_bases:
            kb_ids = [kb.id for kb in knowledge_bases[:2]]  # 使用前2个知识库
            session = client.create_session(
                knowledge_base_ids=kb_ids,
                mode="agent"
            )
            print(f"✓ 会话创建成功，ID: {session.id}\n")
            
            # 5. 发送消息
            print("5. 发送消息...")
            response = client.send_message(
                session_id=session.id,
                content="你好，请介绍一下这个系统",
                stream=False
            )
            print(f"✓ 收到回复:")
            print(f"  {response.content}\n")
            
            # 6. 获取历史消息
            print("6. 获取历史消息...")
            messages = client.get_messages(session_id=session.id)
            print(f"✓ 共有 {len(messages)} 条消息")
            for msg in messages[-2:]:  # 显示最后2条
                print(f"  [{msg.role}] {msg.content[:50]}...")
            print()
            
            # 7. 清理：删除会话
            print("7. 清理资源...")
            client.delete_session(session_id=session.id)
            print("✓ 会话已删除\n")
        else:
            print("⚠ 没有可用的知识库，跳过会话创建\n")
        
        # 8. 登出
        print("8. 用户登出...")
        client.logout()
        print("✓ 登出成功\n")
        
        print("=" * 60)
        print("✓ 所有操作完成！SDK工作正常。")
        print("=" * 60)
        
    except ApiException as e:
        print(f"\n✗ API错误: {e.status} - {e.reason}")
        print(f"  详情: {e.body}")
        print("\n提示: 请确保WeKnora服务正在运行，并且用户名密码正确。")
    except Exception as e:
        print(f"\n✗ 发生错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("=" * 60)
    print("WeKnora Python SDK - 快速开始示例")
    print("=" * 60)
    print("\n注意: 此脚本需要WeKnora服务正在运行")
    print("请修改用户名和密码后再运行\n")
    print("=" * 60 + "\n")
    
    # 取消注释下面这行来运行示例
    # main()
    
    print("提示: 请先修改脚本中的用户名和密码，然后取消注释 main() 调用")
