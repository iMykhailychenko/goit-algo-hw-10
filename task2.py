import scipy.integrate as sci
import numpy as np


# Визначення функції та межі інтегрування
def f(x):
    return x**2


a = 0  # Нижня межа
b = 2  # Верхня межа


def mc_integral(a, b, num_samples=10000):
    x = np.random.uniform(a, b, num_samples)
    y = np.random.uniform(0, f(b), num_samples)

    points_under_curve = sum(y <= f(x))
    area_ratio = points_under_curve / num_samples

    total_area = (b - a) * f(b)
    return total_area * area_ratio


if __name__ == "__main__":
    print(f"Numeric integral: {sci.quad(f, a, b)[0]}")

    num_samples = (100, 1000, 10000, 100000, 1000000, 10000000)
    for sample in num_samples:
        print(
            f"Monte Carlo integral ({sample}): {mc_integral(a, b, num_samples=sample)}"
        )
