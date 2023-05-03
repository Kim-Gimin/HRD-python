def isOdd(num):
    return num % 2 == 1

nums = [i for i in range(1, 11)]

print ("nums : ", nums)

result = list(filter(isOdd, nums))

print("list : ", nums)