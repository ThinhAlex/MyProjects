import random

random.seed(10)

NUM_GENERATIONS = 200
NUM_POPULATION = 100
PROBABILITY_MUTATION = 0.2
PROBABILITY_CROSSOVER = 0.8
ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

BANNER = """
**************************************************************
Welcome to GeneticGuess Sentencer! 
This program will attempt to guess a sentence that you input. 
Simply input a sentence and the program will attempt to guess it!
**************************************************************
"""

INPUT = "\nWould you like to continue? (y/n) "

"\nPlease input the sentence you would like the program to guess: "
"\nIncorrect input. Please try again.\n"
"\n\nGeneticGuess results:"
"Generation: "
"I found the sentence early!"
"\nBest Individual: "
"\n\nThank you for using GeneticGuess Sentencer!"


def fitness(target, individual):
    correct = 0
    for i in range(len(target)):
        if individual[i] == target[i]:
            correct +=1
    fit = correct/len(target)
    return fit


def five_tournament_selection(population, target):
    max = -100
    idv_max = ""
    for i in range(5):       
        begin = random.randint(0, NUM_POPULATION-1)*len(target)
        idv = population[begin:begin+len(target)]

        fit = fitness(target, idv)
        if fit > max:
            max = fit
            idv_max = idv
    return idv_max


def make_population(target):
    target_len = len(target)
    population = ""
    for i in range(NUM_POPULATION):
        for j in range(target_len):
            choice = random.choice(ALPHABET)
            population += choice
    
    return population


def mutation(individual):
    new_idv = ""
    for i in range(len(individual)):
        chance = random.random()
        if chance <= PROBABILITY_MUTATION:
            new_idv += random.choice(ALPHABET)
        else:
            new_idv += individual[i]
            
    return new_idv


def single_point_crossover(individual1, individual2):
    chance = random.random()
    if chance <= PROBABILITY_CROSSOVER:
        cross_point = random.randint(1, len(individual1))
        new_idv1 = individual1[0:cross_point] + individual2[cross_point:len(individual2)+1] 
        new_idv2 = individual2[0:cross_point] + individual1[cross_point:len(individual1)+1] 
    else:
        new_idv1 = individual1
        new_idv2 = individual2
    return new_idv1, new_idv2


def find_best_individual(population, target):
    max = -100
    best_idv = ""
    for i in range(NUM_POPULATION):
        idv = population[i*len(target):i*len(target)+len(target)]
        fit = fitness(target, idv)
        if fit > max:
            max = fit
            best_idv = idv
    return best_idv


def main():
    print(BANNER)
    prompt = input(INPUT).lower()
    while prompt == "y":
        sentence = input("\nPlease input the sentence you would like the program to guess: ").lower()

        found = False
        valid = False
        while not valid:         
            for ch in sentence:
                if ch not in ALPHABET:
                    print("\nIncorrect input. Please try again.\n")
                    sentence = input("\nPlease input the sentence you would like the program to guess: ").lower()
                    valid = False
                    break  
                else:
                    valid = True 

        population = make_population(sentence)
        print("\n\nGeneticGuess results:")
        printed = False
        for i in range(NUM_GENERATIONS):
            print(f"Generation: {i}")
            new_population = ""
            for j in range(NUM_POPULATION):
                idv1 = five_tournament_selection(population, sentence)
                idv2 = five_tournament_selection(population, sentence)

                mut_idv1 = mutation(idv1)
                mut_idv2 = mutation(idv2)
                new_idv1, new_idv2 = single_point_crossover(mut_idv1, mut_idv2)

                fit1 = fitness(sentence, new_idv1)
                fit2 = fitness(sentence, new_idv2)
                
                if fit1 > fit2:
                    new_idv = new_idv1
                    new_population += new_idv
                else: 
                    new_idv = new_idv2
                    new_population += new_idv 
                
                if (fit1 == 1) or (fit2 == 1):
                    if not printed:
                        print("I found the sentence early!")
                        print(f"\nBest Individual: {new_idv}")
                    printed = True
                    found = True
                    
            population = new_population
            
            if found == True:
                break

        if found == False:
          best = find_best_individual(population, sentence)
          print(f"\nBest Individual: {best}")

        prompt = input(INPUT).lower()
        if prompt == "n":
            print("\n\nThank you for using GeneticGuess Sentencer!")
        
if __name__ == '__main__':
    main()
