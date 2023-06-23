import numpy as np

def is_feasible(s):
    # boundary conditions for trajectory planning
    if (s[0] <= -4 and s[1] > 3) or ((s[0] > -4 and s[0] < 4) and s[1] > -1) or (s[0] >= 4 and s[1] > 3):
        return True
    return False


def display_cost(gen_idx, cost):
    print(f'Generation {gen_idx} : J = {cost}')


def calculate_fitness(cost):
    # calculates g(i) which is the fitness of J(i)
    return 1 / (cost + 1)


def f(sk, uk):
    # Uses Eulers method to derive the next state
    # sk = [xk yk ak vk], uk = [yk Bk]
    xk_next = sk[3]* np.cos(sk[2])
    yk_next = sk[3]* np.sin(sk[2])
    ak_next = uk[0]
    vk_next = uk[1]
    sk_next = np.array([xk_next, yk_next, ak_next, vk_next])
    return sk_next


def calculate_euclidean_distance(sf, sf_prime):
    # calculates the cost (J) with feasible boundary conditions
    return ((sf_prime[0] - sf[0])**2 
            + (sf_prime[1] - sf[1])**2 
            + (sf_prime[2] - sf[2])**2 
            + (sf_prime[3] - sf[3])**2)**.5


def interpolate_individual(i, num_points):
    # Interpolates how many interpolated points betweem optimization parameters
    indices = np.arange(i.shape[0])
    new_indices = np.linspace(0, i.shape[0]-1, num_points*(i.shape[0]-1)+i.shape[0])
    interpolated_i = np.zeros((len(new_indices), i.shape[1]))
    for j in range(i.shape[1]):
        interpolated_i[:,j] = np.interp(new_indices, indices, i[:,j])
    return interpolated_i


def calculate_cost(sf, sf_prime, config):
    # sf_prime is required final state, sf is derived final state, K is infeasible constant
    if is_feasible(sf):
        return calculate_euclidean_distance(sf, sf_prime)
    else:
        return config['ODE']['K']


def calculate_eulers(T, dt, s0, individual):
    s = np.zeros((int(T / dt) + 1, 4))
    s[0, :] = s0
    t = np.zeros((int(T / dt) + 1,))
    t[0] = 0
    feasible = True
    for i in range(1, int(T / dt) + 1):
        k = f(s[i-1, :], individual[i - 1])
        s[i, :] = s[i-1, :] + k * dt
        t[i] = t[i-1] + dt
        if is_feasible(s[i]) == False:
            feasible = False
    return s, t, feasible