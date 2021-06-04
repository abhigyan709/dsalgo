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