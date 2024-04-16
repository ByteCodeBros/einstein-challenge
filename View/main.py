from Control.Manager import Manager

if __name__ == '__main__':
    print("Bem-Vindo(a) ao Algoritmo Genético")
    # popSize = int(input("Informe o tamanho da população: "))
    # nGeneration = int(input("Informe a quantidade de gerações: "))
    popSize = 25000
    nGeneration = 100

    manager = Manager(popSize, nGeneration)
    manager.ga(8, 5, 1)
    
