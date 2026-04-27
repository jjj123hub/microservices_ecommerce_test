from utils.db_helper import DBHelper


def test_mysql_connection():
    """测试 MySQL 连接"""
    try:
        db = DBHelper()
        conn = db.connect()
        assert conn is not None
        print("✅ MySQL 连接成功！")
        conn.close()  # 这里改对了！
    except Exception as e:
        print(f"❌ MySQL 连接失败：{e}")
        raise


def test_mysql_select_order():
    """测试从数据库查询订单"""
    db = DBHelper()
    db.connect()

    # 你项目里叫 execute_query，不是 query！
    sql = "SELECT * FROM orders LIMIT 1"
    result = db.execute_query(sql)

    assert len(result) > 0
    print(f"✅ 查询订单成功：{result}")


def test_verify_order_data():
    """测试你项目自带的订单校验方法（最核心！）"""
    db = DBHelper()
    db.connect()

    # 调用项目自带的订单验证方法
    order_data = db.verify_order_data(1)

    assert order_data is not None
    print(f"✅ 订单业务校验成功：{order_data}")