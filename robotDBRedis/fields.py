#!/usr/bin/python

class Field(object):
    """docstring for Field.
    Base class for all fields"""
    def __init__(self, field_name, arg, type=str):
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

    def set(self, val):
        """
        Should be implemented in child classes
        """
        pass


class TextField(Field):
    """docstring for NameField.
    Just a field containing a string like the name of the object,
    should be a string"""
    def __init__(self, field_name, text="user"):
        super(TextField, self).__init__(field_name, text, str)

    def get(self):
        return self._arg

    def set(self, val):
        self._arg = val

class IntField(Field):
    """docstring for NameField.
    Just a field containing an integer like the id of the object,
     should be an int """
    def __init__(self, field_name, id=0):
        super(IntField, self).__init__(field_name, id, int)

    def get(self):
        return self._arg

    def set(self, val):
        self._arg = val

    def increment(self):
        self._arg = self._arg + 1

    def decrement(self):
        self._arg = self._arg - 1
