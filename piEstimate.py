import numpy as np
from matplotlib import pyplot as plt
import genPoints as gp
import math

# First, we need the amount of points to be established:

pointAmount = gp.generatePoints()

# generate the points, assuming 2D Space

randPoints = np.random.rand(pointAmount, 2)

# breakpoint()

# Calculating distance from origin, and determining point range for criteria

distances = np.sqrt(randPoints[:, 0]**2 + randPoints[:, 1]**2)

# breakpoint()

# Grabbing points within the circle

inside_circle = distances <= 1.0

# Estimating π value:
n_inside_circle = np.cumsum(inside_circle)
total_points = np.arange(1, pointAmount + 1)
estimated_pi = (n_inside_circle / total_points) * 4


plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.scatter(randPoints[inside_circle, 0],
            randPoints[inside_circle, 1], color='b', s=1)
plt.scatter(randPoints[~inside_circle, 0],
            randPoints[~inside_circle, 1], color='r', s=1)
plt.axis('equal')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Points')


plt.subplot(1, 2, 2)
plt.plot(total_points, estimated_pi)
plt.axhline(y=np.pi, color='r', linestyle='-')
plt.xlabel('No of Points Generated')
plt.ylabel('Estimated Value')
plt.title('Running Estimate')
plt.tight_layout()
plt.show()


print(f"The final estimate of π: {estimated_pi[-1]} is ",
      math.pi - estimated_pi[-1], "Shy of the actual value of π")
