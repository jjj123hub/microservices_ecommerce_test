import redis
from config.settings import Config

class RedisHelper:
    def __init__(self):
        self.client = redis.Redis(
            host=Config.REDIS_HOST,
            port=Config.REDIS_PORT,
            db=Config.REDIS_DB,
            decode_responses=True
        )
        
    def get(self, key):
        return self.client.get(key)
        
    def set(self, key, value, ex=None):
        return self.client.set(key, value, ex=ex)
        
    def delete(self, key):
        return self.client.delete(key)
        
    def get_hot_keys(self, pattern="*", count=10):
        keys = self.client.keys(pattern)
        hot_keys = []
        for key in keys:
            try:
                ttl = self.client.ttl(key)
                hot_keys.append({"key": key, "ttl": ttl})
            except:
                pass
        return sorted(hot_keys, key=lambda x: x["ttl"])[:count]
        
    def incr(self, key):
        return self.client.incr(key)
