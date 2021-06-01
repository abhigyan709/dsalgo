# this is how the append() function works, addition of the element in the list at last 
add(element):
1. When the list is initially created, it is created with a certain capacity.
2. While adding the elements, if the list is filled to the capacity,
   a. Create a new list with increased capacity
   b. Copy the elements of initial list to the new list
3. Add the element to the end of the existing elements in the list
                  
append() method of python list implicitly implements the above algorithm,

# this is how the insert() function works in python data structures, insertion of the element at particular index
insert(pos, element):
 1. If the list is filled to capacity
    a. Create a new list with increased capacity (capacity doubled)
    b. Copy the elements of initial list to the new list
 2. Shift right all the existing elements from index position (pos) by 1 position
 3. Insert the element at index position (pos)
                
insert(pos, element) method in python list implicitly implements the abvove alogorithm to insert the particular item in the list 

infyTQ cousre has some interactve session upon this, 

# so what do you think how the deletion function works?
## here is the logic!
delete(pos):
 1. Shift left all the existing elements from index 
    position (pos+1) by 1 position
Note: Capacity will be decreased whenever remaining number 
of elements fall below certain value
                
list.pop(index) ---> this function will delete the partuicular element from the list


Observations that we observed during the particular array operations: 
    a) here the grocery list is sequence of values
    b) insertion and deletion from the list involves shift operations 
    c) it grows and shrinks in size dynamically based on insertion and deletions

# employee directory system to implement the array 
## when we look up for employee(s) by keying in his/her name in a directory of an organization, it retrieves the objects of all employees whose details have the keyed name in it and stores the employee objects in a list before displaying it. 
### you can see the live exapmle in the array_employeelist.py file

