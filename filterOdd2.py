def isOdd(num):
    return num % 2 == 1

nums = [i for i in range(1, 11)]

print ("nums : ", nums)

result = list(filter(isOdd, nums))
print("result:", result)

result = list(filter(lambda num : num % 2 == 1, nums))
print("result: ",result)

result = [num for num in range(1, 10+1) if num % 2 == 1]
print("result : ", result)