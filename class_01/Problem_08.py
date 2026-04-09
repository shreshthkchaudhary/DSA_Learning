# Find factorial of a number
def factorial (num):
    num=int(input("Input number: "))
    n=1
    for i in range (1,num+1):
        n*=i
    print(f"factorial of {num} is {n}")

factorial(0)