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



# driver code

if __name__ == "__main__":
    # calling the function 
    normal_io()