def factor(a):
    mylist=[]
    for i in range(1,a+1):
        if a % i ==0:
           mylist.append(i)
    return mylist

a=int(input("Enter a number : "))
for i in factor(a):
    print(i)
