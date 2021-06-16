fruits = ["orange", 'apple', "pear", "banana", "kiwi", "apple", "banana"]

# count
# work: return number of times x appears in the list
fruits.count("apple")
fruits.count("grapes")

# index
# work: tells the index of particular item 
fruits.index("kiwi")

# reverse function 
# work: reverse the elements of the list in place
fruits[::-1] # only returns the reversed list
fruits.reverse() # reversed the particular list permanently
fruits

# sort function --> based upon tim sort algorithm
fruits.sort()
print(fruits)

# fruits = ["orange", 'apple', "pear", "banana", "kiwi", "apple", "banana"]
# pop function

fruits.pop(3)
fruits.pop() # returns the removed item

fruits
fruits.remove("apple")
fruits


