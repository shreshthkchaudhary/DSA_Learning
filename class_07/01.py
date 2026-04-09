def find(nums,target):
    nums.sort()
    x=nums
    def find_n(x):
        if len(x)%2==0:
            n=len(x)//2
        elif len(x)%2!=0:
            n=(len(x)-1)//2
    if nums[find_n(x)] == target:
        return n
    elif nums[find_n(x)]>target:
        x=[]
        for i in range(0,n):
            x.append(nums[i])
        return find(x)

    elif nums[n]<target:
        x=[]
        for i in range(n-1,len(nums)):
            x.append(nums[i])
        return find(x)
    
print(find([9,5,8,2,10,6],8))