#!/usr/bin/python
import unittest


from robotDBRedis.modules import User

class CreateAUserTest(unittest.TestCase):
    def test_name(self):
        user = User("Cagatay")
        self.assertEqual(user.get_name(), "cagatay")
