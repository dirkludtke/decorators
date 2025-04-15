# decorator with args: repeat

def repeat(n: int):
    def create_decorator(fun):
        def decorate(value):
            for _ in range(n):
                value = fun(value)
            return value
        return decorate
    return create_decorator

@repeat(5)
def plus_one(n):
    return n + 1
print('plus one repeated 5 times:', plus_one(0))

# combined decorators: nested repeat

@repeat(5)
@repeat(5)
@repeat(5)
def plus_one_c(n):
    return n + 1

print('plus one repeated 5 * 5 * 5 times:', plus_one_c(0))

# combined decorators: nested decoration

def repeat2(n: int, m: int):
    @repeat(m)
    def create_decorator(fun):
        @repeat(n)
        def decorate(value):
            return fun(value)
        return decorate
    return create_decorator

@repeat2(5, 4)
def plus_one_c(n):
    return n + 1

print('plus one repeated 5 ** 4 times:', plus_one_c(0))
