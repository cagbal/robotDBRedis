#!/usr/bin/python

# Drink Serving Robot Example

from robotDBRedis.modules import User, Module, update_decorator
from robotDBRedis.fields import ListField

class DrinkServingRobotUser(User):
    """docstring for DrinkServingRobotUser.
    This is a custom User to use"""
    @update_decorator
    def __init__(self, name="user", drink_pref_list = [],
                 module_name = "drink_serving_user",
                 host='localhost', port=6379, db=0):
        super(DrinkServingRobotUser, self).__init__(name=name,
                     module_name = module_name,
                     host=host, port=port, db=db)

        self._drink_preferences = \
                self.add_field(ListField("drinks_pref", drink_pref_list))

    def get_drink_prefs(self):
        return self._drink_preferences.get()

class RobotStocks(Module):
    """docstring for RobotStocks.
    This is a custom Module to use"""
    @update_decorator
    def __init__(self, drink_names = [], drink_stocks = [],
                 module_name = "robot_stocks"):
        super(RobotStocks, self).__init__(module_name = module_name)

        if len(drink_names) != len(drink_stocks):
            raise Exception("The length of both lists should be the same")

        self._drink_stocks = \
                self.add_field(ListField("drink_stocks", drink_stocks))

        self._drink_names = \
                self.add_field(ListField("drink_names", drink_names))

    def get_drink_stocks(self):
        return self.get_field_value(self._drink_stocks)

    def get_drink_names(self):
        return self.get_field_value(self._drink_names)

    @update_decorator
    def increment_stock(self, drink_name):

        if isinstance(drink_name, str):
            names = self._drink_names.get_list()
        else:
            raise Exception("Drink name should be a ", str)

        try:
            idx = names.index(drink_name)

            self._drink_stocks.get_list()[idx] = \
                 self._drink_stocks.get_list()[idx] + 1
        except Exception as e:
            raise e

    @update_decorator
    def decrement_stock(self, drink_name):
        if isinstance(drink_name, str):
            names = self._drink_names.get_list()
        else:
            raise Exception("Drink name should be a ", str)

        try:
            idx = names.index(drink_name)

            self._drink_stocks.get_list()[idx] = \
                 self._drink_stocks.get_list()[idx] - 1
        except Exception as e:
            raise e



user = DrinkServingRobotUser("cagatay", ["apple, coffee"])

print(user.get_hash())

stocks =  RobotStocks(["apple", "coffee", "tea"], [0, 10, 100])

print(stocks.get_hash())

print(user.get_drink_prefs())

print(stocks.get_drink_names())

print(stocks.get_drink_stocks())

stocks.increment_stock("apple")

stocks.increment_stock("apple")

stocks.increment_stock("coffee")

stocks.decrement_stock("tea")

print(stocks.get_drink_stocks())

user2 = DrinkServingRobotUser().capture("drink_serving_user:00000")

robot =  RobotStocks().capture("robot_stocks:00000")

print(robot.get_drink_names())

print(robot.get_drink_stocks())
