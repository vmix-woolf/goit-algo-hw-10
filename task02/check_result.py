import scipy.integrate as spi
import numpy as np

# Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
def f(x):
    return np.log(x)

# Визначте межі інтегрування, наприклад, від 0 до 1
a = 1  # нижня межа
b = 5  # верхня межа

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Integral: ", result)
print("Error level: ", error)
