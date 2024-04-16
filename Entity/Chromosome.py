class Chromosome:

    YELLOW = "000"; GERMAN = "000"; WATER = "000"; BLENDS = "000"; DOGS = "000"
    BLUE = "001"; DANISH = "001"; COFFEE = "001"; BLUEMASTER = "001"; HORSES = "001"
    WHITE = "010"; BRITISH = "010"; BEER = "010"; DUNHILL = "010"; CATS = "010"
    GREEN = "011"; NORWEGIAN = "011"; TEA = "011"; PALLMALL = "011"; BIRDS = "011"
    RED = "100"; SWEDISH = "100"; MILK = "100"; PRINCE = "100"; FISHES = "100"

    HOUSE1 = 0; HOUSE2 = 15; HOUSE3 = 30; HOUSE4 = 45; HOUSE5 = 60
    COLOR = 0; NATIONALITY = 3; DRINK = 6; CIGARETTE = 9; ANIMAL = 12
    SIZE = 3; EASY = 1; MEDIUM = 1; HARD = 1; RIGHT = 1; LEFT = -1

    colors = ["YELLOW", "BLUE", "WHITE", "GREEN", "RED"]
    nationality = ["GERMAN", "DANISH", "BRITISH", "NORWEGIAN", "SWEDISH"]
    drink = ["WATER", "COFFEE", "BEER", "TEA", "MILK"]
    cigarette = ["BLENDS", "BLUEMASTER", "DUNHILL", "PALLMALL", "PRINCE"]
    animal = ["DOGS", "HORSES", "CATS", "BIRDS", "FISHES"]

    def __init__(self, binaryChromosome):
        self.binaryChromosome = binaryChromosome
        self.score = 0
        self.score = self.fitness()

    def fitness(self):
        self.score = 0
        self.easy()
        self.medium()
        self.hard()
        return self.score

    def easy(self):
        i = 0

        # Rule 1
        if self.verifyHouse(0, self.NATIONALITY, self.NORWEGIAN):
            i += 1

        # Rule 9
        if self.verifyHouse(2, self.DRINK, self.MILK):
            i += 1

        self.score += i * self.EASY

    def medium(self):
        i = 0

        # Rule 2
        nHouse = self.houseNumber(self.NATIONALITY, self.BRITISH)
        if self.verifyHouse(nHouse, self.COLOR, self.RED):
            i += 1

        # Rule 3
        nHouse = self.houseNumber(self.NATIONALITY, self.SWEDISH)
        if self.verifyHouse(nHouse, self.ANIMAL, self.DOGS):
            i += 1

        # Rule 4
        nHouse = self.houseNumber(self.NATIONALITY, self.DANISH)
        if self.verifyHouse(nHouse, self.DRINK, self.TEA):
            i += 1

        # Rule 5
        nHouse = self.houseNumber(self.COLOR, self.GREEN)
        if self.verifyHouse(nHouse+self.RIGHT, self.COLOR, self.WHITE):
            i += 1

        # Rule 6
        nHouse = self.houseNumber(self.COLOR, self.GREEN)
        if self.verifyHouse(nHouse, self.DRINK, self.COFFEE):
            i += 1

        # Rule 7
        nHouse = self.houseNumber(self.CIGARETTE, self.PALLMALL)
        if self.verifyHouse(nHouse, self.ANIMAL, self.BIRDS):
            i += 1

        # Rule 9
        nHouse = self.houseNumber(self.COLOR, self.YELLOW)
        if self.verifyHouse(nHouse, self.CIGARETTE, self.DUNHILL):
            i += 1

        # Rule 12
        nHouse = self.houseNumber(self.CIGARETTE, self.BLUEMASTER)
        if self.verifyHouse(nHouse, self.DRINK, self.BEER):
            i += 1

        # Rule 13
        nHouse = self.houseNumber(self.NATIONALITY, self.GERMAN)
        if self.verifyHouse(nHouse, self.CIGARETTE, self.PRINCE):
            i += 1

        self.score += i * self.MEDIUM

    def hard(self):
        i = 0
        # Rule 10
        nHouse = self.houseNumber(self.CIGARETTE, self.BLENDS)
        if self.verifyHouse(nHouse + self.RIGHT, self.ANIMAL, self.CATS) or self.verifyHouse(nHouse+self.LEFT, self.ANIMAL, self.CATS):
            i += 1

        # Rule 11
        nHouse = self.houseNumber(self.ANIMAL, self.HORSES)
        if self.verifyHouse(nHouse + self.RIGHT, self.CIGARETTE, self.DUNHILL) or self.verifyHouse(nHouse + self.LEFT, self.CIGARETTE, self.DUNHILL):
            i += 1

        # Rule 14
        nHouse = self.houseNumber(self.NATIONALITY, self.NORWEGIAN)
        if self.verifyHouse(nHouse + self.RIGHT, self.COLOR, self.BLUE) or self.verifyHouse(nHouse + self.LEFT, self.COLOR, self.BLUE):
            i += 1

        # Rule 15
        nHouse = self.houseNumber(self.CIGARETTE, self.BLENDS)
        if self.verifyHouse(nHouse + self.RIGHT, self.DRINK, self.WATER) or self.verifyHouse(nHouse + self.LEFT, self.DRINK, self.WATER):
            i += 1

        self.score += i * self.HARD

    def houseNumber(self, dataType, desiredData):
        for i in range(0, 61, 15):
            if self.binaryChromosome[i + dataType: i + dataType + self.SIZE] == desiredData:
                return int(i/15)
        return 5

    def verifyHouse(self, houseNumber, dataType, desiredData):
        if houseNumber > 4 or houseNumber < 0:
            return False
        return self.binaryChromosome[houseNumber * 15 + dataType: houseNumber * 15 + dataType + self.SIZE] == desiredData

    def getBinaryChromosome(self):
        return self.binaryChromosome

    def getScore(self):
        return self.score

    def __str__(self):
        res = ""  # "\nScore: " + str(self.getScore()) + ", "
        for i in range(self.HOUSE1, self.HOUSE5+1, 15):
            res += "\nHouse " + str(int(i/15) + 1) + ": \t"

            index = int(self.binaryChromosome[i+self.COLOR:i+self.COLOR+self.SIZE], 2)
            res += self.colors[index] + "(" + format(index, '03b') + "), "

            index = int(self.binaryChromosome[i + self.NATIONALITY:i + self.NATIONALITY + self.SIZE], 2)
            res += self.nationality[index] + "(" + format(index, '03b') + "), "

            index = int(self.binaryChromosome[i + self.DRINK:i + self.DRINK + self.SIZE], 2)
            res += self.drink[index] + "(" + format(index, '03b') + "), "

            index = int(self.binaryChromosome[i + self.CIGARETTE:i + self.CIGARETTE + self.SIZE], 2)
            res += self.cigarette[index] + "(" + format(index, '03b') + "), "

            index = int(self.binaryChromosome[i + self.ANIMAL:i + self.ANIMAL + self.SIZE], 2)
            res += self.animal[index] + "(" + format(index, '03b') + "), "

        return str(res)
