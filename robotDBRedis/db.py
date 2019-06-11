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
