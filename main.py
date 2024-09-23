import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sin, cos, pi
from sys import exit

wheel_radius = float(input('Enter wheel radius, meters: '))
if wheel_radius <= 0:
    raise Exception('Radius cannot be less than or equal to zero')

center_mass_velocity = float(input('Enter center of mass velocity, meters per second: '))

cycloid_period = 2 * pi * wheel_radius

if center_mass_velocity != 0:
    delta_t = 0.2 / abs(center_mass_velocity) * wheel_radius
else:
    delta_t = 0.2

t = 0.0
x_values = [center_mass_velocity * t - wheel_radius * sin(center_mass_velocity / wheel_radius * t)]
y_values = [wheel_radius - wheel_radius * cos(center_mass_velocity / wheel_radius * t)]
t += delta_t

fig, ax = plt.subplots()
graph = ax.plot(x_values, y_values)[0]
plt.xlabel('x, meters')
plt.ylabel('y, meters')
plt.ylim(0, wheel_radius * 2)


def update(frame):
    global t

    x = center_mass_velocity * t - wheel_radius * sin(center_mass_velocity / wheel_radius * t)
    y = wheel_radius - wheel_radius * cos(center_mass_velocity / wheel_radius * t)

    x_values.append(x)
    y_values.append(y)

    graph.set_xdata(x_values)
    graph.set_ydata(y_values)

    if center_mass_velocity > 0:
        plt.xlim(x_values[-1] - cycloid_period, x_values[-1])
    else:
        plt.xlim(x_values[-1], x_values[-1] + cycloid_period)

    t += delta_t

anim = FuncAnimation(fig, update, frames = None)
plt.show()
exit()
