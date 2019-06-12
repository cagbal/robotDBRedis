#!/usr/bin/python
from .fields import TextField, IntField, Field
from .db import Database


class Module(object):
    """Base class for database entries."""
    def __init__(self, module_name, host='localhost', port=6379, db=0, id=0):
        super(Module, self).__init__()

        self._db = Database(host=host, port=port, db=db)

        self.property_list = []

        self._module_name = module_name

        self._id = self.add_field(IntField("id", id))

    def save(self):
        self._db.save()

    def push(self):
        """
        Pushes everything to database without saving it, to save it you should
        use .save() method
        """

        dict_to_push = {}

        for field in self.property_list:
            dict_to_push[field.field_name] = str(field.get()).lower()

        self._db.push(self._module_name + ":" + str(self._id.get()),
                        dict_to_push)

    def add_field(self, field):
        if isinstance(field, Field):
            self.property_list.append(field)
            return field
        else:
            raise Exception('Parameter should be a', Field)

    def get_id(self):
        return self._id.get()


class User(Module):
    """docstring for User.
    Database class for user object. Intended to keep personal
    data of the user and some states"""
    def __init__(self, name="user", module_name = "user", id=0,
                 host='localhost', port=6379, db=0):
        super(User, self).__init__(module_name, host=host, port=port,
                 db=db, id=id)

        self._name = self.add_field(TextField("username", name))
        # count how many times we serve to that person
        self._serve_counter = self.add_field(IntField("serve_count", 0))

        self.push()

    def get_name(self):
        return self._name.get()

    def get_serve_count(self):
        return self._serve_counter.get()

    def increment_serve_count(self):
        self._serve_counter.increment()
