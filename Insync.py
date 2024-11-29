# -*- coding: utf-8 -*-
"""
Created on Sat May 18 12:41:35 2024

@author: Christian
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
g = 9.81  # Acceleration due to gravity (m/s^2)
L = 1.0   # Length of each pendulum (m)
m = 1.0   # Mass of each pendulum (kg)
k = 10 # Spring constant (N/m)
dt = 0.01 # Time step (s)
T = 80    # Total time (s)

# Initial conditions
theta1_0, omega1_0 = np.radians(20), 0  # Pendulum 1
theta2_0, omega2_0 = np.radians(-20), 0  # Pendulum 2

# Time array
t = np.arange(0, T, dt)

# Initialize arrays to store data
theta1 = np.zeros_like(t)
omega1 = np.zeros_like(t)
theta2 = np.zeros_like(t)
omega2 = np.zeros_like(t)
theta1[0], omega1[0] = theta1_0, omega1_0
theta2[0], omega2[0] = theta2_0, omega2_0

# Simulation loop
for i in range(1, len(t)):
    # Dynamics of pendulum 1
    torque1 = -m*g*L*np.sin(theta1[i-1]) - k*(theta1[i-1] - theta2[i-1]) 
    omega1[i] = omega1[i-1] + torque1/m/L*dt
    theta1[i] = theta1[i-1] + omega1[i]*dt

    # Dynamics of pendulum 2
    torque2 = -m*g*L*np.sin(theta2[i-1]) - k*(theta2[i-1] - theta1[i-1]) 
    omega2[i] = omega2[i-1] + torque2/m/L*dt
    theta2[i] = theta2[i-1] + omega2[i]*dt

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(t, theta1, label='Theta 1 (rad)')
plt.plot(t, theta2, label='Theta 2 (rad)')
plt.title('Dynamics of Coupled Pendulums')
plt.xlabel('Time (s)')
plt.ylabel('Angular Displacement (rad)')
plt.legend()
plt.grid(True)
plt.show()
