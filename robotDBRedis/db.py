#!/usr/bin/python

import redis

class Database(object):
    """Database object for redis operations"""
    def __init__(self, host='localhost', port=6379, db=0, id=0):
        super(Database, self).__init__()
        self._redis = redis.Redis(host=host, port=port, db=db)

    def __del__(self):
        self._redis.save()

    def save(self):
        self._redis.save()

    def push(self, key, dict_to_push):
        """
        Pushes everything to database without saving it, to save it you should
        use .save() method
        """
        if isinstance(dict_to_push, dict):
            self._redis.hmset(key, dict_to_push)
        else:
            raise Exception("Parameter should be a", dict)

    def hash_increment(self, hash, field_name,incement=1):
        self._redis.hincrby(hash, field_name, increment)
