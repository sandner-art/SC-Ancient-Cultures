import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Set plot style for publication quality
plt.style.use(['science', 'ieee'])

# Royal cubit approximation (π/6 meters)
ROYAL_CUBIT = np.pi / 6  # ≈ 0.5236 meters

def draw_regular_polygon(ax, center, side_length, n_sides, color='blue', label_prefix=''):
    """Draw a regular n-sided polygon with given side length."""
    angles = np.linspace(0, 2 * np.pi, n_sides + 1)[:-1]
    x = center[0] + side_length * np.cos(angles)
    y = center[1] + side_length * np.sin(angles)
    ax.plot(np.append(x, x[0]), np.append(y, y[0]), color=color, lw=2, label=f'{label_prefix} sides')

    # Label vertices
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.text(xi, yi, f'V{i+1}', fontsize=12, ha='center', va='center', color=color)

    return x, y

# Create figure for the hexagon
fig, ax = plt.subplots(figsize=(6, 6))

# Draw Hexagon
x_hex, y_hex = draw_regular_polygon(ax, (0, 0), ROYAL_CUBIT, 6, color='blue', label_prefix='Hexagon')

# Annotate side length and angles
ax.text(0, ROYAL_CUBIT * 1.1, r'$s = r = \pi/6$', fontsize=12, ha='center', va='center', color='red')
ax.text(ROYAL_CUBIT * np.cos(np.pi/6), ROYAL_CUBIT * np.sin(np.pi/6) + 0.05, r'$60^\circ = \pi/3$', fontsize=12, ha='center', va='center', color='red')
ax.text(ROYAL_CUBIT * np.cos(np.pi/3) - 0.1, ROYAL_CUBIT * np.sin(np.pi/3) - 0.1, r'$120^\circ$', fontsize=12, ha='center', va='center', color='red')

# Set plot limits and aspect
ax.set_xlim(-1, 1)
ax.set_ylim(-0.5, 1)
ax.set_aspect('equal')

# Remove axes for a cleaner look
ax.axis('off')

# Add title
ax.set_title(r'Perfect integration of hexagonal geometry in the $\pi/6$ system', fontsize=14)

# Save figure
fig.savefig('fig_hexagon_geometry.pdf', dpi=300, bbox_inches='tight')

plt.show()
