# python program to illustrate fast input and output
import io, os, time
# function to take a normal input 

def normal_io():

    # stores the start time 
    start = time.perf_counter()

    # take input 
    s = input().strip();
    
    # stores the end time
    end = time.perf_counter()

    # print the time taken
    print("\nTime taken in normal I / O: ", end - start)


def fast_io():
    # reinitialize the input function 
    # to take input from the byte like
    # objects 
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    # fast input / input 
    start = time.perf_counter()

    # taking input as string 

    s = input().decode()

    # stores the end time

    end = time.perf_counter()

    # print the time taken
    print("\nTime taken in fast I/O: ", end - start)


    pass


if __name__ == "__main__":
    # calling the function 
    normal_io()

    fast_io()