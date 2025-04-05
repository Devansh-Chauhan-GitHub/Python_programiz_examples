r=int(input("Give a range of numbers : "))
n=int(input("Number to be divisible by : "))
req_list=list(filter(lambda x: x % n == 0 ,range(r)))
for i in req_list:
    print(i)
