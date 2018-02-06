import random

NUMMERS = ["9","10","J","D","K","A"]
WAARDEN = [9,10,11,12,13,14]
PUNTEN = [0,0,1,2,3,4]
SOORTEN = ["Schuppen", "Klaveren", "Harten", "Koeken"]
SPELERS = []
TROEF = None

#info spelers
Spelers=["speler1","speler2","speler3","speler4"]


class Kaart:
    def __init__(self,nr,soort):
        self.nr = nr
        self.soort = soort
    def show(self):
        print(str(self.nr) + " " + self.soort)
    def getSoort(self):
        return self.soort
    def getNr(self):
        return self.nr
    def getWaarde(self):
        waarde = NUMMERS.index(self.nr)
        return WAARDEN[waarde]
    def getPunten(self):
        punt = NUMMERS.index(self.nr)
        return PUNTEN[punt]
    def getKaart(self):
        samenstelling = self.nr + " " + self.soort
        return samenstelling

class Speler:
    def __init__(self,naam,score, spelerKaarten):
        self.spelerKaarten = spelerKaarten
        self.naam = naam
        self.score = score
        self.laatsteKaart = None

    def kaartToevoegen(self, kaart):
        self.spelerKaarten.append(kaart)

    def printKaart(self, index):
        kaart = self.spelerKaarten[index].getKaart()
        print(kaart)

    def getKaart(self, index):
        kaart = self.spelerKaarten[index]
        return kaart
        
    def toonKaarten(self):
        for e in self.spelerKaarten:
            print(str(self.spelerKaarten.index(e)) + " : " +e.getKaart())

    def getNaam(self):
        return self.naam
    def getScore(self):
        return self.score
    def removeKaart(self,Kaart):
        self.spelerKaarten.remove(Kaart)

    def setLaatsteKaart(self, Kaart, troef):
        
        self.laatsteKaart = Kaart
        self.troef = troef
    def setScore(self,score):
        self.score = score
    def getLaatsteKaart(self):
        return self.laatsteKaart
    def printLaatsteKaart(self):
        print(self.laatsteKaart.getKaart())

    def getLaatsteIsTroef(self):
        return self.troef

class Deck:
    def __init__(self):
        self.kaarten = []
        self.bouw()

    def bouw(self):
        for s in range(0,4):
            for n in range(0, 6):
                self.kaarten.append(Kaart(NUMMERS[n],SOORTEN[s]))

    def uithalen(self, index):
        self.kaarten.remove(self.kaarten[index])
        
    def show(self):
        for c in self.kaarten:
            c.show()

    def schudden(self):
        random.shuffle(self.kaarten)

    def delen(self):
        aantalSpelers = len(SPELERS)
        aantalKaarten = len(self.kaarten)
        print()
        global TROEF
        TROEF = dek.kaarten[23]
        print("TROEF = " + TROEF.getKaart())
        print()
        for s in range(0,3):
            for k in range (0,len(Spelers)):
                SPELERS[k].kaartToevoegen(dek.kaarten[0])
                dek.uithalen(0)
                SPELERS[k].kaartToevoegen(dek.kaarten[0])
                dek.uithalen(0)

class Tafel:
    def __init__(self):
        self.hoop = []
        self.lijst = []
    def toevoegen(self,Kaart, troef, Speler):
        self.lijst = [Kaart, troef, Speler]
        self.hoop.append(self.lijst)
    def printTafel(self):
        print("TAFEL: ")
        for i in range(0,len(self.hoop)):
            alsTroef = ""
            if self.hoop[i][1] == True:
                alsTroef = "TROEF"
            else:
                alsTroef = ""
                
            print(self.hoop[i][2].getNaam() + ": " + self.hoop[i][0].getKaart() + " " + alsTroef )
    def getHoop(self):
        return self.hoop
