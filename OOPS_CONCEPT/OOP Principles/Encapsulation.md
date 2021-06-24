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