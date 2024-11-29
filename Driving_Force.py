# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:23:22 2024

@author: Christian
"""
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # m/s^2, acceleration due to gravity
L = 1.0   # m, length of the pendulum
m = 1.0   # kg, mass of the pendulum bob 
F = 0.2   # Driving force amplitude
omega_d = 0.25  # Driving force frequency

# Initial conditions
theta0 = np.radians(20)  # Initial angle in radians
omega0 = 0.0  # Initial angular velocity in rad/s

# Time array
dt = 0.01  # time step
t = np.arange(0, 60, dt)  # Time span of 60 seconds

# Arrays to store theta and omega
theta = np.zeros(len(t))
omega = np.zeros(len(t))
KE = np.zeros(len(t))  # Kinetic energy 
PE = np.zeros(len(t))  # Potential energy 
TE = np.zeros(len(t))  # Total energy 

theta[0] = theta0
omega[0] = omega0

# Euler-Cromer method
for i in range(1, len(t)):
    omega[i] = omega[i - 1] + (- (g / L) * np.sin(theta[i - 1]) + F * np.cos(omega_d * t[i - 1])) * dt
    theta[i] = theta[i - 1] + omega[i] * dt
    KE[i] = 0.5 * m * L**2 * omega[i]**2 
    PE[i] = m * g * L * (1 - np.cos(theta[i])) 
    TE[i] = KE[i] + PE[i]

# Plot the result
plt.figure(figsize=(10, 6))
plt.plot(t, theta, label='Theta (rad)')
plt.plot(t, KE, label='Kinetic Energy') 
plt.plot(t, PE, label='Potential Energy') 
plt.plot(t, TE, label='Total Energy', linestyle='--') 
plt.title('Driven Nonlinear Pendulum Simulation using Euler-Cromer Method')
plt.xlabel('Time (s)')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()
