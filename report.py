
# coding: utf-8

# In[ ]:

def get_description(): # see the docstring below?
    """Return random weather, just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows do you?']
    return choice(possibilities)

