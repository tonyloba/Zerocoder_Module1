"""
В этом коде:
- `np.random.rand(num_samples)` генерирует массив из случайных чисел, равномерно распределенных в диапазоне от 0 до 1. Два таких массива создаются для осей X и Y.
- `plt.scatter(data_x, data_y, alpha=0.7, color='blue', edgecolor='black')` создает диаграмму рассеяния из сгенерированных данных. Параметры `alpha`, `color`, и `edgecolor` позволяют настроить внешний вид точек.
- Заголовок и метки осей добавляются с помощью `plt.title`, `plt.xlabel`, и `plt.ylabel`.
- `plt.show()` отображает диаграмму рассеяния.

"""

import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 5  # Количество образцов
data_x = np.random.rand(num_samples)
data_y = np.random.rand(num_samples)

# Создание диаграммы рассеяния
plt.scatter(data_x, data_y, alpha=0.7, color='blue', edgecolor='black')

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')

# Показать диаграмму рассеяния
plt.show()