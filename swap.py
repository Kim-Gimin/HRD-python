def swap(a, b): #안바뀜(지역변수라 swap함수 끝날시 모두 없어짐)
    tmp = a
    a = b
    b = tmp
def swap2():#전역변수라 바뀜
    global a, b
    
    tmp = a
    a = b
    b = tmp

a = 100
b = 200
print("a : ", a, "b : ", b)

swap(a, b)
print("a : ", a, "b : ", b)

swap2()
print("a : ", a, "b : ", b)
