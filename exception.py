a, b = map(int, input("input a b : ").split())

try:
    result = a / b

    if b == 0:
        raise ZeroDivisionError()
    
    print(f"{a} / {b} = {result}")
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero!")

