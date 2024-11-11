import numpy as np
import matplotlib.pyplot as plt


h = 100  # Height from which the ball is dropped (in meters)
g = 9.8  # Gravitational acceleration (in m/s^2)

# Calculate the time it takes for the ball to hit the ground

t_max = np.sqrt(2 * h / g)  # Time to reach the ground (using y = 0)

# We'll divide the fall time into 100 intervals (including the final time point)
num_steps = 100

time_steps = np.linspace(0, t_max, num_steps)

positions = h - 0.5 * g * time_steps**2


# This gives us the distance fallen between each time step
distance_fallen = np.diff(positions)

average_distance_fallen = np.mean(distance_fallen)

# Print results
print(f"Time to hit the ground: {t_max:.2f} seconds")
print(f"Average distance fallen per time step: {
      average_distance_fallen:.2f} meters")

# 6. Plot the motion of the ball over time
plt.plot(time_steps, positions, label="Position of the ball")
plt.xlabel('Time (seconds)')
plt.ylabel('Height (meters)')
plt.title('Free Fall of a Ball')
plt.grid(True)
plt.legend()
plt.show()
