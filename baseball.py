import random
list = [1,2,3,4,5,6,7,8,9]

question = random.sample(list, 3)

strike = 0
ball = 0
count = 0

while strike != 3:
    str = input("a b c : ")
    answer = list(map(int, str.split()))

    for i in range(0, 3):
        for j in range(0, 3):
            if question[i] == answer[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    count += 1

print("Congratuation")