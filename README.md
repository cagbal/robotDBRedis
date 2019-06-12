
# What's going on everybody? robotDBRedis here.

This is a really young repo, so please be open to adventures.

![alt text](https://github.com/cagbal/robotDBRedis/blob/master/imgs/logo.png "robotDBRedis logo" )

## Why does robotDBRedis even exists?
In the intelligent robotics area, the robot should keep track of the basic statistics of the users such as how many drinks served to each people or name of the users also, user preferences. That's why, I wrote robotDBRedis. It's super simple but also it helps. You can also keep track of everything in a sql or redis directly, but you need to know how to use them.  

## Features
- Light
- Few requirements
- Intiutive

## Usage


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
Just inherit the Field class and write get and set methods for the value stored. The value stored should be stored in the self._arg property of the Field class. In the init function, you should accept a field_name and give super class the type of the argument.

Note that the type of objects that can be stored in Redis are limited.

@setter_decorator is checking if you are giving the correct type to setter also it applies deepcopy to the input.

Example custom field:

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

## ROADMAP
1. Complete main functionalities
2. Write all tests
3. Document everything

## LICENSE
MIT
