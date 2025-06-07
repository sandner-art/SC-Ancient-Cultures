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

    # Draw circumcircle
    circle = plt.Circle(center, side_length, color=color, fill=False, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)

    # Label vertices
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.text(xi, yi, f'V{i+1}', fontsize=12, ha='center', va='center', color=color, bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

    return x, y

# Create figure with two panels
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel 1: Pentagon
x_pent, y_pent = draw_regular_polygon(ax1, (0, 0), ROYAL_CUBIT, 5, color='blue', label_prefix='Pentagon')
ax1.set_title('Pentagon with Circumcircle', fontsize=16, pad=20)
ax1.set_xlabel('x (m)', fontsize=12)
ax1.set_ylabel('y (m)', fontsize=12)
ax1.text(0, ROYAL_CUBIT * 1.15, r'Circumradius = $\pi/6$', fontsize=12, ha='center', va='center', color='blue')
ax1.text(0, 0, 'Center', fontsize=12, ha='center', va='center', color='red', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
ax1.set_aspect('equal')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='upper right', fontsize=10)

# Panel 2: Hexagon
x_hex, y_hex = draw_regular_polygon(ax2, (0, 0), ROYAL_CUBIT, 6, color='green', label_prefix='Hexagon')

# Annotate internal angles
for i in range(6):
    angle = np.pi / 3  # Internal angle of a regular hexagon
    ax2.text(0, 0.05, f'{np.degrees(angle):.0f}$^\circ$ = $\pi/3$', fontsize=12, ha='center', va='center', color='purple')

ax2.set_title('Hexagon with Circumcircle', fontsize=16, pad=20)
ax2.set_xlabel('x (m)', fontsize=12)
ax2.set_ylabel('y (m)', fontsize=12)
ax2.text(0, ROYAL_CUBIT * 1.15, r'Circumradius = $\pi/6$', fontsize=12, ha='center', va='center', color='green')
ax2.text(0, 0, 'Center', fontsize=12, ha='center', va='center', color='red', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
ax2.set_aspect('equal')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout
plt.tight_layout()

# Save figure
fig.savefig('advanced_geometric_illustration.pdf', dpi=300, bbox_inches='tight')

plt.show()
