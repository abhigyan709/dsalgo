import sys
def listcapacity(lst):
    print("Capacity: ", (sys.getsizeof(lst)-36)//4) # initial capacity of the list
    print("Size: ", len(lst)) # no. of the elements in the list
    print("Space left in the list: ", ((sys.getsizeof(lst)-36) - len(lst*4))//4)

    # some thing is totally depended upon the machines that we use
    # (size-36)/4 == 32 bit machines
    # (size-64)/8 == 64 bit machines
    # 36, 64 == size of empty list based upon machines i.e 32 & 64 bits
    # 4, 8 == size of an element in the list 

maria_lst = [] # an empty list is created
print("Empty list is created!!!")
print("List details: ")
listcapacity(maria_lst)
