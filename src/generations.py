import numpy as np
import random

def combine_gamma_beta(population, config):
    combined_pop = np.zeros((len(population), config['GENETIC']['NUM_GA_OPT_PARAMETERS']), dtype=object)
    for i, individual in enumerate(population):
        for j, para in enumerate(individual):
            combined_string = ''.join(para)
            combined_pop[i][j] = combined_string
    return combined_pop


def separate_beta_gamma(combined_pop, config):
    separated_pop = np.zeros((len(combined_pop), config['GENETIC']['NUM_GA_OPT_PARAMETERS'], 2), dtype=object)
    for i, individual in enumerate(combined_pop):
        for j, para in enumerate(individual):
            gamma = para[:config['GENETIC']['NUM_BITS_BIN']]
            beta = para[config['GENETIC']['NUM_BITS_BIN']:]
            control_parameter = np.array([gamma, beta])
            separated_pop[i, j, :] = control_parameter
    return separated_pop


def reproduce(parent1, parent2):
    # Choose a random point to split the parents' strings
    n = len(parent1)
    p_index = random.randint(0, n-1)
    n_bin = len(parent1[p_index])
    crossover_index = random.randint(1, n_bin-1)
    # Combine the substrings to create a child
    child1 = parent1
    child2 = parent2
    changedparam1 = parent1[p_index][:crossover_index] + parent2[p_index][crossover_index:]
    changedparam2 = parent2[p_index][:crossover_index] + parent1[p_index][crossover_index:]
    child1[p_index] = changedparam1
    child2[p_index] = changedparam2
    return child1, child2


def mutate(individual, config):
    # Takes in i = [y_0 B_0 ... y_n B_n] string of bits (0, 1), iterates through
    # them and flips the value depending if it fits the mutation boundary of 0.5% 
    mutated_individual = np.zeros((len(individual)), dtype=object)
    j = 0
    for p in individual:  
        mutated = ""
        for i in range(0, len(p)):
            percent = round(random.uniform(0, 100), 2)
            if percent <= config['GENETIC']['MUTATION_RATE']:
                if p[i] == '0':
                    mutated += '1'
                else:
                    mutated += '0'
            else:
                mutated += p[i]
        mutated_individual[j] = mutated
        j += 1
    return mutated_individual


def determine_top_two_elitism(costs):
    costs = np.array(costs)
    sorted_indices = np.argsort(costs)
    two_smallest_indices = np.array(sorted_indices[:2], dtype=int)
    two_smallest_values = costs[two_smallest_indices]
    result = tuple(zip(two_smallest_indices, two_smallest_values))
    return result[0], result[1]
