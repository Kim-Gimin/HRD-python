fin = open("lyrics.txt", "r")

lyrics = fin.readlines()
#print(lyrics)
fin.close()
lines = []
i = 1


for lines in lyrics:
    if 'strangers' in lyrics:
        lines.append(i)
    i += 1

print("counter : ", lines)
