import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup (1 row, 2 columns) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("Impact of Stellar Distance on Sun's Rays", fontsize=16, weight='bold')

# --- SUBPLOT 1: Close Star (Diverging Rays) ---
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title('Close Star: Diverging Rays (Parallax)', fontsize=14)

# Planet and Star
planet1 = patches.Circle((0, 0), 1.0, facecolor='#cce6ff', edgecolor='black', zorder=2)
star1 = patches.Circle((-4, 0), 0.5, facecolor='gold', edgecolor='orange', zorder=1)
ax1.add_patch(planet1)
ax1.add_patch(star1)

# Observation points on the planet
point_a = (np.cos(np.pi/4), np.sin(np.pi/4))
point_b = (np.cos(-np.pi/4), np.sin(-np.pi/4))

# Draw diverging rays from star's center
ax1.plot([-4, point_a[0]], [0, point_a[1]], 'r--', dashes=(5, 5))
ax1.plot([-4, point_b[0]], [0, point_b[1]], 'r--', dashes=(5, 5))
ax1.text(-2.5, 1.0, 'Rays are not parallel', ha='center', style='italic', color='red')

# Draw gnomons
ax1.plot([point_a[0], point_a[0]*1.2], [point_a[1], point_a[1]*1.2], 'b-')
ax1.plot([point_b[0], point_b[0]*1.2], [point_b[1], point_b[1]*1.2], 'b-')
ax1.set_xlim(-5, 1.5)
ax1.set_ylim(-2, 2)

# --- SUBPLOT 2: Distant Star (Parallel Rays) ---
ax2.set_aspect('equal')
ax2.axis('off')
ax2.set_title('Distant Star: Parallel Rays (No Parallax)', fontsize=14)

# Planet
planet2 = patches.Circle((0, 0), 1.0, facecolor='#cce6ff', edgecolor='black', zorder=2)
ax2.add_patch(planet2)

# Draw parallel rays
for y_pos in np.linspace(-0.8, 0.8, 5):
    ax2.arrow(-2.5, y_pos, 2, 0, head_width=0.06, head_length=0.1, fc='gold', ec='orange', zorder=1)

ax2.text(-1.5, 1.0, 'Rays are effectively parallel', ha='center', style='italic')
ax2.set_xlim(-2.5, 1.5)
ax2.set_ylim(-2, 2)

# --- Final Touches ---
plt.tight_layout(rect=[0, 0, 1, 0.95]) # Adjust layout to make room for suptitle
plt.savefig("figure_3_parallax_comparison.png", dpi=300)
plt.show()