import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
s = 2  # начальное расстояние от лодки до катера
fi = 3 * np.pi / 4


def f(r, theta):  # функция, описывающая движение катера береговой охраны
    dr = r / np.sqrt(3)
    return dr


# начальные условия
r0 = s
theta0 = - np.pi
theta = np.arange(0, 2 * np.pi, .01)
r = odeint(f, r0, theta)
t = np.arange(0, 800, 1)


def f2():  # функция, описывающая движение лодки браконьеров
    xt = np.tan(fi) * t
    return xt


rect1 = [0.2, 0.2, 0.7, 0.7]
fig = plt.figure(figsize=(8., 6.))
plt.polar(theta, r)  # построение траектории движения катера в полярных координатах
plt.plot(t, f2())  # построение траектории движения лодки
plt.show()
