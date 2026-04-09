# n=int(input())

# matrix=[]
# for i in range(n):
#     temp = list(map(int,input().split()))
#     matrix.append(temp)

# m= len(matrix[0])

# sum=0

# for j in range(n):
#     for j in range (m):
        # sum = sum+matrix[i][j]

matrix=[[1,2,3,4],
      [5,6,7,8],
      [9,10,11,12],
      [13,14,15,16],
      [17,18,19,20]]

n=5
m=4
print("rows sum")
for i in range(n):
    sum=0
    for j in range(m):
        sum = sum+matrix[i][j]
    print (sum)
print("columns sum")
for j in range(m):
    col_sum = 0
    for i in range(n):
        col_sum += matrix[i][j]
    print(col_sum)
