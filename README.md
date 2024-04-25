# Genetic Algorithm Solution for Einstein's Challenge

## Introduction
This repository contains an implementation of a **genetic algorithm (GA)**, a **metaheuristic** inspired by the process of **natural selection**. It is part of the larger class of evolutionary algorithms (EA) and is designed to solve optimization and search problems through operations such as **mutation, crossover, and selection**.

## Implementation
The genetic algorithm in this repository has been specifically implemented to solve **Einstein's Challenge**, a logic puzzle that involves deducing the correct arrangement of various items based on a series of clues. The challenge is structured as follows:

## Puzzle 
The puzzle is the following. Let us assume that there are five houses of different colors next to each other on the same road. In each house lives a man of a different nationality. Every man has his favorite drink, his favorite brand of cigarettes, and keeps pets of a particular kind. Next we are given the following 15 statements.

1. The Englishman lives in the red house.
2. The Swede keeps dogs.
3. The Dane drinks tea.
4. The green house is just to the left of the white one.
5. The owner of the green house drinks coffee.
6. The Pall Mall smoker keeps birds.
7. The owner of the yellow house smokes Dunhills.
8. The man in the center house drinks milk.
9. The Norwegian lives in the first house.
10. The Blend smoker has a neighbor who keeps cats.
11. The man who smokes Blue Masters drinks bier.
12. The man who keeps horses lives next to the Dunhill smoker.
13. The German smokes Prince.
14. The Norwegian lives next to the blue house.
15. The Blend smoker has a neighbor who drinks water.
The objective is to determine who owns the fish based on the given clues, which include statements like "The Brit lives in the red house," "The Swede keeps dogs as pets," and "The Dane drinks tea."

![TABLET](https://github.com/ByteCodeBros/einstein-challenge/assets/92281096/55f80e00-c1e7-4096-af6e-5170afa028aa)

For Einstein's Challenge there are 5 variables each with 5 possible assignments, generating a total of 5^5 = 3125 possible variations. Then all permutations of size 5 would be 3125^5 ~= 3e17. This is too large of a number to brute force and try all the possibilities.
The genetic algorithm approaches this problem by representing each possible solution as an individual in the population. The fitness function evaluates how closely an individual's arrangement of houses, nationalities, beverages, cigars, and pets matches the clues provided. Through the processes of **selection, crossover, and mutation**, the algorithm iteratively improves the population until it **converges on the correct solution**.

## How the Genetic Algorithm Works
The algorithm follows these steps:

1. **Initialization**: Start with a randomly generated population of candidate solutions for Einstein's Challenge.
2. **Evaluation**: Each candidate is evaluated based on how well it satisfies the conditions of the challenge.
3. **Selection**: Candidates are selected for reproduction based on their fitness scores.
4. **Crossover**: Selected candidates undergo crossover to produce offspring that combine traits from both parents.
5. **Mutation**: Offspring are mutated to introduce new traits and increase diversity.
6. **Replacement/ Random Immigrant**: New offspring replace some of the older population.
7. **Termination**: The algorithm repeats until a candidate that fully solves Einstein's Challenge is found or a set number of generations have passed.

## Goals
The goal of this genetic algorithm is to efficiently navigate the vast search space of possible solutions to Einstein's Challenge and converge on the correct answer.

## Conclusion
By leveraging the principles of natural evolution, this genetic algorithm provides an innovative approach to solving Einstein's Challenge, demonstrating the versatility and power of evolutionary computation.

