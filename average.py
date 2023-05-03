str = input("kor eng mat :")
list = str.split()

kor, eng, mat = list
sum = int(kor) + int(eng) + int(mat)

kor, eng, mat = map(int, list)
average = sum / 3

print(f"sum : {sum} ----- average : {average:.2f}")