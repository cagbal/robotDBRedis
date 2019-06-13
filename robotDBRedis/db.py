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

    def get_field_value(self, hash, field_name):
        return self._redis.hget(hash, field_name).decode("utf-8")

    def get_object(self, hash):
        d = self._redis.hgetall(hash)

        d2 = dict((k.decode("utf-8"),
             v.decode("utf-8")) for k, v in d.items())

        return d2

    def get_objects_by_module_name(self, module_name):
        keys = self._redis.keys(module_name + "*")

        l = []

        for key in keys:
            l.append(self.get_object(key.decode("utf-8")))

        print(l)

        return l


    def hash_increment(self, hash, field_name,increment=1):
        self._redis.hincrby(hash, field_name, increment)

    def get_unique_id(self, module_name):
        keys = []
        if isinstance(module_name, str):
            keys = self._redis.keys(module_name + "*")
        else:
            raise Exception("Module name should be a type of", str)

        if keys:
            last_key = sorted(keys)[-1].decode("utf-8")
            last_id = last_key.split(":")[-1]

            return int(last_id) + 1
        else:
            return 0

    def clear(self):
        """
        Clears everything in the database
        """
        self._redis.flushall()
