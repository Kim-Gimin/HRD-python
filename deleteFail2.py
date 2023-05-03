import random

def isPass(score):
    return score >= 60

scores = [random.randint(50, 100) for _ in range(1, 10 + 1)]

result = list(filter(isPass, scores))

print("result :", result)