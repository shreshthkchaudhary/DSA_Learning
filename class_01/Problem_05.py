# # Asks for a number and check its PRIME or not.

# def prime (num):
#     num=int(input("input number:"))
#     print(f"number is {num}")
#     for i in range(2,num):
#         if num%i==0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
        
# prime(0)



# def isPrime(self, n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#             break
#         else:
#             return True
# isPrime(10)

def isPrime(n):
    if n<=1:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            
        return True
print(isPrime(25))