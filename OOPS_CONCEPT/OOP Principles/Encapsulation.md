# Encapsulation 
the process of hiding or restrciting the code from directly accessing the sensitive data.

Considering a live example where the customer has a wallet_balance and there are methods which allow us to access and update that balance based on some logic.

# Accessing the private data
## private data access

we can put a lock on that data by adding a double underscore in of it, as shown in the encapsulation_example_3.py

adding a double underscore makes the attribute a private attribute. private attributes are those which are accessible only inside the class. This method of restricting access to our data is called **encapsulation.**

### How does encapsulation work?
when we put a double underscore in front of the attribute name, python will internally change its name to _Classname__attribute.

This is why we get an error when we try to access a private attribute.


### Private data update caution!!
if you try to assign a value to a private variable, we end up creating a new attribute in python.

thus the code in encapsulation_example_5.py, will not give an error but it is logically flawed and doesnot produce the intended result.

### Accessing the private variables
we all know that the name of the variable changes when we make it private, we can access it using its modified name as shown in the encapsulation_example_6.py

**Note**: langueges like Java, C#, etc do not allow access of private variables outside the class.

now the question arises why we use the data encapsulation in python if it is possible to access it from outside the class

## Encapsulation - Just a Caution Sign!

Any lock can be broken by a determined thief. 😁
so in python just because we make our code private, does not mean it is not accessible to other developers. 

When a developer sees a private variable/data, its a gentleman's agreement / understanding that not to access it directly. It is used to only prevent accidental access.

thus in python **Encapsulation** is just a caution sigh rather than a lock.
Meaning that you should not break the rule accidently, but if you want to break it, yes you can proceed. 😉


## Getters & Setters in Python 

To have a error free way of accessing and updating private variables, we create specific methods for this.
    a) the methods which are meant to set a value to a private variable are called **setter methods**
    b) the methods meant to access private variable values are called **getter methods**

encapsulation_example_7.py shows the live example.

### Class Diagram!!
Class diagram is simple and easy to understand. It consists of following parts:
1. name of the class
2. list of attributes
3. list of methods 
4. access specifiers, i.e getter/setters

in a class diagram a (-)ve sign indicates the private access and (+)ve indicates public access.

**Note**
We can create private methods by adding a double underscore in front of it, just like private variables. Also if a method has both leading and trailing double underscores (like __init__, __str__, etc ) it indcates that is a special built-in method.
As per coding standards and rules, we are not supposed to create our own methods with noth leading and trailing underscores.



