fobj = open("C:/Users/rkovalch/Documents/players.txt","r")
players = {}
for line in fobj:
    fields = line.split()
    name = fields[0]
    score = int(fields[1])

    if name in players:
        players[name] = players[name] + score
    else:
        players[name] = score

for name, score in players.items():
    print(name, end=" ")
    print(score)
