def evil_decorator(function):
    def internal_name(*args, **kwargs):
        print('I am extremely evil')
    return internal_name
