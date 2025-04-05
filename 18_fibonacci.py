a=0
b=1
print(a,b,sep=",",end=",")
for i in range(1,11):
    c=a+b
    a=b
    b=c
    print(c,end=",")
