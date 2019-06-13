
# What's going on everybody? robotDBRedis here.

This is a really young repo, so please be open to adventures.
[![codebeat badge](https://codebeat.co/badges/1e4f4aab-918c-473a-837e-937a04926a2a)](https://codebeat.co/projects/github-com-cagbal-robotdbredis-master)

![alt text](https://github.com/cagbal/robotDBRedis/blob/master/imgs/logo.png "robotDBRedis logo" )

## Why does robotDBRedis even exist?
In the intelligent robotics area, the robot should keep track of the basic statistics of the users such as how many drinks served to each people or name of the users also, user preferences. That's why, I wrote robotDBRedis. It's super simple but also it helps. You can also keep track of everything in a sql or redis directly, but you need to know how to use them.  

## Features
- Light
- Few requirements
- Intiutive

## Install

    git clone https://github.com/cagbal/robotDBRedis
    cd robotDBRedis
    sudo apt install redis-server
    (optional) pipenv shell
    pip install -r requirements.txt  
    python setup.py install

## Getting Started

    from robotDBRedis.modules import User
    user_1 = User("mark")
    user_1.push() # Push operation should be done just for once after creation
    user_2 = User("cagatay")
    user_2.push() # Push operation should be done just for once after creation

    # Your robot interacted  with user_1, but not with user_2
    user_1.increment_serve_count()

    print(user_1.get_serve_count()) # 1
    print(user_2.get_serve_count()) # 0

    # Capturing a database entry
    hash = "user:00001"
    user_3 = User.capture(hash)
    user_3.get_id() # 1
    user_3.get_name() # mark

## Modules
Modules are main objects that hold several fields together. For instance, you may want to create a Robot module and a User module for your robotics application to store several data such as how many times did it serve or name of the robot.

### Built-in Modules
1. Abstract Module
   - get_hash() # gets the hash used for redis database
    - capture(hash, host='localhost', port=6379, db=0) # captures the user by using the hash
    - push() # pushes changes to database
    - get_id() # gets the id
    - get_field_value(field) # gets the value of the field
2. User
   - get_name() # gets username
   - get_serve_count() # how many times that people is served
   - increment_serve_count() # increment serve count by 1


### Creating New Modules
You can find a good example in main_example.py. Just inherit Module class, but of course there are some rules.

Whenever you write a method that modifies a data inside a Field, the you must use @update_decorator except constructor. If you use the decorator on \_\_init\_\_ this will cause useless database entries.

You can add built-in IntField, TextField and ListField without any problems, but if you want to add some custom fields into the Module, then you need to dive into the code.

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

`@setter_decorator` is checking if you are giving the correct type to setter also it applies deepcopy to the input.

The most important thing is that .get() method MUST return an object which can be converted into string with `str()` method. For instance, I apply `" ".join([el for el in self._arg])` to ListField.

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
