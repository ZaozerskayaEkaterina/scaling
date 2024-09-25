# 5. Изобразить плавное масштабирование квадрата вдоль осей ОХ и OY.
# Коэффициенты масштабирования по осям различны. Центр квадрата не находится на координатных
# осях, а стороны квадрата не совпадают с направлением координатных осей.

import numpy as np
import matplotlib.pyplot as plt
import time

# Параметры квадрата
square_size = 0.5  # Для координат точек
in_center = np.array([0, 0])  # Центр квадрата
scale_increment_x = 0.5  # Скорость масштабирования по оси X
scale_increment_y = 0.2  # Скорость масштабирования по оси Y


# Определение начальных вершин квадрата
def get_square_vertices(size):
    vertices = np.array([
        [-size, -size, 1],
        [size, -size, 1],
        [size, size, 1],
        [-size, size, 1],
        [-size, -size, 1]  # Замыкание (левая нижняя вершина)
    ])
    return vertices


# Масштабирование
def transform_vertices(vertices, scale_x, scale_y):
    # Создание матрицы преобразования
    transformation_matrix = np.array([
        [scale_x, 0, 0],
        [0, scale_y, 0],
        [0, 0, 1]
    ])

    # Применяем преобразование
    new_transformed_vertices = vertices @ transformation_matrix.T
    return new_transformed_vertices


# Инициализация графика
plt.figure()
plt.xlim(-3, 3)
plt.ylim(-3, 3)

# Коэффициенты масштабирования по оси X и Y.
in_scale_x = 1.0
in_scale_y = 1.0

# Получаем начальные вершины квадрата в гомогенных координатах
square_vertices = get_square_vertices(square_size)

# Время начала анимации
start_time = time.time()
duration = 3  # Длительность анимации в секундах

# Анимация
while time.time() - start_time < duration:

    # Применяем преобразование (масштабирование)
    transformed_vertices = transform_vertices(square_vertices, in_scale_x, in_scale_y)

    # Очищаем предыдущий график и рисуем новый
    plt.clf()
    plt.xlim(-3, 3)
    plt.ylim(-3, 3)
    plt.plot(transformed_vertices[:, 0], transformed_vertices[:, 1], color='green')

    # Обновляем параметры масштабирования
    in_scale_x += scale_increment_x * (time.time() - start_time) / duration
    in_scale_y += scale_increment_y * (time.time() - start_time) / duration

    plt.pause(0.1)

plt.show()
