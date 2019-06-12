#!/usr/bin/python

from copy  import deepcopy

#instance check decorator
def setter_decorator(func):
    def wrapper(self, val):
        if isinstance(val, self._type):
            func(self, deepcopy(val))
        else:
            raise Exception('Parameter should be a', self._type)

    return wrapper

class Field(object):
    """docstring for Field.
    Base class for all fields"""
    def __init__(self, field_name, arg, type=str):
        self._type = type
        if isinstance(arg, type):
            self._arg = arg
        else:
            raise Exception('Parameter should be a', type)

        if isinstance(field_name, str):
            self._field_name = field_name
        else:
            raise Exception('Field name should be a', str)

    def get_field_name(self):
        return self._field_name

    def get(self):
        """
        Should be implemented in child classes
        """
        pass

    @setter_decorator
    def set(self, val):
        """
        Should be implemented in child classes
        """
        pass


class TextField(Field):
    """docstring for NameField.
    Just a field containing a string like the name of the object,
    should be a string"""
    def __init__(self, field_name, arg="user"):
        super(TextField, self).__init__(field_name, arg, str)

    def get(self):
        return self._arg

    @setter_decorator
    def set(self, val):
        self._arg = val

class IntField(Field):
    """docstring for NameField.
    Just a field containing an integer like the id of the object,
     should be an int """
    def __init__(self, field_name, arg=0):
        super(IntField, self).__init__(field_name, arg, int)

    def get(self):
        return self._arg

    @setter_decorator
    def set(self, val):
        self._arg = val


    def increment(self):
        self._arg = self._arg + 1

    def decrement(self):
        self._arg = self._arg - 1

class ListField(Field):
    """docstring for CustomField.
    Just a field containing a custom object """
    def __init__(self, field_name, arg):
        super(ListField, self).__init__(field_name, arg, deepcopy(list))

    def get(self):
        return self._arg

    @setter_decorator
    def set(self, val):
        self._arg = val

    def str(self):
        # Returns a string version of the list
        return " ".join([str(el) for el in self._arg])


class CustomField(Field):
    """docstring for CustomField.
    Just a field containing a custom object """
    def __init__(self, field_name, arg):
        super(CustomField, self).__init__(field_name, deepcopy(arg), type(arg))

    def get(self):
        return self._arg

    @setter_decorator
    def set(self, val):
        self._arg = val
