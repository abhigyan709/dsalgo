"""In the previous seen we have a look of how input in STDIN mode works"""

# fast output

import sys, time

def normal_out():

    start = time.perf_counter()
    n = 5
    print(n)
    s = "Abhigyan"
    print(s)

    arr = [1, 2, 3, 4]
    print(arr)

    end = time.perf_counter()

    print("\nTime taken in Normal Output: ", end - start)

# function for fast output
def fast_out():

    start = time.perf_counter()
    n = 5
    sys.stdout.write(str(n)+"\n")

    # output string