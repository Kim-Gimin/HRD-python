import random

def deleteFail(scores):
    for data in scores:
        if data < 60:
            scores.remove(data)

scores = []
for _ in range(1, 10 + 1):
    scores.append(random.randint(50, 100))

deleteFail(scores)

print("nums :", scores)