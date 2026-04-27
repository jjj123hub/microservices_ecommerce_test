from utils.db_helper import DBHelper
from utils.redis_helper import RedisHelper

def test_mysql_with_redis_cache():
    """
    最终大BOSS测试：
    1. 先查Redis
    2. 没有 → 查MySQL
    3. 把MySQL结果写入Redis
    4. 下次直接读Redis
    """
    redis = RedisHelper()
    db = DBHelper()
    order_id = 1

    # 1. 先从Redis取
    cache_data = redis.get(f"order:{order_id}")
    print(f"🔍 Redis读取结果: {cache_data}")

    # 2. Redis没有 → 从MySQL查
    if not cache_data:
        print("🔄 Redis未命中，查询MySQL...")
        db.connect()
        mysql_data = db.verify_order_data(order_id)
        print(f"✅ MySQL查询结果: {mysql_data}")

        # 3. 写入Redis缓存
        redis.set(f"order:{order_id}", str(mysql_data), ex=60)
        print("✅ 数据已写入Redis缓存")

    # 4. 再次从Redis取（一定有）
    cache_data_2 = redis.get(f"order:{order_id}")
    assert cache_data_2 is not None
    print(f"✅ 第二次Redis读取（命中）: {cache_data_2}")

    print("\n🏆【Redis + MySQL 联动成功！】")