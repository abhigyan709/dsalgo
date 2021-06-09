# default argument values

def ask_ok(prompt, retries = 4, reminder = 'Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?', 2, 'Only yes or no!')


# explaination of in keyword:
"""
this test whether or not a sequence contains a certain values
"""


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
