# # Asks for a number and prints the REVERSE of its digits.

def reverse(num):
    num=int(input("input number:"))
    print(f"number is {num}")
    rev=0
    while num!=0:
        lastdigit=num%10
        rev=rev*10+lastdigit
        num=num//10
    print(rev)
reverse(0)