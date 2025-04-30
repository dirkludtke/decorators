# simple decorator: logging

def log_function(fun):

    def decorate(*args, **kwargs):
        print(f'calling "{fun.__name__}" with {args} and {kwargs}')
        result = fun(*args, **kwargs)
        print(f'"{fun.__name__}" returned {result}')
        return result

    return decorate

@log_function
def add(x, y):
    return x + y

print(add(1, 1))
print(add(y=3, x=2))
