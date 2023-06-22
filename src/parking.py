import matplotlib.pyplot as plt


def genetic_algorithm(population, start_time, s0, sf_prime, plot):
    # Repeat until a fit enough individual is found or enough time has elapsed
    generation = 0
