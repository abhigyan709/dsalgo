# so we are done with the modular programming
## we added features 
### complexity of program increased 
program became much complex so, 
1. We can see that with our current style of programming, we quickly run into complications trying to simulate real world scenarios, 
2. like purchasing and returning a product.
The problem arises due to the fact that in real life everything has some data/characteristic associated with it and some behavior associated with it and we are not able to replicate this in a code. For example:
a) All mobiles have price and brand as its data and purchase and return as its behavior.
b) All shoes have price and material as its data and purchase and return as its behavior.
We need a way of programming which allows to club together the data and behavior so that it becomes easier to code real world scenarios.
# clubbing the data and its behaviour
OOPs allows to club together the data and behaviour so that it becomes easier to code real world scenarios like real world purchase of mobile and shoe
They will have characterstics, we will have 2 function purchase and return consider the following example, where Mobile and Shoe clubs characterstics as data & purchase(), return() ad its behaviour

## Mobile
    a) Mobile Charactestics -- data
    b) purchase_mobile() -- behaviour
    c) return_mobile()

## Shoe
    a) Shoe Characterstics
    b) purchase_shoe()
    c) return_shoe()
### Templating Approach
Once we have a template of data and the related behavior we can use that template to create many copies
Mobile---|
         |
         |------charachterstics
         |
         |------purchase()
             |
             |--return()

# Obejct Oriented Programming: 
The templating style of programming in which we create template and create copies from that template is called **object oriented programming**

## Classes and Object 
The real world entities which can be described is called an **Object**
Similarly, a class contains the properties/attributes of the object and the operations/behavior that can be performed on an object 

### Mobile
**Attributes**
1. Price
2. Brand

**Behavior**
1. Purchase 
2. Return

### So how we will declare the class or design the class?
have a reference from first program: **class_program_1.py**
to create an object we need a class, the syntax for creating an object is "<classname>()" where <classname> is the name of class
following code implements the object creation
1. Mobile()
2. Mobile()
3. Mobile()

#### Consider the following piece of code
1. 10
2. 10
3. 10
Yes it is valid, we are just creating 3 values in 3 lines without storing them in any variables and also we can't access them
### next version of the programme:


# Reference Variables
we need variables to access and use values, and same we need variables to access and reuse the objects that we create. Such variables that are used to access objects are called **reference variables**

you can see how to access the reference varibles 

### So now? if 2 object is looking same and its having the same values, can we treat it as a single object ?

each object is unique and independent of other object. just like every person, including twins, are unique, so is every object.

refer to the class_program_2.py
you can say that every object have an internal unique ID i.e AADHAR Card/Green Card Number the id will reflect the same concept!

**Creating Attributes and Values of the particular attributes**
this is majorly done by :
reference_variable.attribute_name = value
let's have a particular view upon this in the version 3, class_program_3.py

**Additional Attributes**
The class_program_4.py shows how we can add additional attributes to the object 
this also shows how we can add them to particular obejcts
particular attributes for particular objects


**assigning v/s updating**
you can also update the values of an existing attribute using the dot operator. For example refer to the version 5: class_program_5.py.

# What will happen if you will try to access non-exixting attribute?

you will get an attribute error
see live example in class_program_6.py