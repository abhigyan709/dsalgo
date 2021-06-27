if __name__ == '__main__':
    s = input()
    
if any(c.isalnum() for c in s) == True:
    print(True)
else:
    print(False)

if any(c.isalpha() for c in s) == True:
    print(True)
else:
    print(False)

if any(c.isdigit() for c in s) == True:
    print(True)
else:
    print(False)
    
if any(c.lower() for c in s) == True:
    print(True)
else:
    print(False)
    
if any(c.upper() for c in s) == True:
    print(True)
else:
    print(False)

