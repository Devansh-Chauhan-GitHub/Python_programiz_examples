a=int(input("Enter a number 1 : "))
b=int(input("Enter a number 2 : "))
if a>b:
    greatest=a
else:
    greatest=b
for i in range(greatest,a*b+1):
    if (i % a ==0) and (i % b ==0):
        print(i)
        break
