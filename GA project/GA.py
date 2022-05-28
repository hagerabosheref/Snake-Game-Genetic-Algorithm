# Hager Mohamed Abdo Abdo Abo Sheref
# Snake game using Genetic algorithm
 
import numpy as np
import math
import random

#############
# random position for food
position_food = []
xfood=random.randint(-260,260)
yfood=random.randint(-260,260)
position_food.append(xfood)
position_food.append(yfood)
#print(position_food)

##############################################
# creating an initial population randomly (8 x 4)
def init_pop():
    pop=[]
    dirc_list = []
    chromosome = []
    for i in range(8):
        directions = ['left', 'right', 'up', 'down']
        np.random.shuffle(directions)
        dirc_list.append(directions)
    #print(dirc_list)     
    list_num = np.random.randint(13, size=(8,4))   # range 0 to 12 (steps)#
    #print(list_num) 
    list_concate = [] # gene ----> [steps, direction]
    for i in range(8):
        for j in range(4):
            list_concate.append(list_num[i][j])
            list_concate.append(dirc_list[i][j])
            chromosome.append(list_concate)
            list_concate = []
        pop.append(chromosome)   
        chromosome = []
    return pop

#print(init_pop()) ###Just to try the function   


##############################################
# 20 (size of step)
# left  ----> step * -20  ---->  x_axis
# right ----> step * 20   ---->  x_axis
# up    ----> step * 20   ---->  y_axis
# down  ----> step * -20  ---->  y_axis 
# fitness ----> distance <= 40 
# fitness function
def calc_fitness(population, pos_food, pos_snake):
    #print(population)
    fitness_vals = [] # distance between food and snake
    for i in range(8):
        x_axis = 0 
        y_axis = 0        
        for j in range(4):
            if(population[i][j][1] == 'right'):
                x_axis += population[i][j][0] * 20
            elif(population[i][j][1] == 'left'):
                x_axis += population[i][j][0] * -20
            elif(population[i][j][1] == 'up'):
                y_axis += population[i][j][0] * 20
            elif(population[i][j][1] == 'down'):
                y_axis += population[i][j][0] * -20 
        x_pos_snake = pos_snake[0] + x_axis    
        y_pos_snake = pos_snake[1] + y_axis
        distance = round(math.sqrt( pow((x_pos_snake - pos_food[0]),2) + pow((y_pos_snake - pos_food[1]),2)),2) # Euclidean distance
        fitness_vals.append(distance)
    return np.array(fitness_vals)                            

#print(calc_fitness(init_pop(),(0,100),(0,0))) ###Just to try the function 

 
##############################################
# selection function
def selection(population, fitness_vals):
    #population = np.array(population)          # <<< Just to try
    #probs = np.array(fitness_vals)             # <<< Just to try
    probs = fitness_vals.copy()
    probs = 1 / probs  
    #print(probs)
    probs = probs / probs.sum()
    #print(probs)
    indices = np.arange(8)
    select_indices = np.random.choice(indices, size = 8 , p = probs)
    #print(select_indices)
    selected_population = []
    for i in range(8):
        selected_population.append(population[select_indices[i]])    
    return selected_population

'''print(selection(
    [[[0, 'down'], [7, 'left'], [9, 'up'], [11, 'right']], 
    [[4, 'left'], [11, 'right'], [9, 'down'], [8, 'up']], 
    [[6, 'up'], [4, 'left'], [7, 'down'], [7, 'right']], 
    [[5, 'right'], [11, 'down'], [6, 'up'], [11, 'left']], 
    [[7, 'right'], [3, 'left'], [3, 'up'], [11, 'down']], 
    [[5, 'up'], [0, 'left'], [12, 'right'], [5, 'down']], 
    [[10, 'left'], [8, 'down'], [4, 'up'], [11, 'right']], 
    [[10, 'up'], [4, 'right'], [11, 'down'], [6, 'left']]],
    [113.14, 184.39, 134.16, 233.24, 272.03, 260.0, 181.11, 126.49]))''' ###Just to try the function 


##############################################
# crossover function (single point)
def crossover(parent1, parent2 , pc):
    r = np.random.random() # range 0 between 1 ||| exclusive(0,1)
    if r < pc:
        m = np.random.randint(1,4)  # range 1 to 3 
        #print(m)
        child1 = parent1[:m] + parent2[m:] #if choose 3, 0 to (3-1) for parent1 3 to end for parent2
        child2 = parent2[:m] + parent1[m:]
    else:
        child1 = parent1.copy()
        child2 = parent2.copy()
    return child1, child2

#print(crossover([[8, 'down'], [6, 'left'], [9, 'up'], [5, 'right']], [[2, 'up'], [10, 'left'], [4, 'right'], [1, 'down']],0.9)) ###Just to try the function   


##############################################
# mutation function (swap)
def mutation(individual, pm):
    #print(individual)
    r = np.random.random() # range 0 between 1 ||| exclusive(0,1)
    if r < pm: 
        m = np.random.randint(4) # range 0 to 3  because columns are integer numbers between 0 to 3 
        n = np.random.randint(4)
        #print(m,n)
        x = individual[m].copy() # prevent aliasing
        #print(x)
        #print(individual[n])
        individual[m] = individual[n]
        individual[n] = x
 
    return individual 

#print(mutation([[8, 'down'], [6, 'left'], [9, 'up'], [5, 'right']],0.9)) ###Just to try the function   


##############################################
# crossover && mutation
def crossover_mutation(seleted_population, pc, pm):
    #print(seleted_population)
    new_pop = []
    for i in range(0,8,2):
        parent1 = seleted_population[i]
        parent2 = seleted_population[i+1]
        child1, child2 = crossover(parent1, parent2, pc)
        new_pop.append(child1)
        new_pop.append(child2)
    for i in range(8):
        mutation(new_pop[i], pm)
    return  new_pop

#print(crossover_mutation([[[8, 'down'], [6, 'left'], [9, 'up'], [5, 'right']], [[2, 'up'], [10, 'left'], [4, 'right'], [1, 'down']]],0.9,0.9)) ###Just to try the function


##############################################
# snake game
def snake_game(num_generation, pc, pm):
    population = init_pop()
    best_fitness_overall = None
    all_generation = [] # all generation
    all_fitness = []
    for generation in range(num_generation):
        every_generation = [] # every generation
        every_generation.append(population)
        all_generation.append(every_generation)
        fitness_val = calc_fitness(population, position_food, [0, 0])
        every_fitness = []
        every_fitness.append(fitness_val)
        all_fitness.append(every_fitness)
        best_i = fitness_val.argmin()
        best_fitness = fitness_val[best_i]
        if best_fitness_overall == None or best_fitness < best_fitness_overall:
            best_fitness_overall = best_fitness
            best_solution = population[best_i]
        print(f'generation={generation+1}  fitness={best_fitness}')
        if best_fitness <= 60:
            print('found optimal solution')
            break
        selected_population = selection(population,fitness_val)
        population = crossover_mutation(selected_population, pc, pm)
    print(best_solution)
    return all_generation, all_fitness, position_food 

#print(snake_game(2,0.9,0.9))      
 