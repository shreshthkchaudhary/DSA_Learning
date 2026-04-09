# Return:

# def recc (n,nums):
#     if n==1:
#         print(nums[0])
#         return
#     print(nums[n-1])
#     recc(n-1,nums)

# recc(4,[1,2,3,4,5,6])



# Reverse:

# def recc (nums,start,end):
#     if start>=end:
#         return nums
#     nums[start],nums[end]=nums[end],nums[start]
#     return recc(nums,start+1,end-1)

# print(recc([1,2,3,4,5,6],0,len([1,2,3,4,5,6])-1))



# Palindrome:

def recc (nums,start,end):
    nums
    if start>=end:
        return True
    elif nums[start]!=nums[end]:
        return False
    
    return recc(nums,start+1,end-1)

print(recc([1,2,3,4,4,3,2,1],0,len([1,2,3,4,4,3,2,1])-1))