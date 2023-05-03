fin = open('lyrics.txt', 'r')
lines = fin.readlines()
fin.close()

wordCount = {}
for line in lines:
    words = line.strip().split()
    for word in words:
        if word not in wordCount.keys():
            wordCount[word] = 1
        else:
            wordCount[word] += 1

for word, count in wordCount.items():
    print(word, ':', count)