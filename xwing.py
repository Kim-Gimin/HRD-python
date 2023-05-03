for i in range(1, 5+1):
    line = ' '
    for j in range(1, 5+1):
        if i == j or i + j == 6:
            line += '*'
        else :
            line += ' '
    print(line)