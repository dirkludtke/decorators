# bounded series of numbers

def is_bounded(start, bound_function, max_steps):
    def create_decorator(fun):
        def decorate(c):
            value = start
            for _ in range(max_steps):
                value = fun(value, c)
                if not bound_function(value):
                    return False
            return True
        return decorate
    return create_decorator

# mandelbrot set

@is_bounded(0, lambda z: abs(z) < 2, 1000)
def mandelbrot_step(z, c):
    return z ** 2 + c

symbols = {True: '*', False: ' '}
for row in range(21):
    i = (row - 10) / 10
    for col in range(61):
        r = (col - 40) / 20
        symbol = symbols[mandelbrot_step(complex(r, i))]
        print(symbol, end='')
    print()
