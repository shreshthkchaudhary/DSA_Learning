# # Asks for a number and prints the sum of its digits.

def sum_digits (num):
    num=int(input("input number:"))
    print(f"number is {num}")
    sum=0
    while num!=0:
        lastdigit=num%10
        sum=sum+lastdigit
        num=num//10
    print(sum)

sum_digits(0)