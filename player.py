from stats import mode

class Players:
    def __init__(self):
        self.players = {}
        try:
            fobj = open('player.txt','r')
            for line in fobj:
                fields = line.split()
                name = fields[0]
                fields = fields[1:]
                for player in fields:
                    self.addElement(name, player)
        except:
              pass
    def addElement(self, name, player):
        #if (self.players[name]):
        if name in self.players:
          if player not in self.players[name]:
            self.players[name].append(player)
        else:
            self.players[name] = [player]

    def rmElement(self, name, player):
        #if (self.players[name]):
        if name in self.players:
          if player in self.players[name]:
            self.players[name].remove(player)
        
    def show(self):
        for name in self.players:
            print(name, end=" ")
            print(self.players[name])
    def save(self):
        fobj = open('player.txt','w')
        for name in self.players:
            fobj.write(name)
            for player in self.players[name]:
                fobj.write(" ")
                fobj.write(player)
    def pops(self):
        populars = {}
        for players in self.players.values():
            for player in players:
                if player in populars:
                    populars[player] = populars[player] + 1
                else:
                    populars[player] = 1
        finals = []
        for player,rank in populars.items():
            finals.append((rank, player))
            print("appending" +str(rank) +" " +str(player))
            print(type(finals))
            print("list = " + str(finals))
        finals.sort()
        return finals[-1][-1]
    def mostPopularPlayer1(self):
        allplayers = []
        for players in self.players.values():
            allplayers.extend(players)
        return mode(allplayers)
    

        

p1 = Players()    
p1.addElement("amar", "steve")
p1.addElement("amar", "mark")
p1.addElement("amar", "chris")
p1.addElement("dhoni", "chris")
p1.addElement("dhoni", "steve")
p1.addElement("Jane", "steve")
p1.addElement("Jane", "chris")

print(p1.pops())
#print(p1.mostPopularPlayer1())
