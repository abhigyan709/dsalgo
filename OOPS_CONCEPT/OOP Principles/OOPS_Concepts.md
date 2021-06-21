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

#### Mobile
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

# Varibles v/s Attributes

The rules of creating the variables and attributes are same, but we have to treat reference_variable.attribute_name as a variable.

## Variables
    a) Variable_name = variable;
    b) Variable_name = value;
    c) Variable_name = updated_value; #
    d) accessing non existing varibale throws an error
    e) a variable can be assigned to another variable 
    f) variable2 = variable1;

## Attributes
    a) reference_variable.attribute_name = value;
    b) reference_variable.attribute_name = updated_value;
    c) accessing a non-existent attribute throws an error
    d) value of attrubute can be assigned to another value
    e) variable1 = reference_variable1.color;


# Explantion of class_program_7.py
this program will not give an error
However, mob2 will have an attribute ios_versio. This spelling mistake creates a new attribute! Hence be careful when assigning values to attributes of an object.

The best practice is to ensure all objects of a class have the same set of attributes.

Very rarely should we create a new attributes! Hence we will have to be careful upon this.

Also, languages like Java, C# etc do not allow us to create different set of attributes objects like python does.


# Creating common attributes
you have seen the problem arising out of human error in creating atributes individually.
In this we will also face the problem of non-reusable codes.

For example: an object having 10 attributes and we have 10 objects, then we have to write 100 lines of code! There is no reuse at all!

in the next class_program_8.py you will see how to reslove this issue!


# Constructor & Self-Introduction
## Constructor:
When we create an object, the special __init__() method inside the class of that object is invoked automatically. This special function is called as a constructor.

    class Mobile:
        def __init__(self):
            print("Inside Constructor")
    mob1 = Mobile()

we can create a constructor without parameters. but this rarely useful!
See the **class_program_9.py** to see the live example


# Parameterized Constructor
If a constructor takes parameters then it would be called as parameterized constructor.
class_program_10.py will show the live example!



# Prameterless & Parameterized Constructor
If a constructor takes a parameters and if we invoke it with a different number of parameters were missed out or exceeded

see live example in class_program_11.py


# Attribute Creation Using Self: 
By using self.attribute_name and assigning a value we are creating attributes to the current object. The best practice is to create attributes inside the constructor.

## Attribute v/s Local Variable
Attributes can be created only by using the self variable and the dot operator. Without self we are only creating a local vriable an not an attribute.


# Creating behavior in the class
# adding more functions to the class 
but these type of functions should have special parameter called self as the first parameter.

Such functions which describe the behaviour are also called as methods. we can invoke the methods using the dot operation as shown in the live example.
class_program_13.py

even though purchase() is accepting a parameter called self, we need not pass it when we invoke it.


# Method accessing attributes
 we can access an attribute in a method by using self. 
 value of the attribute accessed inside the method is determined by the object used to invoke the method.

 For example, in the code below when we invoke purchase usning mob1, attributes values (Apple and 20000) of mob1 are accessed. see example class_program_14.py file 


 # Invoking methods:
 We can also invoke one method from another using self.

# indentifying invoking objects  

in the below code how does return_product() method know which mobile object we are using?

    class Mobile:
        def __init__(self, price, brand):
            print("Mobile created with id", id(self))
            self.price = price
            self.brand = brand
        
        def return_product(self):
            print("Mobile being returned has id", id(self))
            print("Brand being returned is ", self.brand, " and price is ", self.price)

    mob1 = Mobile(10000, "Apple")
    mob2 = Mobile(1000, "Samsung")
    mob2.return_product()

in the above code snippet, **mob2.return_product()** can also be invoked as **Mobile.return_product(mob2)**.


# Deep Dive into Self & Methods

| Method Invocation | Method Definition | Explanation |
|-------------------|-------------------|-------------|
| mob1.display() | def display(self): print(self.discount) | Here, 'self' is the first parameter. Hence it refers to mob1. |
| mob1.display() | def display(mob_obj): print(mob_obj.discount) | Here, ‘mob_obj' is the first parameter. Hence it refers to ‘mob1'. | 
| mob1.purchase(2) |def purchase(self,qty):print("Total is ",self.price*qty) | Here, 'self' is the first parameter. Hence it refers to ‘mob1'.The second parameter is ‘qty' which stores 2 passed during invocation. |
| mob1.purchase(2) |
| mob1.display() |



# Need for the references:
Live example: what happens to a balloon without the ribbon connecting 