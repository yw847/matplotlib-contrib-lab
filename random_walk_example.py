"""
2D Random Walk

This example simulates a 2D random walk using unit steps in the x and y
directions. It visualizes the path of the walker over time.
"""

import numpy as np
import matplotlib.pyplot as plt


# Create random number generator
rng = np.random.default_rng(seed=0)

# Generate random steps: -1 or +1
steps = rng.choice([-1, 1], size=(1000, 2))

# Compute cumulative position (the walk path)
path = np.cumsum(steps, axis=0)

# Extract x and y coordinates
x = path[:, 0]
y = path[:, 1]

# Plot the path
plt.plot(x, y, label="Random Walk Path")

# Mark start and end
plt.scatter(x[0], y[0], color="green", label="Start")
plt.scatter(x[-1], y[-1], color="red", label="End")

plt.title("2D Random Walk")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.legend()
plt.axis("equal")

plt.show()