#we will re-visit this also
from stats import mode
class Players:
    def __init__(self,filename=None):
        self.players = {}
        self.filename = filename
        try:
            fobj = open(filename,"r")
            for line in fobj:
                fields = line.split()
                name = fields[0]
                fields = fields[1:]
                for player in fields:
                    self.addElement(name,player)
        except:
            pass
                                         
    def addElement(self,name,player):
        if name in self.players:
            if player not in self.players[name]:
                self.players[name].append(player)
            else:
                self.players[name] = [player]
    def removePlayer(self,name,player):
        if name in self.players:
            if player in self.players[name]:
                self.players[name].remove(player)

    def show(self):
        for name in self.players:
            print(name,end=" ")
            print(self.players[name])
    def save(self):
        try:
            fobj = open(self.filename,"w")
            for name in self.players:
                fobj.write(name+" ")
                for player in self.players[name]:
                    fobj.write(player+" ")
                fobj.write("\n")
        except:
            pass
    def mostPopularPlayer0(self):
        populars = {}
        for players in self.players.values():
            for player in players:
                if player in populars:
                    populars[player] = populars[player] + 1
                else:
                    populars[player] = 1
        finals = []
        for player,rank in populars.items():
            finals.append((rank,player))
        finals.sort()
        return finals[-1][-1]

    def mostPopularPlayer1(self):
        allplayers = []
        for players in self.players.values():
            allplayers.extend(players)
        return mode(allplayers)
    
    def __eq__(self, obj):
        return self.players == obj.players
    def __add__(self, obj):
        tmp = Players()
        for name in self.players:
            for player in self.players[name]:
                tmp.addElement(name, player)
        for name in obj.players:
            for player in obj.players[name]:
               tmp.addElement(name,player)
        return tmp
    def __getitem__(self, index):
        return(self.players[index])
    def __setitem__(self.name, player):
        self.addElement(name, player)
        
p1 = Players("C:/Users/rkovalch/Documents/players.txt")
p1.addElement("amar", "steve")
p1.addElement("grnu", "steve")
p1.addElement("joe", "steve")


p2.addElement("guru", "mark")
p2= Players("player2.txt")
p2.addElement("amar", "steve")
p2.addElement("guru", "mark")


print(p1['amar'])

p1.show()
p2.show()
#p3 = p1 +p2
