add(element):
1. When the list is initially created, it is created with a certain capacity.
2. While adding the elements, if the list is filled to the capacity,
   a. Create a new list with increased capacity
   b. Copy the elements of initial list to the new list
3. Add the element to the end of the existing elements in the list
                  
append() method of python list implicitly implements the above algorithm,

