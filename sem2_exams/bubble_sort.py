def bubble(l1):
    n = len(l1)
    for i in range (n):
        for j in range (n-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
    return l1

print(bubble([4,2,5,6,353,2,52,45,2,53,45,35,3,5]))
