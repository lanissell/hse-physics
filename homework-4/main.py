from airplane import airplane, draw, show
from rotation_matrixes import A_z, A_y
import numpy as np

# 1. Исходное положение
draw(airplane)

# 2. Нормальный поворот (Z-Y-Z)
psi1 = 60
theta1 = 30
phi1 = 0

# Матрица поворота для последовательности Z-Y-Z (поворот вокруг новых осей)
R1 = A_z(psi1) @ A_y(theta1) @ A_z(phi1)
airplane_rotated1 = R1 @ airplane
draw(airplane_rotated1)

# 3. Выражаемость (Gimbal Lock)

# Случай 1
psi2 = -90
theta2 = 0
phi2 = 0
R2 = A_z(psi2) @ A_y(theta2) @ A_z(phi2)
airplane_gimbal1 = R2 @ airplane
draw(airplane_gimbal1)

# Случай 2
psi3 = -45
theta3 = 0
phi3 = -45
R3 = A_z(psi3) @ A_y(theta3) @ A_z(phi3)
airplane_gimbal2 = R3 @ airplane
draw(airplane_gimbal2)

# Случай 3
psi4 = 0
theta4 = 0
phi4 = -90
R4 = A_z(psi4) @ A_y(theta4) @ A_z(phi4)
airplane_gimbal3 = R4 @ airplane
draw(airplane_gimbal3)

# Проверим, что матрицы поворота.
print("Матрицы поворота R2 и R3 идентичны?", np.allclose(R2, R3))
print("Матрицы поворота R2 и R4 идентичны?", np.allclose(R2, R4))
print("Матрицы поворота R3 и R4 идентичны?", np.allclose(R3, R4))

# Показываем все графики
show()
