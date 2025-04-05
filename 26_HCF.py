a=int(input("Enter a Integear : "))
mylist=[]
for i in range(1,a+1):
    if a % i ==0:
        mylist.append(i)
print(mylist)
