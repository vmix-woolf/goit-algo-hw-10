import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def func(x):
    return np.log(x)

a, b = 1, 5  # Інтегруємо від 1 до 5

N = 10000  # Кількість випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, func(b), N)

under_curve = y_random < func(x_random)
box_square = (b - a) * func(b)
under_curve_points = np.sum(under_curve) / N
integral =  box_square * under_curve_points

print(f"Оцінка інтегралу методом Монте-Карло: {integral:.5f}")
# Обчислення інтеграла аналітично
result, error = spi.quad(func, a, b)

print("Оцінка інтегралу аналітичним методом: ", result)
print("Точність результату: ", error)

# Побудова графіка
x_vals = np.linspace(a, b, 100)
y_vals = func(x_vals)

plt.plot(x_vals, y_vals, label='y=log(x)', color='blue')
plt.scatter(x_random, y_random, c=under_curve, cmap='coolwarm', s=1, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Обчислення інтегралу методом Монте-Карло')
plt.legend()
plt.show()
