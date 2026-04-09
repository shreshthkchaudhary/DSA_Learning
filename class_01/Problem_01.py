# # for 3 digit number.

num=int(input("input number:"))
print(f"number is {num}")
lastdigit=num%10
print(lastdigit)
secondlastdigit=num//10
thirdlastdigit=secondlastdigit//10
print(thirdlastdigit)
truesecondlastdigit=secondlastdigit-thirdlastdigit*10
print(truesecondlastdigit)
print(f"sum of every digit {lastdigit+truesecondlastdigit+thirdlastdigit}")