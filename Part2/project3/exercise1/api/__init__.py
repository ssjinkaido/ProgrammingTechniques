
def factorial(n:int) -> int:
    """
    Returns the factorial of its parameter.

    The factorial of n (written as n!) is equal to n*factorial(n-1) 
    for all n>1. 
    We extend this definition with factorial(0) being equal to 1.
    Factorial is not defined for negative number!
    """
    if n < 0:
        raise ValueError('parameter must be positive integer')

    result = 1

    for i in range(n):
        result *= i+1

    return result


def fibonacci(n):
    """
    Return the nth Fibonacci number.

    Fibonacci numbers are defined by recurrence as:
    - Fibonacci(0) = 0
    - Fibonacci(1) = 0
    - Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2) for n>1
    Notice that it is not defined for negative number!
    """
    if n < 0:
        raise ValueError('parameter must be positive integer')
    
    # we use the matrix version (see wikipedia)
    fib_i1, fib_i2 = 0, 1
    for i in range(0,n):
        fib_i1, fib_i2 = fib_i2 , fib_i1 + fib_i2

    return fib_i1

 
if __name__ == '__main__':
    def try_factorial():
        try:
            factorial(-1)
        except ValueError:
            print('catch exception as expected...')
        for i in range(11):
            print(f'factorial({i}) = {factorial(i)}')
    def try_fibonacci():
        try:
            fibonacci(-1)
        except ValueError:
            print('catch exception as expected...')
        for i in range(20):
            print(f'fibonacci({i}) = {fibonacci(i)}')
    try_factorial()
    try_fibonacci() 
