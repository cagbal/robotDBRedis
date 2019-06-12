#!/usr/bin/python
from .fields import TextField, IntField, Field
from .db import Database


def update_decorator(func):
    def wrapper(self):
        func(self)
        self.push()
    return wrapper


class Module(object):
    """Base class for database entries."""
    def __init__(self, module_name, host='localhost', port=6379, db=0):
        super(Module, self).__init__()

        self.field_list = []

        self._module_name = module_name

        self._db = Database(host=host, port=port, db=db)

        id = self._db.get_unique_id(module_name)

        self._id = self.add_field(IntField("id", id))

        self._hash = self._module_name + ":" + str(self._id.get()).zfill(5)

    def save(self):
        self._db.save()

    def get_hash(self):
        return self._hash

    def capture(self, hash):
        """
        Captures the object with its hash key
        """

        obj = self._db.get_object(hash)

        for p in self.field_list:

            p.set(obj[p.get_field_name()])

    def push(self):
        """
        Pushes everything to database without saving it, to save it you should
        use .save() method
        """

        dict_to_push = {}

        for field in self.field_list:
            dict_to_push[field.get_field_name()] = str(field.get()).lower()

        self._db.push(self._hash, dict_to_push)

    def add_field(self, field):
        if isinstance(field, Field):
            self.field_list.append(field)
            return field
        else:
            raise Exception('Parameter should be a', Field)

    def get_id(self):
        return self._id.get()

    def get_field_value(self, field):
        return self._db.get_field_value(
                        self._hash, field.get_field_name())


class User(Module):
    """docstring for User.
    Database class for user object. Intended to keep personal
    data of the user and some states"""
    def __init__(self, name="user", module_name = "user",
                 host='localhost', port=6379, db=0):
        super(User, self).__init__(module_name, host=host, port=port,
                 db=db)

        # username holder
        self._name = self.add_field(TextField("username", name))

        # count how many times we serve to that person
        self._serve_counter = self.add_field(IntField("serve_count", 0))

        self.push()

    def get_name(self):
        return self.get_field_value(self._name)

    def get_serve_count(self):
        return self.get_field_value(self._serve_counter)

    @update_decorator
    def increment_serve_count(self):
        self._serve_counter.increment()
