# functions as function arguments

def function1a():
    print('function1a started and finished')

def function1b():
    print('function1b started and finished')

def function2(fun):
    print('function2 started')
    fun()
    print('function2 finished')

function2(function1a)
function2(function1b)

# functions as return values

def function1(opp):
    def function2(a, b):
        if opp == "*":
            return a * b
        return a + b
    return function2

mul = function1('*')
add = function1('+')

print('mul(3, 4) =', mul(3, 4))
print('add(3, 4) =', add(3, 4))
