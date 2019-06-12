
# What's going on everybody? robotDBRedis here.

The code is not ready for anything, please stay away from this repo :) or
just clone it to get into trouble.

![alt text](https://github.com/cagbal/robotDBRedis/blob/master/imgs/logo.png "robotDBRedis logo" )


## ROADMAP
1. Complete main functionalities
2. Write all tests
3. Document everything


## Fields
Fields are data holders. For instance, you should use a TextField to store the
name of the user or the object. Each field also has a name, for instance, you
want to store a counter inside of your object. Then, you should create a IntField
with a name of "counter".  

### Built-in Fields
1. Abstract Field
   - get_field_name() # Returns the name of the field
2. IntField
   - get() # Returns the value stored in the field
   - set() # Sets the value stored in the field
   - increment() # Increments the value stored in the field
   - decrement() # Decrements the value stored in the field
3. TextField
   - get() # Returns the value stored in the field
   - set() # Sets the value stored in the field

### Creating New Fields
Just inherit the Field class and write get and set methods for the value stored. The value stored should be stored in the \_arg property of the Field class. In the init function, you should accept a field_name and give super class the type of the argument.

Note that the type of objects that can be stored in Redis are limited.

Example custom field:

    class CustomField(Field):
    """docstring for NameField.
    Just a field containing a custom object """
    def __init__(self, field_name, arg):
        super(CustomField, self).__init__(field_name, arg, type(arg))

    def get(self):
        return self._arg

    def set(self, val):
        self._arg = val
