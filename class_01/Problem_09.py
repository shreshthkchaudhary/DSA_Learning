# Print all prime numbers between 1 and N
def find (n):
    n=int(input("input number:"))
    for num in range(1,n+1):
        if_prime = True
        for i in range(2,num):
            if num%i==0:
                if_prime = False
                break
        if if_prime:
            print(num, end=" ")

find(0)