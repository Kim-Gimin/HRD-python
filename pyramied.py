for i in range (1, 5):
    line = ' '
    for j in range(1, 6-i):
        line += ' '
    for k in range(1, 2*i):
        line += '*'
    print(line)