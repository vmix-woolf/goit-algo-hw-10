from pulp import LpMaximize, LpProblem, LpVariable

# model initialization
model = LpProblem(name="drink-production", sense=LpMaximize)

# number of beverage units produced
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# goal function - maximize the total number of drinks
model += lemonade + fruit_juice, "Total_Production"

# Limitations of resources
model += (2 * lemonade + fruit_juice <= 100, "Water_Limit")
model += (1 * lemonade <= 50, "Sugar_Limit")
model += (1 * lemonade <= 30, "Lemon_Juice_Limit")
model += (2 * fruit_juice <= 40, "Fruit_Puree_Limit")

model.solve()

# Виведення результатів
print(f"Optimal production of lemonade: {lemonade.varValue}")
print(f"Optimal production of fruit juice: {fruit_juice.varValue}")