import matplotlib.pyplot as plt

from airplane import *
from rotation_matrixes import *
from scipy.spatial.transform import Rotation as R

airplane_0 = A_z(0) @ airplane

angle = 100
pause = 0.1

while True:
    airplane_now = airplane_0
    draw(airplane_0)
    plt.pause(pause)
    airplane_now = A_y(angle) @ airplane_now
    draw(airplane_now)
    plt.pause(pause)
    airplane_now = A_x(angle) @ airplane_now
    draw(airplane_now)
    plt.pause(pause)
    airplane_now = A_z(angle) @ airplane_now
    draw(airplane_now)
    plt.pause(pause)