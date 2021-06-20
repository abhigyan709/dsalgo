# first create an empty list and append the strings into it,
# by taking inputs from user
a = []
list_size = int(input("Please enter the size of List: "))
for i in range(list_size):
    n = str(input("Please enter your desired string: "))
    a.append(n)
print("You entered", a, "as list.")


# now create an another empty list on which the converted string to ascii will be appended
# by taking help of ord() method, which accepts a string of len 1
# the function will convert the string into ASCII codes
# here the extend() function is used to expand strings
b = []
for ele in a:
    b.extend(ord(num) for num in ele)

print("The converted string into the ASCII Character is: ", b)


# now we have created another empty list on which the coverted ASCII code to Binary digit will be appended
c = []
for i in b:
    c.append(bin(i))

print("The coneverted ASCII Characters into Binary digits are: ", c)