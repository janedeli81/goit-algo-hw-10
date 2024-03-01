import numpy as np
from scipy.integrate import quad

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2
max_y = 4  # Максимальне значення y, оскільки f(2) = 4

# Кількість рандомізованих точок для методу Монте-Карло
n_points = 100000

# Генеруємо випадкові точки
x_random = np.random.uniform(a, b, n_points)
y_random = np.random.uniform(0, max_y, n_points)

# Визначаємо, які точки знаходяться під кривою
points_under_curve = y_random < f(x_random)

# Розрахунок площі під кривою методом Монте-Карло
area_under_curve = points_under_curve.sum() / n_points * (b - a) * max_y

# Аналітичний розрахунок інтегралу
def analytic_integral(x):
    return (1/3) * x ** 3

analytic_result = analytic_integral(b) - analytic_integral(a)

# Розрахунок за допомогою quad
quad_result, _ = quad(f, a, b)

(area_under_curve, analytic_result, quad_result)
