import json
#"""
"""
with open("words.json", "w") as f:
    words = json.loads(f.read())
"""

with open("con.csv", "r") as f:
    data = f.read()
data = [n.split(",") for n in data.split("\n")]
#labels = [n for i, n in enumerate(data[0]) if (i + 1) % 2]
#print(labels)
counts = {}
for row in data[2:]:
    for i in range(0, len(row), 2):
        if row[i] != "":
            
            #letter = row[i][0].lower()
            for letter in row[i].lower():
                if counts.get(letter) is not None:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
                #if not row[i] in words:
                    #words[row[i]] = [row[i + 1], 0, 0]

for letter in "abcdefghijklmnopqrstuvwxyzáéíóú":#
    if counts.get(letter) is None:
        counts[letter] = 0
    print(letter, "█" * counts[letter] + " " + str(counts[letter]))


with open("con.csv", "r") as f:
    data = f.read()

data = [n.split(",") for n in data.split("\n")]

words = {}
for row in data[2:]:
    for i in range(0, len(row), 2):
        if row[i] != "":
            if not row[i] in words:
                words[row[i]] = row[i + 1]

print(words)
"""
with open("words.json", "w") as f:
    f.write(json.dumps(words))
"""
"""
with open("words.json", "r") as f:
    data = json.loads(f.read())

keys = list(data.keys())
import random
while True:
    try:
        word = keys[random.randint(0, len(keys) - 1)]
        if data[word][1] > 8:
            continue
        if random.randint(0, 1) == 0:
            res = input(word + ": ")
            res = res.strip(" \n")
            if res.lower() == data[word][0].lower():
                print("Yes")
                data[word][1] += 1
            else:
                print("No it was " + data[word][0])
                data[word][2] += 1
        else:
            res = input(data[word][0] + ": ")
            res = res.strip(" \n")
            if res.lower() == word.lower():
                print("Yes")
                data[word][1] += 1
            else:
                print("No it was " + word)
                data[word][2] += 1
    except EOFError:
        break

with open("words.json", "w") as f:
    f.write(json.dumps(data))
"""
