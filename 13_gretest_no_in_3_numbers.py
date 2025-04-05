a=int(input("Enter the number A : "))
b=int(input("Enter the number B : "))
c=int(input("Enter the number C : "))
if a>b:
    if a>c:
        print(f"{a} is greatest")
    else:
        print(f"{c} is greatest")
elif b>c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
