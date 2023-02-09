"""f(x) = -12x^4*sin(cos(x)) - 18x^3 + 5x^2 + 10x - 30

1. Определить корни
2. Найти интервалы, на которых функция возрастает
3. Найти интервалы, на которых функция убывает
4. Построить график
5. Вычислить вершину
6. Определить промежутки, на котором f > 0
7. Определить промежутки, на котором f < 0  """

import matplotlib.pyplot as plt
import numpy as np

a, b, c, d, e = -12, -18, 5, 10, -30

def func(x):
    return a * x**4 * np.sin(np.cos(x)) + b * x**3 + c * x**2 + d*x + e
    
limit = 23.626197999995878
step = 0.01
step_acr = 0.000001
line_style = '-'
color = 'b'
dir_up = True

def switch_line():
    global line_style
    if line_style == '-':
        line_style = '--'
    else:
        line_style = '-'
    return line_style


def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color

x = np.arange(-limit, limit + step, step)

x_change = [(-limit, 'limit')]      # создаем список картежей (значение по x, 'название') координат корней уравнения и точек смены направления функции

for i in range(len(x) - 1):
    if func(x[i]) > 0 and func(x[i + 1]) < 0 or func(x[i]) < 0 and func(x[i + 1]) > 0:    
        x_accur = np.arange(x[i], x[i+1] + step_acr, step_acr)
        for j in range(len(x_accur) - 1):
            if func(x_accur[j]) > 0 and func(x_accur[j + 1]) < 0 or func(x_accur[j]) < 0 and func(x_accur[j + 1]) > 0:
                x_change.append((x_accur[j], 'zero'))       # добавление в список значений по х координат корней
    if dir_up:
        if func(x[i]) > func(x[i + 1]):
            dir_up = False
            x_change.append((x[i], 'dir'))                  # добавление в список значений по х точки, где функция начинает убывать
    else:
        if func(x[i]) < func(x[i + 1]):
            dir_up = True
            x_change.append((x[i], 'dir'))                  # добавление в список значений по х точки, где функция начинает возрастать
x_change.append((limit, 'limit'))
# print(x_change)

for i in range(len(x_change) - 1):
    current_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.plot(x_change[i][0], func(x_change[i][0]), 'go')        
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(current_x, func(current_x), color)

    else:
        plt.plot(current_x, func(current_x), switch_color())

plt.plot(-limit, func(-limit), 'go', label = 'Функция не имеет решения(бесконечное множество корней)') 
plt.legend() 
plt.grid()
plt.show()


