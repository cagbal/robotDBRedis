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

    def push(self, key, dict):
        """
        Pushes everything to database without saving it, to save it you should
        use .save() method
        """
        # TODO: Burasi degisecek

        dict_to_push = {}

        for field in self.property_list:
            dict_to_push[field.field_name] = field.get()

        if dict_to_push:
            self._redis.hmset(self._module_name + ":" + str(self._id.get()),
                             dict_to_push)

        print(dict_to_push)