class Boompje:
    def __init__(self):
        self.team1 = []
        self.team2 = []
        self.team1Takken = 7
        self.team2Takken = 7
        self.team1geschrapt = 5
        self.team2geschrapt = 5
        
        for i in range(0,len(SPELERS)):
            if i % 2 == 0:
                self.team1.append(SPELERS[i])
            else:
                self.team2.append(SPELERS[i])

    def schrap(self,index):
        if index == 1:
            self.team1geschrapt = self.team1geschrapt + 1 
        if index == 2:
            self.team2geschrapt = self.team2geschrapt + 1

    def takkenBijtekenen(self,index):
        if index == 1:
            self.team1Takken = self.team1Takken + 1 
        if index == 2:
            self.team2Takken = self.team2Takken + 1

    def getTeam(self,index):
        if index == 1:
            return self.team1
        if index == 2:
            return self.team2

    def getTakken(self,index):
        if index == 1:
            return self.team1Takken
        if index == 2:
            return self.team2Takken
    def getGeschrapt(self,index):
        if index == 1:
            return self.team1geschrapt
        if index == 2:
            return self.team2geschrapt
        
    def printTeamNamen(self,index):
        if index == 1:
            for i in self.team1:
                print(i.getNaam())
        if index == 2:
            for i in self.team2:
                print(i.getNaam())

    def tekenBoompje(self):
        print("team1    -------    team2")
        t1g = []
        t2g = []
        for i in range(0,self.team1geschrapt):
            t1g.append("************")
        for i in range(0,self.team2geschrapt):
            t2g.append("************")
            
        lengte = len(t1g)
        if len(t2g)>len(t1g):
            lengte = len.t2g
            
        for i in range(0,lengte):
            print("{}{}{}".format(t1g[i],"|", t2g[i]))
class Ronde:
    def __init__(self):
        #kaarten weergeven
        for i in range(0,len(SPELERS)):
            print(SPELERS[i].getNaam())
            SPELERS[i].toonKaarten()
            print()
            
        print("Geef nummer van kaart in, bv. 4")

        #Nieuwe tafel aanmaken
        nieuweTafel = Tafel()

        #input vragen "kaart"
        for i in range(0,len(SPELERS)):
            try:
                kaart = int(input(SPELERS[i].getNaam()+": "))
                
            except ValueError:
                print("Geef een nummer in, laatste kans!")
                try:
                    kaart = int(input(SPELERS[i].getNaam()+": "))

                except ValueError:
                    print("automatisch 0...")
                    kaart = 0
            SPELERS[i].printKaart(kaart)
            
            troef = None
            
            if(SPELERS[i].getKaart(kaart).getSoort() == TROEF.getSoort()):
                troef = True
            else:
                troef = False
                
            nieuweTafel.toevoegen(SPELERS[i].getKaart(kaart),troef,SPELERS[i])
            
            SPELERS[i].setLaatsteKaart(SPELERS[i].getKaart(kaart),troef)
            SPELERS[i].removeKaart(SPELERS[i].getKaart(kaart))
            nieuweTafel.printTafel()

        print()
        #kijken wie wint
        hoop = nieuweTafel.getHoop()
        eersteSoort = hoop[0][0].getSoort()
        gevolgd = []
        troeven = []

        for i in range(0,len(hoop)):
            if hoop[i][0].getSoort() == eersteSoort:
                gevolgd.append(hoop[i])
            if hoop[i][0].getSoort() == TROEF.getSoort():
                troeven.append(hoop[i])
                
        hoogsteKaart = None
        if len(troeven)<=0:
            hoogsteKaart = gevolgd[0][0]
            for i in range(0,len(gevolgd)):
                if hoogsteKaart.getWaarde() < gevolgd[i][0].getWaarde():
                    hoogsteKaart = gevolgd[i][0]

        if len(troeven)>0:
            hoogsteKaart = troeven[0][0]
            for i in range(0,len(troeven)):
                if hoogsteKaart.getWaarde() < troeven[i][0].getWaarde():
                    hoogsteKaart = gevolgd[i][0]
        winnaar = None
        punten = 0
        for i in range(0,len(SPELERS)):
            if SPELERS[i].getLaatsteKaart().getKaart() == hoogsteKaart.getKaart():
                winnaar = SPELERS[i]
                
        for i in range (0,len(hoop)):
            punten = hoop[i][0].getPunten() + punten
        winnaar.setScore(punten)
        print(winnaar.getNaam() + " heeft deze ronde gewonnen met " + str(punten) + " punten")

        print("-----TUSENSTAND------")
        for i in SPELERS:
            print(i.getNaam() + " " + str(i.getScore()))
                    
#Spelers aanmaken
for i in range(0,len(Spelers)):
    SPELERS.append(Speler(Spelers[i],0,[]))
    
boom = Boompje()
boom.printTeamNamen(2)
boom.tekenBoompje()

#dek aanmaken
dek = Deck()
dek.schudden()
dek.delen()

for i in range(0,5):
    nieuweRonde = Ronde()
    
#kaarten weergeven
#for i in range(0,len(SPELERS)):
#    print(SPELERS[i].getNaam())
#    SPELERS[i].toonKaarten()
#    print()
