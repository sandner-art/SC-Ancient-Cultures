import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')

# --- Gnomon and Reference Circle ---
gnomon_base = (0, 0)
ref_radius = 2.0
reference_circle = patches.Circle(gnomon_base, ref_radius, facecolor='none', edgecolor='gray', linestyle='--', label='Reference Circle')
ax.add_patch(reference_circle)
ax.plot(*gnomon_base, 'ko', markersize=10, label='Gnomon Base')

# --- Shadow Path ---
x_shadow = np.linspace(-2.5, 2.5, 400)
y_shadow = 0.3 * x_shadow**2 + 1.5
ax.plot(x_shadow, y_shadow, color='#CC3311', linewidth=2, label="Path of Shadow Tip")

# --- Find and Mark Intersections ---
# Calculate intersection points programmatically
# y_shadow = 0.3*x^2 + 1.5  AND  x^2 + y^2 = ref_radius^2
# For this visualization, we can just define them
x_am = -1.5
y_am = 0.3 * x_am**2 + 1.5
x_pm = 1.5
y_pm = 0.3 * x_pm**2 + 1.5

ax.scatter([x_am, x_pm], [y_am, y_pm], c='blue', s=80, zorder=5, label='Crossover Points')
ax.text(x_am - 0.2, y_am, 'AM', ha='right', va='center', fontsize=11, color='blue')
ax.text(x_pm + 0.2, y_pm, 'PM', ha='left', va='center', fontsize=11, color='blue')

# --- Draw Lines and Angle Bisector ---
# Lines from base to crossover points
ax.plot([0, x_am], [0, y_am], 'k:', zorder=1)
ax.plot([0, x_pm], [0, y_pm], 'k:', zorder=1)

# Angle Bisector (the meridian)
ax.plot([0, 0], [0, 4], 'r-', linewidth=2, zorder=4, label='North-South Meridian')

# --- Annotations ---
ax.annotate('Angle Bisector Yields\nPrecise Meridian Line', xy=(0, 2.5), xytext=(-2.5, 3.5),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6),
            ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="ivory", ec="red", lw=1))

# --- Final Touches ---
ax.set_xlim(-4, 4)
ax.set_ylim(-1, 4.5)
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=3)
ax.set_title("Determining the Meridian via the 'Method of Equal Altitudes'", fontsize=14, weight='bold', pad=20)
plt.tight_layout()
plt.savefig("figure_10_equal_altitudes.png", dpi=300)
plt.show()