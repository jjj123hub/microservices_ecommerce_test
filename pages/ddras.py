import redis

# 连接本地Redis（默认端口6379，无密码）
client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True  # 自动解码字符串，不用手动转bytes
)

# 测试：写入+读取数据
client.set("test_key", "hello_redis")
value = client.get("test_key")

# 打印结果
print("✅ Redis 连接成功！")
print(f"读取到的值：{value}")