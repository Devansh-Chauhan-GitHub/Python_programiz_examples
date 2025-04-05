for i in range(1,100001):
    n=i
    temp=n
    sum=0
    while(n>0):
        r=n%10
        sum=sum+pow(r,3)
        n=n//10
    if temp==sum:
        print(f"{sum} is armstrong number")

