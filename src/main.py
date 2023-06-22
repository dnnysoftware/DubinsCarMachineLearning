import numpy as np
import datetime as dt
import random
import time
import yaml
import graph
import parking


FILE = "config/config.yaml"

def parse_config():
    with open(FILE, "r") as f:
        return yaml.safe_load(f)
    

def generate_controls_file(individual):
    controls_file = open(f"log/controls-{dt.datetime.now()}.dat", "w")
    for i in individual:
        controls_file.write(f'Gamma: {i[0]} Beta: {i[1]}\n')
    controls_file.close()


def random_binary(config):
    # Convert the decimal value to a binary string with a specified number of bits
    value_bin = ''.join(random.choices(['0', '1'], k=config['GENETIC']['NUM_BITS_BIN']))
    return value_bin


def init_popluation(population_size, config):
    population = np.zeros((population_size, config['GENETIC']['NUM_GA_OPT_PARAMETERS'], 2), dtype=object)
    # Iterate over each individual in the population
    for i in range(population_size):
        # Iterate over each time step in the simulation
        for t in range(config['GENETIC']['NUM_GA_OPT_PARAMETERS']):
            gamma_bin = random_binary(config)
            beta_bin = random_binary(config)
            control_parameter = np.array([gamma_bin, beta_bin])
            population[i, t, :] = control_parameter
    return population


def main():
    config = parse_config()
    s0 = config['USER']['START']
    sf_prime = config['USER']['FINISH']
    population_size = config['USER']['POP_SIZE']
    plot = graph.create_plot()
    if population_size <= config['CONSTRAINTS']['MAX_POP_SIZE']:
        init_pop = init_popluation(population_size, config)
        start_time = time.time()
        opt_indv_state, opt_indv_control, times = parking.genetic_algorithm(init_pop, start_time, s0, sf_prime, plot, config)
        if opt_indv_state is not None and opt_indv_control is not None and times is not None:
            generate_controls_file(opt_indv_control)
            graph.graph_all(opt_indv_state, opt_indv_control, times)
        else:
            print("Couldn't find an optimal trajectory")
    else:
        print(f"Can't have population size exceed {config['CONSTRAINTS']['MAX_POP_SIZE']}")


if __name__ == '__main__':
    main()