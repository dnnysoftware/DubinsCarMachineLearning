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


def plot_trajectory(x, y, plot):
    fig, ax = plot
    if not ax.lines:
        trajectory_line, = ax.plot([], [], 'b')
    else:
        trajectory_line = ax.lines[0]
        trajectory_line.set_data([],[])
    ax.plot([-15, -4], [3, 3], 'k-')
    ax.plot([-4, -4], [-1, 3], 'k-')
    ax.plot([-4, 4], [-1, -1], 'k-')
    ax.plot([4, 4], [-1, 3], 'k-')
    ax.plot([15, 4], [3, 3], 'k-')
    trajectory_line.set_data(x, y)
    fig.canvas.draw()
    plt.show(block=False)
    plt.pause(0.001)


def plot_x_state(states, times):
    x = states[:, 0]
    t = times
    f = CubicSpline(t, x, bc_type='natural')
    t_new = np.linspace(0, 10, 100)
    x_new = f(t_new)
    plt.figure(figsize = (8,6))
    plt.plot(t_new, x_new, 'b')
    # Axes bounds 
    plt.xlim([0, 10])
    plt.ylim([-15, 15])
    # Labels
    plt.title('X-Pos State')
    plt.ylabel('x (ft)')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.show()


def plot_y_state(states, times):
    y = states[:, 1]
    t = times
    f = CubicSpline(t, y, bc_type='natural')
    t_new = np.linspace(0, 10, 100)
    y_new = f(t_new)
    plt.figure(figsize = (8, 6))
    plt.plot(t_new, y_new, 'b')
    # Axes bounds 
    plt.xlim([0, 10])
    plt.ylim([-15, 15])
    # Labels
    plt.title('Y-Pos State')
    plt.ylabel('y (ft)')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.show()


def plot_a_state(states, times):
    t = times
    a = states[:, 2]
    f = CubicSpline(t, a, bc_type='natural')
    t_new = np.linspace(0, 10, 100)
    a_new = f(t_new)
    plt.figure(figsize = (8, 6))
    plt.plot(t_new, a_new, 'b')
    # Axes bounds 
    plt.xlim([0, 10])
    plt.ylim([-6.28319, 6.28319])
    # Labels
    plt.title('Heading Angle State')
    plt.ylabel('a (rad)')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.show()


def plot_v_state(states, times):
    t = times
    v = states[:, 3]
    f = CubicSpline(t, v, bc_type='natural')
    t_new = np.linspace(0, 10, 100)
    v_new = f(t_new)
    plt.figure(figsize = (8, 6))
    plt.plot(t_new, v_new, 'b')
    # Axes bounds 
    plt.xlim([0, 10])
    plt.ylim([-10, 10])
    # Labels
    plt.title('Velocity State')
    plt.ylabel('v (ft/s)')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.show()


def plot_y_control(controls, times):
    t = times[0:100]
    y = controls[:, 0]
    f = CubicSpline(t, y, bc_type='natural')
    t_new = np.linspace(0, 10, 100)
    y_new = f(t_new)
    plt.figure(figsize = (8,6))
    plt.plot(t_new, y_new, 'b')
    # Axes bounds 
    plt.xlim([0, 10])
    plt.ylim([-0.524, 0.524])
    # Labels
    plt.title('Heading Angle Rate Control')
    plt.ylabel('y (rad/s)')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.show()


def plot_B_control(controls, times):
    t = times[0:100]
    b = controls[:, 1]
    f = CubicSpline(t, b, bc_type='natural')
    t_new = np.linspace(0, 10, 100)
    B_new = f(t_new)
    plt.figure(figsize = (8,6))
    plt.plot(t_new, B_new, 'b')
    # Axes bounds 
    plt.xlim([0, 10])
    plt.ylim([-5, 5])
    # Labels
    plt.title('Acceleration Control')
    plt.ylabel('B (ft/s^2)')
    plt.xlabel('Time (s)')
    plt.grid()
    plt.show()


def graph_all(opt_indv_state, opt_indv_control, times):
    plot_x_state(opt_indv_state, times)
    plot_y_state(opt_indv_state, times)
    plot_a_state(opt_indv_state, times)
    plot_v_state(opt_indv_state, times)
    plot_y_control(opt_indv_control, times)
    plot_B_control(opt_indv_control, times)