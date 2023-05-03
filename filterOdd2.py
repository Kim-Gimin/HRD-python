def isOdd(num):
    return num % 2 == 1

list = [i for i in range(1, 11)]

print ("list : ", list)

filter(isOdd, list)

print("list : ", list)