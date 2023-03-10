class Pokemon:
    def __init__(self, nom, vie=0, defense=0, attaque=0):
        self.__nom = nom
        self.__vie = vie
        self.__defense = defense
        self.__attaque = attaque

    def afficherInfos(self):
        print(f"Nom: {self.__nom}")
        print(f"Vie: {self.__vie}")
        print(f"Défense: {self.__defense}")
        print(f"Attaque: {self.__attaque}")

    def enleverVie(self, points_de_vie):
        self.__vie -= points_de_vie

    def getNom(self):
        return self.__nom

    def getVie(self):
        return self.__vie

    def getDefense(self):
        return self.__defense

    def getAttaque(self):
        return self.__attaque
