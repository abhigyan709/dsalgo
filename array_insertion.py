import sys

def list_details(lst):
    print("Capacity of the list: ", (sys.getsizeof(lst)-36)//4)
    print("Length of the list i.e Size: ", len(lst))
    print("Space left in the list: ", ((sys.getsizeof(lst)-36)- len(lst*4))//4)

marias_list = [] # empty list initiatied
print("Empty list created!!")
print("List details: ")
list_details(marias_list)

# all ok 
marias_list.append('Sugar')
marias_list.append('Milk')
marias_list.append('Tea')
marias_list.append('Rice')

# calling the details of the list
print("Shopping list: ", marias_list)
print("List details: ")
list_details(marias_list)

# insert operation in python ds list array
marias_list.insert(1, 'Salt')
print("New Shopping list: ", marias_list)
print("New List Details: ")
list_details(marias_list)