#!/usr/bin/python
import unittest

import redis

from robotDBRedis.modules import User

def flushall():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.flushall()


class UserTest(unittest.TestCase):

    def test_user_name(self):
        flushall()

        user0 = User("Cagatay")
        user1 = User("Mark")
        user2 = User("Daisy")
        user3 = User("Baron")
        user4 = User("Bruno")
        user5 = User("Bazzi")
        user6 = User("Jacob")

        self.assertEqual(user0.get_name(), "cagatay")
        self.assertEqual(user1.get_name(), "mark")
        self.assertEqual(user2.get_name(), "daisy")
        self.assertEqual(user3.get_name(), "baron")
        self.assertEqual(user4.get_name(), "bruno")
        self.assertEqual(user5.get_name(), "bazzsi")
        self.assertEqual(user6.get_name(), "jacob")



    def test_user_hash(self):
        flushall()

        user0 = User("Cagatay")
        user1 = User("Mark")
        user2 = User("Daisy")
        user3 = User("Baron")
        user4 = User("Bruno")
        user5 = User("Bazzi")
        user6 = User("Jacob")

        self.assertEqual(user0.get_hash(), "user:00000")
        self.assertEqual(user1.get_hash(), "user:00001")
        self.assertEqual(user2.get_hash(), "user:00002")
        self.assertEqual(user3.get_hash(), "user:00003")
        self.assertEqual(user4.get_hash(), "user:00004")
        self.assertEqual(user5.get_hash(), "user:00005")
        self.assertEqual(user6.get_hash(), "user:00006")
