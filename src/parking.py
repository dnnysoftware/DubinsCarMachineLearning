import matplotlib.pyplot as plt
import numpy as np
import time

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


def genetic_algorithm(population, start_time, s0, sf_prime, plot, config):
    # Repeat until a fit enough individual is found or enough time has elapsed
    generation = 0
    while True and calculate_time_passed(start_time) < config['CONSTRAINTS']['MAX_EXEC_TIME_SEC'] and \
        generation <= config['CONSTRAINTS']['MAX_NUM_GEN']:
        dec_pop = convert_binary_population_to_decimal(population, config)
        generation += 1