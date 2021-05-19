with open("inputs/7.txt", 'r') as file:
    lines = file.read().split("\n")

scoredict = dict()

for line in lines:
    folder, items = line.split(' bags contain ')
    if 'no other bags' in items:
        scoredict[folder] = 1

for run in range(15):
    for line in lines:
        folder, items = line.split(' bags contain ')
        items_splitted = items.split(', ')
        q = []
        colors = []
        for item in items_splitted:
            item = item.replace(' bags', '').replace(' bag', '').replace('.', '')
            q.append(item[:1])
            colors.append(item[2:])

        if all(elem in scoredict for elem in colors):
            scoredict[folder] = 1
            for i in range(len(colors)):
                scoredict[folder] += int(q[i]) * scoredict[colors[i]]

print(scoredict['shiny gold'] - 1)
