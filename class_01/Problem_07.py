# Check Armstrong number.

def Armstrong_number(num):
    num=int(input("Input number: "))
    n=num
    digits=len(str(num))
    sum=0
    while num!=0:
        lastdigit=num%10
        sum=sum+lastdigit**digits
        num=num//10
    if sum==n:
        print(f"{n} is Armstrong number")
    else:
        print(f"{n} is not Armstrong number")

Armstrong_number(0)