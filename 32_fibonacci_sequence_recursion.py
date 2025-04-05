def fib(a):
    if a<=1:
        return 1
    else:
        return fib(a-1)+fib(a-2)


a=int(input("Enter the range : "))
for i in range(a):
    print(fib(i))
