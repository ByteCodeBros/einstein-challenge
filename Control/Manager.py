import math
import random
import time

from Entity.Chromosome import Chromosome


class Manager:
    MAX = 15  # Mesmo peso
    # MAX = 2 * 1 + 9 * 2 + 4 * 3 # Equilibrado(1/2/3)
    # MAX = 2 * 1 + 9 * 3 + 4 * 5 # Extremo(1/3/5)
    # MAX = 2 * 1 + 9 * 1 + 4 * 2

    def __init__(self, popSize, nGeneration):
        self.popSize = popSize
        self.nGeneration = nGeneration
        self.population = list()

    def ga(self, survivalRate, mutationRate, immigrationRate):
        startTime = time.time()
        self.population = self.startPop(self.popSize)
        self.population.sort(key=lambda c: c.score, reverse=True)
        t = 0
        # print(f'{t+1}ª Geração: ', end="|")
        # for i in range(self.popSize):
        #     print(str(self.population[i].getScore()), end="|")
        # print(self.population[0])

        while t != self.nGeneration:
            t += 1
            print(f'\n{t}ª Geração: ', end="|")
            print(self.population[0].getScore(), end="|")
            if self.population[0].getScore() == self.MAX:
                print(f'\n\nResposta encontrada em ' + "{:.2f}".format(time.time() - startTime) + ' segundos:')
                print(f'\nGenótipo: {self.population[0].getBinaryChromosome()}\n\nFenótipo:')
                print(self.population[0])
                break
            self.population.sort(key=lambda c: c.score, reverse=True)
            # for i in range(self.popSize):
            #     print(str(self.population[i].getScore()), end="|")

            # SURVIVAL
            survivalPop = self.survival(survivalRate)
            # print("\nSURVIVAL:    ", end="|")
            # for i in range(len(survivalPop)):
            #     print(str(survivalPop[i].getScore()), end="|")

            # CROSSOVER
            crossOverPop = self.crossOver(self.popSize - len(survivalPop))
            # print("\nCROSSOVER:   ", end="|")
            # for i in range(len(crossOverPop)):
            #     print(str(crossOverPop[i].getScore()), end="|")

            # Transição de gerações após crossover
            self.population.clear()
            self.population.extend(survivalPop)
            self.population.extend(crossOverPop)
            self.population.sort(key=lambda c: c.score, reverse=True)

            # MUTATION
            self.mutation(mutationRate)

            # IMMIGRATION
            self.immigration(immigrationRate)

        if self.population[0].getScore() != 15:
            print(f'\n\nNão foi encontrada uma resposta satisfatória para o problema.\nTempo de execução: ' + "{:.2f}".format(time.time() - startTime) + ' segundos')

        # print("\nFINAL:")
        # print(self.population[0])

    def survival(self, survivalRate):
        # sumFitness = 0
        # rouletteWheel = []
        # survivalPop = []
        #
        # for c in self.population:
        #     sumFitness += c.getScore()
        #
        # for c in self.population:
        #     relativeFit = int((c.getScore() ** 2 / sumFitness))
        #     for i in range(0, relativeFit+1):
        #         rouletteWheel.append(c)
        #
        # for i in range(math.ceil(len(self.population) * survivalRate / 100)):
        #     c1 = rouletteWheel[random.randint(0, len(rouletteWheel) - 1)]
        #     survivalPop.append(c1)
        # survivalPop.sort(key=lambda chromosome: chromosome.score, reverse=True)

        # print()
        # for i in range(len(survivalPop)):
        #     print(str(survivalPop[i].getScore()), end="|")

        # return survivalPop

        return self.population[0: math.ceil(len(self.population) * survivalRate / 100)]

    def crossOver(self, newPopSize):
        sumFitness = 0
        rouletteWheel = []
        crossPop = []

        for c in self.population:
            sumFitness += c.getScore()

        for c in self.population:
            relativeFit = int((c.getScore() / sumFitness) ** 1.5)
            for i in range(0, relativeFit+1):
                rouletteWheel.append(c)

        # print(f'\nWheel({len(rouletteWheel)}):  ', end='|')
        # for c in rouletteWheel:
        #     print(f'{c.getScore()}|', end='')

        for i in range(newPopSize):
            c1 = rouletteWheel[random.randint(0, len(rouletteWheel) - 1)]
            c2 = rouletteWheel[random.randint(0, len(rouletteWheel) - 1)]
            c3 = self.cross(c1, c2)
            crossPop.append(Chromosome(c3))
        crossPop.sort(key=lambda chromosome: chromosome.score, reverse=True)
        return crossPop

    def cross(self, c1, c2):
        c1Binary = list(c1.getBinaryChromosome())
        c2Binary = list(c2.getBinaryChromosome())

        for i in range(0, 61, 15):
            c1Binary[i + 6: i + 15] = c2Binary[i + 6: i + 15]
        sonBinary = ''.join(str(i) for i in c1Binary)

        return sonBinary

    def mutation(self, mutationRate):
        for i in range(int(self.popSize/100) * mutationRate):
            popIndex = random.randint(0, self.popSize-1)
            newChromosomeBinary = list(self.population[popIndex].getBinaryChromosome())

            house = [0, 1, 2, 3, 4]
            randomHouse1 = house.pop(random.randint(0, len(house)-1))
            randomHouse2 = house.pop(random.randint(0, len(house)-1))
            randomHouse3 = house.pop(random.randint(0, len(house) - 1))
            randomHouse4 = house.pop(random.randint(0, len(house) - 1))

            allele = random.randint(0, 4)
            house1AlleleBinary = list(newChromosomeBinary[randomHouse1 * 15 + allele * 3: randomHouse1 * 15 + allele * 3 + 3])
            house2AlleleBinary = list(newChromosomeBinary[randomHouse2 * 15 + allele * 3: randomHouse2 * 15 + allele * 3 + 3])

            # Allele of House2 <- Allele of House1, Allele of House1 <- Allele of House2
            newChromosomeBinary[randomHouse2 * 15 + allele * 3: randomHouse2 * 15 + allele * 3 + 3], newChromosomeBinary[randomHouse1 * 15 + allele * 3: randomHouse1 * 15 + allele * 3 + 3] = house1AlleleBinary, house2AlleleBinary

            allele = random.randint(0, 4)
            house3AlleleBinary = list(newChromosomeBinary[randomHouse3 * 15 + allele * 3: randomHouse3 * 15 + allele * 3 + 3])
            house4AlleleBinary = list(newChromosomeBinary[randomHouse4 * 15 + allele * 3: randomHouse4 * 15 + allele * 3 + 3])

            # Allele of House4 <- Allele of House3, Allele of House3 <- Allele of House4
            newChromosomeBinary[randomHouse4 * 15 + allele * 3: randomHouse4 * 15 + allele * 3 + 3], newChromosomeBinary[randomHouse3 * 15 + allele * 3: randomHouse3 * 15 + allele * 3 + 3] = house3AlleleBinary, house4AlleleBinary

            # Construindo binario do cromossomo mutado
            newChromosomeBinaryString = ''.join(str(i) for i in newChromosomeBinary)

            newChromosome = Chromosome(newChromosomeBinaryString)

            # if popIndex == 0:
            #     print("\nMUTAÇÃO-" + str(newChromosome))

            self.population.pop(popIndex)
            self.population.append(newChromosome)

        self.population.sort(key=lambda c: c.score, reverse=True)

    def immigration(self, immigrationRate):
        for i in range(int(self.popSize / 100) * immigrationRate):
            popIndex = random.randint(0, self.popSize - 1)
            self.population.pop(popIndex)
            self.population.append(self.generatesChromossome())
        self.population.sort(key=lambda c: c.score, reverse=True)

    def startPop(self, popSize):
        return [self.generatesChromossome() for i in range(popSize)]

    def generatesChromossome(self):

        binaryChromosome = ""

        allele = list()

        # Uma lista para cada casa
        for i in range(0, 5):
            allele.append(list())

        # Gera as 25 casas
        for i in range(1, 26):
            alleleList = [0, 1, 2, 3, 4]
            randomAllele = alleleList.pop(random.randint(0, len(alleleList) - 1))

            # Tratamento para não haver alelos repetidos em cada casa
            while randomAllele in allele[(i - 1) % 5]:
                randomAllele = alleleList.pop(random.randint(0, len(alleleList) - 1))

            allele[(i - 1) % 5].append(randomAllele)
            binaryChromosome += format(randomAllele, '03b')

        return Chromosome(binaryChromosome)
