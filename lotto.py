import random

balls = []
for i in range(1, 45 + 1):
    balls.append(i)

random.shuffle(balls)

lotto = balls[0:7]
print("lotto:", lotto)