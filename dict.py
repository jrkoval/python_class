players = {'rose':100, 'joe':50}
players['nick'] = 500
print(players)
players['rose'] = 150
print(players)
for name, rank in players.items():
    print(name, end=" ")
    print(rank)
