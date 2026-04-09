# matrix
nums=[[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16],
      [17,18,19,20]]
# x=len(nums)
# y=len(nums[0])
# print(x,y)
# for i in range (len(nums)):
#     for j in range (len(nums[i])):
#         print(f"{nums[i][j]}({i+1},{j+1})")

a=int(input("Num: "))
for i in range (len(nums)):
    for j in range (len(nums[i])):
        if a==nums[i][j]:
            print(f"{nums[i][j]}({i+1},{j+1})")
