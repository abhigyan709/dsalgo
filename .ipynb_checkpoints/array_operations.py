import sys

def list_details(lst):
    print("Capacity o f the list: ", (sys.getsizeof(lst)-36)//4)
    print("Numbers of element in the list: ", len(lst))
    print("Space left in the list: ", ((sys.getsizeof(lst)-36) - len(lst*4))//4)

marias_lst = [] # empty list initiated
print("Empty list created!!")
print("List details: ")
list_details(marias_lst)

marias_lst.append('Sugar')
print(marias_lst)
print("Details after adding first element in the list: ")
list_details(marias_lst)

marias_lst.append('Milk')
print(marias_lst)
print("Details after adding second element in the list: ")
list_details(marias_lst)


# so you can see that how the space in the array list is dynamically being allocated