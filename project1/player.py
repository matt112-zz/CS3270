from sets import Set

class Player:
    def __init__(self, name):
        self.name = name
        self.army = 0
        self.terr = []
        self.numOfTerr = 0
        
        self.NorthAmerica = Set()
        self.SouthAmerica = Set()
        self.Europe = Set()
        self.Africa = Set()
        self.Asia = Set()
        self.Australia = Set()
        
    def addArmy(self, num):
        self.army += num
    def addTerr(self, j):
        self.terr.append(j)
        self.numOfTerr+=1
    def getArmy(self):
        return self.army
    def getTerr(self):
        return self.terr
    def getName(self):
        return self.name
    def addToSet(self, territory, continent):
        if(continent == "North America"):
            self.NorthAmerica.add(territory)
        elif(continent == "South America"):
            self.SouthAmerica.add(territory)
        elif(continent == "Europe"):
            self.Europe.add(territory)
        elif(continent == "Africa"):
            self.Africa.add(territory)
        elif(continent == "Asia"):
            self.Asia.add(territory)
        elif(continent == "Australia"):
            self.Australia.add(territory)
    def checkSets(self):
        if(len(self.NorthAmerica) == 9):
            print "Owns all territories in North America"
        if(len(self.SouthAmerica) == 4):
            print "Owns all territories in South America"
        if(len(self.Europe) == 7):
            print "Owns all territories in Europe"
        if(len(self.Africa) == 6):
            print "Owns all territories in Africa"
        if(len(self.Asia) == 12):
            print "Owns all territories in Asia"
        if(len(self.Australia) == 4):
            print "Owns all territories in Australia"