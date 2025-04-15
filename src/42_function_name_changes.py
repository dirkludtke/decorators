# decorators change the function name

def change_name(function):
    def internal_name(*args, **kwargs):
        return function(*args, **kwargs)
    return internal_name

@change_name
def external_name():
    pass

print(external_name.__name__)

# except one adapts the decorator function

import functools

def dont_change_name(function):
    @functools.wraps(function)
    def internal_name(*args, **kwargs):
        return function(*args, **kwargs)
    return internal_name

@dont_change_name
def external_name():
    pass

print(external_name.__name__)
