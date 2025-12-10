import numpy as np  # работа с линейной алгеброй (вектора, матрицы...)
import matplotlib.pyplot as plt  # графика и 3D-визуализация

airplane = np.array([
    [1.5, 0, 0],      # nose
    [-1, -1, 0],      # left wing tip
    [-1, 1, 0],       # right wing tip
    [-0.5, -0.5, 0],  # left inner wing
    [-0.5, 0.5, 0],   # right inner wing
    [-1.2, 0, 0],  # tail base
    [-0.9, 0, 0],    # tail tip
    [-0.8, -0.2, 0],# cockpit left
    [-0.8, 0.2, 0], # cockpit right
    [-1.3, 0, 0.7]      # vertical tail fin
]).T  # shape (3,10)

def draw(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.clear()
    ax.scatter(points[0], points[1], points[2], c='black', s=50)
    # линии между ключевыми точками
    ax.plot([points[0,0], points[0,1]], [points[1,0], points[1,1]], [points[2,0], points[2,1]], c='gray')  # nose → left wing
    ax.plot([points[0,0], points[0,2]], [points[1,0], points[1,2]], [points[2,0], points[2,2]], c='gray')  # nose → right wing
    ax.plot([points[0,5], points[0,6]], [points[1,5], points[1,6]], [points[2,5], points[2,6]], c='gray')  # tail
    ax.plot([points[0,6], points[0,9]], [points[1,6], points[1,9]], [points[2,6], points[2,9]], c='gray')  # vertical fin

    # Добавляем оси координат
    axis_length = 2.0
    # Ось X (красная)
    ax.quiver(0, 0, 0, axis_length, 0, 0, color='red', arrow_length_ratio=0.1, linewidth=2)
    ax.text(axis_length, 0, 0, 'X', color='red', fontsize=12)
    # Ось Y (зелёная)
    ax.quiver(0, 0, 0, 0, axis_length, 0, color='green', arrow_length_ratio=0.1, linewidth=2)
    ax.text(0, axis_length, 0, 'Y', color='green', fontsize=12)
    # Ось Z (синяя)
    ax.quiver(0, 0, 0, 0, 0, axis_length, color='blue', arrow_length_ratio=0.1, linewidth=2)
    ax.text(0, 0, axis_length, 'Z', color='blue', fontsize=12)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

def show():
    plt.show()
