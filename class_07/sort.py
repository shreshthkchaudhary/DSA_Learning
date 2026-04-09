def sort(nums):
    for i in range(len(nums)-1):
        for j in range (i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                # sort(nums)
    return nums

print(sort([3,5,2,1,7,8,9,3,2,1]))