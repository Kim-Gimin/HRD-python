
nums = [1,2,3,4]
nums2 = [5,6,7,8]
nums3 = [9,10,11,12]

matrix = [nums, nums2, nums3]
print(matrix)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(matrix)

total = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        total = total + matrix[i][j]

print("total:", total)

total = 0
for i in range(0, len(matrix)):
    total = total + sum(matrix[i])

print("total :", total)