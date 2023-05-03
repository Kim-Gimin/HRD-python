fin = open('lyrics.txt', 'r')
lines = fin.readlines()
fin.close()

wordCount = {}
for index, line in enumerate(lines):
    words = line.strip().split()
    for word in words:
        word = word.strip('"(),!').lower()
        if word not in wordCount.keys():
            wordCount[word] = [index]
        else:
            wordCount[word].append(index)

for word, lines in wordCount.items():
    print(word, ":", lines)
