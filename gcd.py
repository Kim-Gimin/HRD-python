def gcd(a, b):
    remain = a % b
    while remain != 0:
        a = b
        b = remain
        reamin = a % b
    return b
a, b = map(int, input("input a b :").split())
result = gcd(a, b)

print("gcd", gcd)