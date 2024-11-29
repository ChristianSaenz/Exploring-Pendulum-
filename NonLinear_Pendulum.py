# -*- coding: utf-8 -*-
"""
Created on Wed May  8 16:06:56 2024

@author: Christian
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # m/s^2, acceleration due to gravity
L = 1.0   # m, length of the pendulum

# Initial conditions
theta0 = np.radians(40)  # Initial angle in radians, larger angle for more noticeable nonlinearity
omega0 = 0.0  # Initial angular velocity in rad/s

# Time array
dt = 0.01  # time step
t = np.arange(0, 20, dt)  # 20 seconds, with dt time step

# Arrays to store theta and omega
theta = np.zeros(len(t))
omega = np.zeros(len(t))
theta[0] = theta0
omega[0] = omega0

# Euler-Cromer method
for i in range(1, len(t)):
    omega[i] = omega[i - 1] - (g / L) * np.sin(theta[i - 1]) * dt  # Use sin(theta) instead of theta
    theta[i] = theta[i - 1] + omega[i] * dt

# Plot the result
plt.figure(figsize=(10, 6))
plt.plot(t, theta, label='Theta (rad)')
plt.title('Nonlinear Pendulum Simulation using Euler-Cromer Method')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.legend()
plt.grid(True)
plt.show()
