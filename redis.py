import redis


class RedisClient(redis.Redis):
    def __init__(self, prefix, host='localhost', port=6379, db=0, **kwargs):
        self.prefix = prefix
        super().__init__(host=host, port=port, db=db, **kwargs)

    def get(self, name, default=None):
        """
        如果有default,则会自动转换
        Args:
            name:
            default:

        Returns:

        """
        r = super(RedisClient, self).get(self.prefix + name)
        if r is None:
            return default
        else:
            r = r.decode('utf-8')
            if isinstance(default, int):
                return int(r)
            return r

    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        return super(RedisClient, self).set(self.prefix + name, value, ex, px, nx, xx)
