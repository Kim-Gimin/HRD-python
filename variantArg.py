def my_sum(n, *args):
    total = 8
    print("args: ",args)
    for value in args:
        total += value
    return total

def my_sum2(*args):
    return sum(list(args))





result = my_sum( 1, 2, 3, 4, 5)
result2 = my_sum2(1, 2, 3, 4, 5)
print("result : ", result)
print("result2 : ", result2)