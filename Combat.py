import random
from Feu import Feu
from Eau import Eau
from Normal import Normal
from Terre import Terre


class Combat:
    def __init__(self, pkm1, pkm2):
        self.__pkm1 = pkm1
        self.__pkm2 = pkm2
        self.tour = 0

    # Vérifie si le Pokémon est en vie
    def verifieHP(self):
        if self.__pkm1.getVie() <= 0 or self.__pkm1.getVie == 0:
            return self.__pkm2.getNom() and self.__pkm1.getNom()
        elif self.__pkm2.getVie() <= 0 or self.__pkm2.getVie == 0:
            return self.__pkm1.getNom() and self.__pkm2.getNom()
        else:
            return None

    # Affiche le nom du vainqueur
    def afficherNomWIN(self):
        if self.__pkm1.getVie() > 0 >= self.__pkm2.getVie():
            print(self.__pkm1.getNom(), "a gagné !")
        elif self.__pkm2.getVie() > 0 >= self.__pkm1.getVie():
            print(self.__pkm2.getNom(), "a gagné !")
        else:
            pass

    # Attaque du premier Pokémon
    def attaque(self):
        if random.randint(0, 1) == 1:
            self.degat()
        else:
            print(self.__pkm1.getNom(), "rate son attaque !")
            pass

    # Attaque du second Pokémon
    def attaque2(self):
        if random.randint(0, 1) == 1:
            self.degat2()
        else:
            print(self.__pkm2.getNom(), "rate son attaque !")
            self.attaqueRater()

    def attaqueRater(self):
        self.verifieHP()

    def typepkm1(self):
        if isinstance(self.__pkm1, Eau):
            if isinstance(self.__pkm2, Feu):
                return 2
            elif isinstance(self.__pkm2, Terre):
                return 0.5
            elif isinstance(self.__pkm2, Eau):
                return 1
            elif isinstance(self.__pkm2, Normal):
                return 1
        if isinstance(self.__pkm1, Feu):
            if isinstance(self.__pkm2, Feu):
                return 1
            elif isinstance(self.__pkm2, Terre):
                return 2
            elif isinstance(self.__pkm2, Eau):
                return 0.5
            elif isinstance(self.__pkm2, Normal):
                return 1
        if isinstance(self.__pkm1, Terre):
            if isinstance(self.__pkm2, Feu):
                return 0.5
            elif isinstance(self.__pkm2, Terre):
                return 1
            elif isinstance(self.__pkm2, Eau):
                return 2
            elif isinstance(self.__pkm2, Normal):
                return 1
        if isinstance(self.__pkm1, Normal):
            if isinstance(self.__pkm2, Feu):
                return 0.75
            elif isinstance(self.__pkm2, Terre):
                return 0.75
            elif isinstance(self.__pkm2, Eau):
                return 0.75
            elif isinstance(self.__pkm2, Normal):
                return 1

    def typepkm2(self):
        if isinstance(self.__pkm2, Eau):
            if isinstance(self.__pkm1, Feu):
                return 2
            elif isinstance(self.__pkm1, Terre):
                return 0.5
            elif isinstance(self.__pkm1, Eau):
                return 1
            elif isinstance(self.__pkm1, Normal):
                return 1
        if isinstance(self.__pkm2, Feu):
            if isinstance(self.__pkm1, Feu):
                return 1
            elif isinstance(self.__pkm1, Terre):
                return 2
            elif isinstance(self.__pkm1, Eau):
                return 0.5
            elif isinstance(self.__pkm1, Normal):
                return 1
        if isinstance(self.__pkm2, Terre):
            if isinstance(self.__pkm1, Feu):
                return 0.5
            elif isinstance(self.__pkm1, Terre):
                return 1
            elif isinstance(self.__pkm1, Eau):
                return 2
            elif isinstance(self.__pkm1, Normal):
                return 1
        if isinstance(self.__pkm2, Normal):
            if isinstance(self.__pkm1, Feu):
                return 0.75
            elif isinstance(self.__pkm1, Terre):
                return 0.75
            elif isinstance(self.__pkm1, Eau):
                return 0.75
            elif isinstance(self.__pkm1, Normal):
                return 1

    # Calcule des dégâts
    def degat(self):
        print("----------", "Tour", self.tour, "----------")
        pkm1_degats = (self.__pkm1.getAttaque() * self.typepkm1()) - self.__pkm2.getDefense()
        print(self.__pkm1.getNom(), "inflige", pkm1_degats, "dégâts à", self.__pkm2.getNom())
        self.__pkm2.enleverVie(pkm1_degats)
        print(self.__pkm2.getNom(), "a désormais", self.__pkm2.getVie(), "HP")
        self.verifieHP()
        self.afficherNomLOSE()
        self.afficherNomWIN()

    def degat2(self):
        pkm2_degats = (self.__pkm2.getAttaque() * self.typepkm2()) - self.__pkm1.getDefense()
        print(self.__pkm2.getNom(), "inflige", pkm2_degats, "dégâts à", self.__pkm1.getNom())
        self.__pkm1.enleverVie(pkm2_degats)
        print(self.__pkm1.getNom(), "a désormais", self.__pkm1.getVie(), "HP")
        self.verifieHP()
        self.afficherNomLOSE()
        self.afficherNomWIN()

    # Affiche le nom du perdant
    def afficherNomLOSE(self):
        if self.__pkm1.getVie() <= 0 < self.__pkm2.getVie():
            print(self.__pkm1.getNom(), "a perdu !")
        elif self.__pkm2.getVie() <= 0 < self.__pkm1.getVie():
            print(self.__pkm2.getNom(), "a perdu !")
        else:
            pass
    # Déroulement du combat
    def debuterCombat(self):
        while self.verifieHP() is None:
            self.tour += 1
            # Mon tour
            self.attaque()
            # Tour adversaire
            self.attaque2()
