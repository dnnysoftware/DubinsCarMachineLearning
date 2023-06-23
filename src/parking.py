import matplotlib.pyplot as plt
import numpy as np
import random
import time
import ode
import graph
import generations


def display_final_state(sf):
    print('Final state values:')
    print(f'x_f = {sf[0]}\ny_f = {sf[1]}\nalpha_f = {sf[2]}\nv_f = {sf[3]}')


def calculate_time_passed(start_time):
    # Calculates time passed from start of reinforcement process
    end_time = time.time()
    return end_time - start_time


def binary_to_decimal(value_bin):
    # Convert the binary string to a decimal value
    value_dec = int(value_bin, 2)
    return value_dec


def calculate_parameter_value(value_dec, value_range, num_bits):
    range_diff = value_range[1] - value_range[0]
    true_value = ((value_dec / (2**num_bits - 1))  * range_diff) + value_range[0]
    return true_value


def convert_binary_population_to_decimal(population, config):
    dec_population = np.zeros((len(population), config['GENETIC']['NUM_GA_OPT_PARAMETERS'], 2), dtype=float)
    i = 0
    for individual in population:
        # Iterate over each time step in the simulation
        p = 0
        for opt_para in individual:
            gamma_dec = binary_to_decimal(opt_para[0])
            gamma_actual = calculate_parameter_value(gamma_dec, config['ODE']['CONTROLS']['GAMMA_RANGE'], 
                                                            config['GENETIC']['NUM_BITS_BIN'] )
            beta_dec = binary_to_decimal(opt_para[1])
            beta_actual = calculate_parameter_value(beta_dec, config['ODE']['CONTROLS']['BETA_RANGE'], 
                                                           config['GENETIC']['NUM_BITS_BIN'] )
            control_parameter = np.array([gamma_actual, beta_actual])
            dec_population[i, p, :] = control_parameter
            p += 1
        i += 1
    return dec_population


def determine_cost_for_individual(individual, s0, sf_prime, config):
    num_points = 1 / config['ODE']['DT'] # the number of points between parameters each original parameter is 1 second between others
    interpolated_individual = ode.interpolate_individual(individual, int(num_points))
    states, times, feasible = ode.calculate_eulers(config['ODE']['T'], config['ODE']['DT'], s0, interpolated_individual)
    if feasible:
        return ode.calculate_cost(states[len(states) - 1], sf_prime, config), states, times, interpolated_individual
    return config['ODE']['K'], states, times, interpolated_individual


def genetic_algorithm(population, start_time, s0, sf_prime, plot, config):
    # Repeat until a fit enough individual is found or enough time has elapsed
    generation = 0
    while True and calculate_time_passed(start_time) < config['CONSTRAINTS']['MAX_EXEC_TIME_SEC'] and \
        generation <= config['CONSTRAINTS']['MAX_NUM_GEN']:
        dec_pop = convert_binary_population_to_decimal(population, config)
        costs = np.zeros((len(population)), dtype=float)
        times, states, interpolated_individuals = [], [], []
        for i in range(0, len(dec_pop)):
            cost, state_list, times_list, inter_indv = determine_cost_for_individual(dec_pop[i], s0, sf_prime, config)
            costs[i] = cost
            times = times_list
            states.append(state_list)
            interpolated_individuals.append(inter_indv)
        weights = [ode.calculate_fitness(c) for c in costs]
        next_population = []
        temp_combined_pop = generations.combine_gamma_beta(population, config)
        # random crossover of population size - 2 children because 2 with best cost go to next generation
        for _ in range(0, int(len(population) / 2) - 1):
            parent1, parent2 = random.choices(temp_combined_pop[:len(temp_combined_pop)-2], weights[:len(weights)-2], k=2)

            child1, child2 = generations.reproduce(parent1, parent2)

            child1 = generations.mutate(child1, config)
            child2 = generations.mutate(child2, config)
            next_population.append(child1)
            next_population.append(child2)
        min_cost_index, second_min_cost_index = generations.determine_top_two_elitism(costs)
        next_population.append(temp_combined_pop[second_min_cost_index[0]])
        next_population.append(temp_combined_pop[min_cost_index[0]])
        next_sep_pop = generations.separate_beta_gamma(next_population, config)
        population = next_sep_pop
        x = states[min_cost_index[0]][:, 0]
        y = states[min_cost_index[0]][:, 1]
        graph.plot_trajectory(x, y, plot)
        ode.display_cost(generation, min_cost_index[1])
        generation += 1
        for index, c in enumerate(costs):
            if c <= config['CONSTRAINTS']['J_TOL']:
                print()
                display_final_state(states[index][len(states[index]) - 1])
                plt.show()
                return states[index], interpolated_individuals[index], times
    return None, None, None