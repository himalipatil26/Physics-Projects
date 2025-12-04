# Simple Pendulum Simulation - Class 11 Physics Project
# Formula: T = 2π * sqrt(L / g)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print("=== Simple Pendulum Simulation ===")
print("This program simulates a simple pendulum and verifies T ∝ √L.\n")

# constants
g = 9.81  # acceleration due to gravity (m/s^2)

# take user input for different pendulum lengths
lengths = []
for i in range(3):
    L = float(input(f"Enter length of pendulum {i+1} (in meters): "))
    lengths.append(L)

# calculate period for each length
periods = [2 * np.pi * np.sqrt(L / g) for L in lengths]

print("\nLength (m)\tPeriod (s)")
for L, T in zip(lengths, periods):
    print(f"{L:.2f}\t\t{T:.2f}")

# plot T vs sqrt(L)
plt.figure()
plt.title("Verification of T ∝ √L")
plt.xlabel("√Length (m^0.5)")
plt.ylabel("Time Period (s)")
plt.grid(True)
plt.plot(np.sqrt(lengths), periods, marker='o')
plt.show()

# --- Simple Animation for one pendulum ---
L = lengths[0]
T = 2 * np.pi * np.sqrt(L / g)
theta_max = 0.2  # small angle in radians

fig, ax = plt.subplots()
ax.set_xlim(-L-0.2, L+0.2)
ax.set_ylim(-L-0.2, 0.2)
ax.set_aspect('equal')
ax.set_title("Simple Pendulum Motion")

line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(t):
    theta = theta_max * np.cos(2 * np.pi * t / T)
    x = L * np.sin(theta)
    y = -L * np.cos(theta)
    line.set_data([0, x], [0, y])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, T, 200),
                              init_func=init, blit=True, interval=30, repeat=True)

plt.show()
print("\nSimulation complete. Thank you for using the Simple Pendulum Simulation!")

