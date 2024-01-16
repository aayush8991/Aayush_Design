import numpy as np
import matplotlib.pyplot as plt
import scipy

def plot_function(x_values, y_values, color='blue'):
    plt.plot(x_values, y_values, color=color)
    plt.plot(x_values, -y_values, color=color)

functions = [lambda x: 0.8 * x, lambda x: 0.3 * x + 2, lambda x: 0.2 * x, lambda x: 1.143 * x - 4.66,
             lambda x: -0.8 * x, lambda x: -0.3 * x + 2, lambda x: -0.2 * x, lambda x: -1.143 * x - 4.66]

x_ranges = [(0, 3.95), (3.95, 7.9), (0, 4.9), (4.93, 7.9), (-3.95, 0), (-7.9, -3.95), (-4.9, 0), (-7.9, -4.93)]

for func, x_range in zip(functions, x_ranges):
    x_values = np.linspace(x_range[0], x_range[1], 100)
    y_values = func(x_values)
    plot_function(x_values, y_values)

def plot_function(func, x_range, color='blue'):
    x_values = np.linspace(x_range[0], x_range[1], 100)
    y_values = func(x_values)
    plt.plot(x_values, y_values, color=color)
    plt.plot(x_values, -y_values, color=color)

functions = [lambda x: 4.8 * x, lambda x: -4.8 * x, lambda x: x + 3.77, lambda x: -x + 3.77,
             lambda x: -3.5 * x - 7.3, lambda x: -1.2 * x, lambda x: 3.5 * x - 7.3, lambda x: 1.2 * x]

x_ranges = [(0, 1), (0, -1), (1, 4.44), (-4.44, -1), (-4.44, -3.18), (-3.18, 0), (3.18, 4.44), (0, 3.18)]

for func, x_range in zip(functions, x_ranges):
    plot_function(func, x_range)

def circle_eq1(x):
    return np.sqrt(1.6**2 - (x - 0)**2) + 5.3
def circle_eq(x):
    return np.sqrt(1.6**2 - (x + 5.5)**2)
def circle_eq2(x):
    return np.sqrt(1.6**2 - (x + 4.3)**2) + 4.3
def circle_eq3(y):
    return np.sqrt(1.6**2 - (y - 4.3)**2) - 7.5

x_values = np.linspace(-7.1, -5.5, 400)
x_values1 = np.linspace(-1.598, 1.598, 400)
x_values2 = np.linspace(-5.89, -3.75, 400)
x_values22 = np.linspace(-5.82, -5.89, 400)
y_values3 = np.linspace(3.8, 4.35, 400)

y_values1_pos = circle_eq1(x_values1)
y_values = circle_eq(x_values)
y_values2 = circle_eq2(x_values2)
y_values22 = circle_eq2(x_values22)
x_values3 = circle_eq3(y_values3)

def plot_symmetric(x, y, color='blue'):
    plt.plot(x, y, color=color)
    plt.plot(-x, y, color=color)
    plt.plot(-x, -y, color=color)
    plt.plot(x, -y, color=color)

plot_symmetric(x_values1, y_values1_pos)
plot_symmetric(x_values, y_values)
plot_symmetric(x_values2, y_values2)
plot_symmetric(x_values22, -y_values22)
plot_symmetric(x_values3, -y_values3)

def plot_function(func, x_range, color='blue'):
    x = np.linspace(*x_range, 100)
    plt.plot(x, func(x), color=color)
    plt.plot(-x, func(x), color=color)
    plt.plot(x, -func(x), color=color)
    plt.plot(-x, -func(x), color=color)

functions = [lambda x: 0.24 * x + 3.3, lambda x: -1.72 * x -6.85, lambda x: 0.6 * x + 3.8, lambda x: 4 * x + 13,
             lambda x: 4 * x + 20, lambda x: -0.6 * x + 4.8, lambda x: -1.72 * x - 8.64, lambda x: -0.25 * x -4.9]
x_ranges = [(-13.75, -5.76), (-9.51, -6.23), (3.83, 9.5), (-1.85, 0), (-3.25, 0), (-12, -4.17), (-12, -7.49), (-19.6, -6.86)]

for func, x_range in zip(functions, x_ranges):
    plot_function(func, x_range)


def circle_eq(x):
    return np.sqrt(4.38**2 - (x + 9.5)**2)

def circle_eq1(x):
    return -np.sqrt(4.38**2 - (x)**2) - 9.5

def circle_eq2(x):
    return np.sqrt(4.38**2 - (x)**2) - 9.5

def plot_circle_eq(circle_eq, x_values, color='blue'):
    y_values = circle_eq(x_values)
    plt.plot(x_values, y_values, color=color)
    plt.plot(x_values, -y_values, color=color)
    plt.plot(-x_values, y_values, color=color)
    plt.plot(-x_values, -y_values, color=color)

x_values = np.linspace(-7.5, -13.6, 400)
x_values1 = np.linspace(-4.38, -1.6, 400)
x_values2 = np.linspace(-4.38, -4.08, 400)

circle_eqs = [circle_eq, lambda x: -circle_eq1(x), circle_eq2]

for circle_eq, x_values in zip(circle_eqs, [x_values, x_values1, x_values2]):
    plot_circle_eq(circle_eq, x_values)

plt.show()