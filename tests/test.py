#!/usr/bin/python
import unittest

import redis

from robotDBRedis.modules import User, Module
from robotDBRedis.fields import IntField, TextField, ListField, CustomField
from robotDBRedis.db import Database

def flushall():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.flushall()


class UserTest(unittest.TestCase):

    def test_user_name(self):
        flushall()

        user0 = User("Cagatay")
        user0.push()
        user1 = User("Mark")
        user1.push()
        user2 = User("Daisy")
        user2.push()
        user3 = User("Baron")
        user3.push()
        user4 = User("Bruno")
        user4.push()
        user5 = User("Bazzi")
        user5.push()
        user6 = User("Jacob")
        user6.push()

        self.assertEqual(user0.get_name(), "cagatay")
        self.assertEqual(user1.get_name(), "mark")
        self.assertEqual(user2.get_name(), "daisy")
        self.assertEqual(user3.get_name(), "baron")
        self.assertEqual(user4.get_name(), "bruno")
        self.assertEqual(user5.get_name(), "bazzi")
        self.assertEqual(user6.get_name(), "jacob")


    def test_user_hash(self):
        flushall()

        user0 = User("Cagatay")
        user0.push()
        user1 = User("Mark")
        user1.push()
        user2 = User("Daisy")
        user2.push()
        user3 = User("Baron")
        user3.push()
        user4 = User("Bruno")
        user4.push()
        user5 = User("Bazzi")
        user5.push()
        user6 = User("Jacob")
        user6.push()


        self.assertEqual(user2.get_hash(), "user:00002")
        self.assertEqual(user3.get_hash(), "user:00003")
        self.assertEqual(user4.get_hash(), "user:00004")
        self.assertEqual(user5.get_hash(), "user:00005")
        self.assertEqual(user6.get_hash(), "user:00006")

    def test_serve_increment(self):
        flushall()

        user0 = User("Cagatay")
        user0.push()
        user1 = User("Mark")
        user1.push()

        user0.increment_serve_count()
        user0.increment_serve_count()
        user0.increment_serve_count()

        self.assertEqual(user0.get_serve_count(), "3")
        self.assertEqual(user1.get_serve_count(), "0")

    def test_capture_module(self):
        flushall()

        user0 = User("Cagatay")
        user0.push()
        user1 = User("Mark")
        user1.push()

        user00 = User.capture("user:00001")

        self.assertEqual(user1.get_id(), 1)
        self.assertEqual(user1.get_name(), "mark")
        self.assertEqual(user1.get_serve_count(), "0")




class DatabaseTest(unittest.TestCase):
    def test_hash_increment(self):
        flushall()

        user0 = User("Cagatay")#
        user0.push()
        user1 = User("Mark")
        user1.push()

        user0._db.hash_increment(user0.get_hash(),
                                user0._serve_counter.get_field_name())

        user1._db.hash_increment(user1.get_hash(),
                                user1._serve_counter.get_field_name(), 145)

        self.assertEqual(user0.get_serve_count(), "1")
        self.assertEqual(user1.get_serve_count(), "145")

    def test_get_all(self):
        flushall()

        user0 = User("Cagatay")#
        user0.push()
        user1 = User("Mark")
        user1.push()

        db = Database()

        self.assertTrue({'id': '1', 'username': 'mark', 'serve_count': '0'} in
                        db.get_objects_by_module_name("user"))
        self.assertTrue({'id': '0', 'username': 'cagatay', 'serve_count': '0'} in
                        db.get_objects_by_module_name("user"))


class FieldTests(unittest.TestCase):
    def test_int_field(self):
        f = IntField("random_name", 5)

        self.assertEqual(f.get(), 5)

        f.set(-123)

        self.assertEqual(f.get(), -123)

        f.increment()

        self.assertEqual(f.get(), -122)

        f.decrement()

        self.assertEqual(f.get(), -123)

    def test_text_field(self):
        f = TextField("random_name", "cagatay")

        self.assertEqual(f.get(), "cagatay")

        f.set("mark")

        self.assertEqual(f.get(), "mark")

    def test_list_field(self):
        f = ListField("random_name", [1,2,3,4])

        self.assertEqual(f.get_list(), [1,2,3,4])

        # Deep copy test

        L = [1,2,3,4,5]

        f.set(L)

        L.append(100)

        self.assertNotEqual(f.get_list(), L)

        # Str conversion test

        L = [1,2,3,4,5]

        f.set(L)

        self.assertEqual(f.get(), " ".join([str(el) for el in L]))


    def test_custom_field(self):
        class A(object):
            """docstring for A."""
            def __init__(self, arg):
                super(A, self).__init__()
                self.arg = arg

        custom_class_instance = A(3)

        f = CustomField("random_name", custom_class_instance)

        self.assertEqual(f.get().arg, custom_class_instance.arg)

        custom_class_instance.arg = 5

        self.assertNotEqual(f.get().arg, custom_class_instance.arg)
