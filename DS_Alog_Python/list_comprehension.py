# list comprehensions

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

# lambda function

square = list(map(lambda x: x**2, range(10)))
print(square)