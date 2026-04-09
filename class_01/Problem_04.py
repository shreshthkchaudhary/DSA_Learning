# # Asks for a number and check its PALINDROME or not.

def palindrome (num):
    num=int(input("input number:"))
    n=num
    print(f"number is {num}")
    rev=0
    while num!=0:
        lastdigit=num%10
        rev=rev*10+lastdigit
        num=num//10
    if n==rev:
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not palindrome")

palindrome(0)