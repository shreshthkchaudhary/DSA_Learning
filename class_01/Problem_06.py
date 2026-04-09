# Count number of digits in a number

def count(num):
    num=int(input("Input Number: "))
    count=0
    while num!=0:
        count=count+1
        num=num//10
    print(count)

count(0)