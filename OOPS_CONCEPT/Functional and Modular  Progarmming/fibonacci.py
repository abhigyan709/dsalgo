# write a function that returns a list of the numbers of fibonacci series 
# instead of printing it:

def fib(n):
    """
    Return a list containing a set of fibonacci series upto n numbers
    """
    result = [] # it is an empty list
    a, b = 0, 1 # multiple value assigtnment in single line
    while a < n:  # initiating the while loop
        result.append(a) # appending the series in the result list 
        a, b = b, a + b # making the logic of fibonacci series
    return result # returning the result

# f1000 = fib(1000)
# print(f1000)
# print(fib(10))
# print(fib(0))


def fib2(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib2(2000)
fib2(0) # none value is naturally supressed by the interpreter
print(fib2(0)) # but still if you want to return None you can use print()



