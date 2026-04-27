import pymysql
from config.settings import Config

class DBHelper:
    def __init__(self):
        self.connection = None
        
    def connect(self):
        self.connection = pymysql.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        return self.connection
    
    def execute_query(self, query, params=None):
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params or ())
                result = cursor.fetchall()
            conn.commit()
            return result
        finally:
            conn.close()
    
    def execute_update(self, query, params=None):
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                affected_rows = cursor.execute(query, params or ())
            conn.commit()
            return affected_rows
        finally:
            conn.close()
    
    def verify_order_data(self, order_id):
        order = self.execute_query(
            "SELECT * FROM orders WHERE id = %s", (order_id,)
        )
        order_items = self.execute_query(
            "SELECT * FROM order_items WHERE order_id = %s", (order_id,)
        )
        return {"order": order, "order_items": order_items}
