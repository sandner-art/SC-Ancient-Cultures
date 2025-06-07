import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Set plot style for publication quality
plt.style.use(['science', 'ieee'])

# Royal cubit approximation (π/6 meters)
ROYAL_CUBIT = np.pi / 6  # ≈ 0.5236 meters
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio ≈ 1.618

def draw_regular_polygon(ax, center, side_length, n_sides, color='blue', label_prefix=''):
    """Draw a regular n-sided polygon with given side length."""
    angles = np.linspace(0, 2 * np.pi, n_sides + 1)[:-1]
    x = center[0] + side_length * np.cos(angles)
    y = center[1] + side_length * np.sin(angles)
    ax.plot(np.append(x, x[0]), np.append(y, y[0]), color=color, lw=1.5, label=f'{label_prefix} sides')

    # Label vertices
    for i, (xi, yi) in enumerate(zip(x, y)):
        ax.text(xi, yi, f'V{i+1}', fontsize=8, ha='center', va='center', color=color)

    return x, y

def draw_diagonal(ax, x, y, i, j, color='red', label=''):
    """Draw a diagonal between vertices i and j."""
    ax.plot([x[i], x[j]], [y[i], y[j]], color=color, ls='--', lw=1, label=label)

def draw_arc(ax, center, radius, start_angle, end_angle, label='', color='black'):
    """Draw an arc with angle labels."""
    theta = np.linspace(start_angle, end_angle, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    ax.plot(x, y, color=color, lw=1.5, label=label)
    # Label angle
    mid_angle = (start_angle + end_angle) / 2
    label_x = center[0] + radius * 1.2 * np.cos(mid_angle)
    label_y = center[1] + radius * 1.2 * np.sin(mid_angle)
    ax.text(label_x, label_y, f'{int(np.degrees(end_angle - start_angle))}$^\circ$', fontsize=8, ha='center', va='center')

# Create figure with three panels
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# Panel 1: Pentagon
x_pent, y_pent = draw_regular_polygon(ax1, (0, 0), ROYAL_CUBIT, 5, color='blue', label_prefix='Pentagon')
draw_diagonal(ax1, x_pent, y_pent, 0, 2, color='red', label=rf'Diagonal = $\phi \times {ROYAL_CUBIT:.3f} \approx {PHI * ROYAL_CUBIT:.3f}$ m')
ax1.set_title(r'Pentagon (Side = $\pi/6$ m)')
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
ax1.legend(loc='upper right', fontsize=8)
ax1.set_aspect('equal')
ax1.grid(True, linestyle='--', alpha=0.5)

# Panel 2: Hexagon
x_hex, y_hex = draw_regular_polygon(ax2, (0, 0), ROYAL_CUBIT, 6, color='green', label_prefix='Hexagon')
ax2.text(x_hex[0], y_hex[0] + 0.1, r'60$^\circ$ (central)', fontsize=8, ha='center', va='bottom', color='green')
ax2.text(x_hex[0] + 0.1, y_hex[0] + 0.05, r'120$^\circ$ (interior)', fontsize=8, ha='left', va='center', color='green')
ax2.set_title(r'Hexagon (Side = $\pi/6$ m)')
ax2.set_xlabel('x (m)')
ax2.set_ylabel('y (m)')
ax2.legend(loc='upper right', fontsize=8)
ax2.set_aspect('equal')
ax2.grid(True, linestyle='--', alpha=0.5)

# Panel 3: Angular System
draw_arc(ax3, (0, 0), ROYAL_CUBIT, 0, np.pi/6, label=r'$\pi/6 = 30^\circ$', color='purple')
draw_arc(ax3, (0, 0), ROYAL_CUBIT * 1.5, 0, 2 * np.pi / 6, label=r'$2\pi/6 = 60^\circ$', color='orange')
draw_arc(ax3, (0, 0), ROYAL_CUBIT * 2, 0, 3 * np.pi / 6, label=r'$3\pi/6 = 90^\circ$', color='blue')
draw_arc(ax3, (0, 0), ROYAL_CUBIT * 2.5, 0, 4 * np.pi / 6, label=r'$4\pi/6 = 120^\circ$', color='green')
ax3.plot([0, ROYAL_CUBIT * 3 * np.cos(np.pi)], [0, ROYAL_CUBIT * 3 * np.sin(np.pi)], 'k--', label=r'$6\pi/6 = 180^\circ$')
ax3.plot([0, ROYAL_CUBIT * 3.5], [0, 0], 'k-', label=r'$12\pi/6 = 360^\circ$')
ax3.set_title(r'$\pi/6$ Angular System')
ax3.set_xlabel('x (m)')
ax3.set_ylabel('y (m)')
ax3.legend(loc='upper right', fontsize=8)
ax3.set_aspect('equal')
ax3.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Save figure
fig.savefig('geometric_illustration.pdf', dpi=300)
fig.savefig('geometric_illustration.png', dpi=300)

plt.show()
