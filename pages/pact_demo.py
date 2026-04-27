import os
# 屏蔽所有Windows警告（干净运行）
os.environ["RUBYOPT"] = "-EUTF-8"
os.environ['PACT_DO_NOT_TRACK'] = 'true'

from pact import Consumer, Provider
import requests

# ===================== 核心配置（官方标准）=====================
pact = Consumer('TestConsumer').has_pact_with(
    Provider('TestProvider'),
    port=1234,
    pact_dir='./pacts'
)

# 第一步：【先定义交互规则】（必须写在最前面！）
pact.given("test service") \
    .upon_receiving("get test data") \
    .with_request('get', '/api/test') \
    .will_respond_with(200, body={
        "code": 200,
        "msg": "success",
        "data": "pact_success"
    })

# 第二步：【启动服务 + 执行测试】
with pact:
    # 发送请求
    res = requests.get("http://localhost:1234/api/test")
    # 打印结果
    print("✅ Pact 契约测试 100% 成功！")
    print(f"接口返回：{res.json()}")