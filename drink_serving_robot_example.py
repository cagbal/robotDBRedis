#!/usr/bin/python

# Drink Serving Robot Example

from robotDBRedis.modules import User
from robotDBRedis.fields import ListField

class DrinkServingRobotUser(User):
    """docstring for DrinkServingRobotUser.
    This is a custom User to use"""
    def __init__(self, name="user", drink_pref_list = [],
                 module_name = "drink_serving_user",
                 host='localhost', port=6379, db=0):
        super(DrinkServingRobotUser, self).__init__(name=name,
                     module_name = module_name,
                     host=host, port=port, db=db)

        self._drink_preferences = \
                self.add_field(ListField("drinks_pref", drink_pref_list))

        self.push()

    def get_drink_prefs(self):
        return self._drink_preferences.get()


user = DrinkServingRobotUser("cagatay", ["apple, coffee"])

print(user.get_drink_prefs())
