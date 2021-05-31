# this is how the append() function works, addition of the element in the list at last 
add(element):
1. When the list is initially created, it is created with a certain capacity.
2. While adding the elements, if the list is filled to the capacity,
   a. Create a new list with increased capacity
   b. Copy the elements of initial list to the new list
3. Add the element to the end of the existing elements in the list
                  
append() method of python list implicitly implements the above algorithm,

insert(pos, element):
 1. If the list is filled to capacity
    a. Create a new list with increased capacity (capacity doubled)
    b. Copy the elements of initial list to the new list
 2. Shift right all the existing elements from index position (pos) by 1 position
 3. Insert the element at index position (pos)
                
insert(pos, element) method in python list implicitly implements the abvove alogorithm to insert the particular item in the list 

infyTQ cousre has some interactve session upon this, 

