from pulp import *

# Define the problem
problem = LpProblem("Maximizing_beverage_production", LpMaximize)

# Define variables
lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Objective function
problem += lemonade + fruit_juice, "Total_Production"

# Constraints
problem += 2 * lemonade + fruit_juice <= 100, "Water"
problem += lemonade <= 50, "Sugar"
problem += lemonade <= 30, "Lemon_Juice"
problem += 2 * fruit_juice <= 40, "Fruit_Puree"

# Solve the problem
problem.solve()

# Print the results
print("Produce {} units of Lemonade".format(lemonade.varValue))
print("Produce {} units of Fruit Juice".format(fruit_juice.varValue))
print("Total units produced: {}".format(lemonade.varValue + fruit_juice.varValue))
