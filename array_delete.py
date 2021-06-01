import sys

def list_details(lst):
    print("Capacity: ", (sys.getsizeof(lst)-36)//4)
    print("Size of list: ", len(lst))
    print("Space left in the List: ", ((sys.getsizeof(lst)-36) - len(lst*4))//4)

marias_list = []
print("Empty list created!!")
print("List Details: ")
list_details(marias_list)

marias_list.append('Sugar')
marias_list.append('Tea Bags')
marias_list.append('Milk')
marias_list.append('Biscuit')
print(marias_list)
print("New list details: ")
list_details(marias_list)

marias_list.insert(1, 'Salt')
print(marias_list)
print("List Details Final: ")
list_details(marias_list)


marias_list.pop(1)
print("List details after removing salt: ", marias_list)
print("List details: ")
list_details(marias_list)