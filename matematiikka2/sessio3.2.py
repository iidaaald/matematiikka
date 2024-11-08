'''
Kuvan oletuskoko 6.4 * 4.8 tuumaa. Haluat tehdä kuvaajan väliltä -3π - 3π. Levennä kuva kolminkertaiseksi
ja vaihdä käyrien värit sekä piirtotyyli. Lisää myöskin kuvaan selite.
'''
from matplotlib import pyplot as plt, patches
import numpy as np

# Set figure size to three times the default width (default is 6.4x4.8)
fig = plt.figure(figsize=(19.2, 4.8))  # 3x the default width
ax = fig.subplots()

# Draw the unit circle
ymp = patches.Circle((0, 0), radius=1, fill=False, color='gray', linestyle='--')
ax.add_patch(ymp)

# Move axes to the center
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Set axis limits to -3π to 3π
ax.set_xlim(-3 * np.pi, 3 * np.pi)
ax.set_ylim(-1.5, 1.5)  # Extended y-axis for visibility of curves

# Define x values from -3π to 3π
x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

# Plot cos(x) and sin(x) with different colors and line styles
ax.plot(x, np.cos(x), color='blue', linestyle='-', label='cos(x)')
ax.plot(x, np.sin(x), color='red', linestyle='--', label='sin(x)')

# Add a legend
ax.legend(loc='upper right')

# Calculate and plot the points for the specified angles on the unit circle
degrees = [30, 45, 60, 90, 120, 150, 180, 270]
radians = np.radians(degrees)
points_x = np.cos(radians)
points_y = np.sin(radians)

# Plot the points on the unit circle
plt.scatter(points_x, points_y, color='blue', marker='X')

# Display the plot
plt.show()
