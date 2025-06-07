import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Set plot style for publication quality
plt.style.use(['science', 'ieee'])

# Royal cubit approximation (π/6 meters)
ROYAL_CUBIT = np.pi / 6  # ≈ 0.5236 meters
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618

def draw_pentagram(ax, center, side_length):
    """Draw a pentagram with given side length."""
    angles = np.linspace(0, 2 * np.pi, 6)[:-1]
    x = center[0] + side_length * np.cos(angles)
    y = center[1] + side_length * np.sin(angles)

    # Draw pentagram
    for i in range(5):
        ax.plot([x[i], x[(i + 2) % 5]], [y[i], y[(i + 2) % 5]], color='blue', lw=2)

    # Draw circumcircle
    circle = plt.Circle(center, side_length, color='blue', fill=False, linestyle='--', linewidth=1.5)
    ax.add_patch(circle)

    # Label vertices
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.text(xi, yi, f'V{i+1}', fontsize=12, ha='center', va='center', color='blue', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))

    return x, y

# Create figure
fig, ax = plt.subplots(figsize=(8, 8))

# Draw Pentagram
x_pent, y_pent = draw_pentagram(ax, (0, 0), ROYAL_CUBIT)

# Annotate important properties
ax.text(0, 0, 'Center', fontsize=12, ha='center', va='center', color='red', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
ax.text(0, ROYAL_CUBIT * 1.15, r'Circumradius = $\pi/6$', fontsize=12, ha='center', va='center', color='blue')

# Set plot properties
ax.set_title('Pentagram with Circumcircle', fontsize=16, pad=20)
ax.set_xlabel('x (m)', fontsize=12)
ax.set_ylabel('y (m)', fontsize=12)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Save figure
fig.savefig('pentagram_illustration.pdf', dpi=300, bbox_inches='tight')

plt.show()
