from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    name='robotDBRedis',

    version='1.0',

    description='A small python module to handle DB operations for robots',

    author='Cagatay Odabasi',

    author_email='cagatayodabasi91@gmail.com',

    packages=['robotDBRedis'],

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/cagbal/robotDBRedis",

)
