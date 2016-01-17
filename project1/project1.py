from collections import defaultdict
from operator import attrgetter
from player import Player

numOfTerritories = 0;

territories = {}
for line in open("territories.txt"):
    line = line.strip()
    tokens = line.split(",")
    territory = tokens[0]
    ID = tokens[1]
    continent = tokens[2]
    data = (territory, continent)
    territories[ID] = data

gamestate = defaultdict(list)   #gamestate is a dictionary list
for line in open("gameState.txt"):
    line = line.strip()
    tokens = line.split(",")
    ID = tokens[0]
    numOfTerritories += 1
    user = int(tokens[1])
    armies = tokens[2]
    data = (ID, armies)
    gamestate[user].append(data)    #is user is already in the dictionary it will append it to that list. If not, create a new entry


players = []

for j in range(1, len(gamestate)+1): #total number of users/dictionary entrys
    p = Player(j)
    for i in range(0, len(gamestate[j])): #length of the list in that dictionary entry
        p.addArmy(int(gamestate[j][i][1])) #gives number of armies to addArmy() 
        p.addTerr(territories[ gamestate[j][i][0] ][0]) #gives name of territory to addTerr()
        p.addToSet(territories[ gamestate[j][i][0] ][0], territories[ gamestate[j][i][0] ][1])
    players.append(p)
  
  
print "Total number of territories:", numOfTerritories, "\n"

for k in range(0, len(players)):
    print "Player", players[k].getName()
    print "Has", players[k].getArmy(), "armies"
    print "Owns", len(players[k].getTerr()), "territories"
    print "Names of territories:",
    s = ", "
    seq = players[k].getTerr()
    print s.join(seq)
    players[k].checkSets()
    print "\n"
    
mostArmies = max(players, key=attrgetter("army"))
mostTerritories = max(players, key=attrgetter("numOfTerr"))
print "Player", mostArmies.name, "has the most armies:", mostArmies.army
print "Player", mostTerritories.name, "owns the most territories:", mostTerritories.numOfTerr