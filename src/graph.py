import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

def create_plot():
    fig, ax = plt.subplots(figsize=(8, 6))

    # wall bounds
    ax.plot([-15, -4], [3, 3], 'k-')
    ax.plot([-4, -4], [-1, 3], 'k-')
    ax.plot([-4, 4], [-1, -1], 'k-')
    ax.plot([4, 4], [-1, 3], 'k-')
    ax.plot([15, 4], [3, 3], 'k-')

    # dimensions
    ax.set_xlim([-15, 15])
    ax.set_ylim([-15, 15])

    # labels
    ax.set_title('State Trajectory')
    ax.set_xlabel('x (ft)')
    ax.set_ylabel('y (ft)')
    ax.grid()
    return (fig, ax)

def graph_all(opt_indv_state, opt_indv_control, times):
    pass