def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("*****MENU*****")
print("1. ADD ")
print("2. Subtratct ")
print("3. Multiplication ")
print("4. Divide ")
choice=int(input("Enter a chooice : "))
a=int(input("Enter Number 1 : "))
b=int(input("Enter Number 2 : "))
if choice == 1:
    print(add(a,b))
if choice == 2:
    print(subtract(a,b))
if choice == 3:
    print(multiply(a,b))
if choice == 4:
    print(divide(a,b))

