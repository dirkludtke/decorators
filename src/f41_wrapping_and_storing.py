# wrapping functions with decorator

def wrap_decorator(function):
    def wrap_decorate(*args, **kwargs):
        print(f'wrap_decorate {function.__name__} {args} {kwargs}')
        return function(*args, **kwargs)
    return wrap_decorate

@wrap_decorator
def wrap_decorated(greeting):
    print(f'{greeting} wrap_decorated')

wrap_decorated('Hello')

# wrapping functions old school

def wrap_old_school(function, *args, **kwargs):
    print(f'wrap_old_school {function.__name__} {args} {kwargs}')
    return function(*args, **kwargs)

def old_school(greeting):
    print(f'{greeting} old_school')

wrap_old_school(old_school, 'Hello')

# storing functions with decorator

decorator_store = {}
def store_decorator(key):
    def create_decorator(function):
        decorator_store[key] = function
        return function
    return create_decorator

@store_decorator('my_function')
def store_decorated(greeting):
    print(f'{greeting} decorator_registered')

print(decorator_store)

# storing functions old school

old_school_store = {}
def store_old_school(key, function):
    old_school_store[key] = function

store_old_school('my_function', old_school)
print(old_school_store)

# wrapping and storing functions with decorator

@wrap_decorator
@store_decorator('my_function')
def wrap_and_store_decorated(greeting):
    print(f'{greeting} wrap_and_store_decorated')

wrap_and_store_decorated('Good bye')
print(decorator_store)

# wrapping and storing functions old school

wrap_old_school(old_school, 'Good bye')
store_old_school('my_function', old_school)
print(old_school_store)
