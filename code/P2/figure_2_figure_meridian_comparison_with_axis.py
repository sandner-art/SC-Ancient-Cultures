import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 14

# --- Figure and Axis Setup for a 1x2 panel figure ---
fig, axs = plt.subplots(1, 2, figsize=(16, 8.5))
fig.suptitle("Two Methods for Determining the North-South Meridian", fontsize=18, weight='bold')

# =============================================================================
# Panel (a): Shortest Shadow Method
# =============================================================================
ax1 = axs[0]
ax1.set_aspect('equal')
ax1.set_title("(a) The 'Shortest Shadow' Method", fontsize=16)
ax1.axis('off')

# --- Plot elements for Panel (a) ---
# Shadow path (approximated as a parabola)
x_a = np.linspace(-2, 2, 400)
y_a = 0.5 * x_a**2 + 1.5
p1, = ax1.plot(x_a, y_a, color='#CC3311', linewidth=2.5, label="Path of Shadow Tip")

# Gnomon base at (0,0)
p2, = ax1.plot(0, 0, 'ko', markersize=12, label='Gnomon Base', zorder=10) # Higher zorder

# Shortest shadow at local noon
noon_x, noon_y = 0, 1.5
p3, = ax1.plot([0, noon_x], [0, noon_y], 'b--', dashes=(5, 5), linewidth=2, label='Shortest Shadow (Local Noon)')

# Meridian Line (made consistent with panel b)
p4, = ax1.plot([0, 0], [-1, 4.5], 'r-', linewidth=2.5, zorder=0, label='North-South Meridian')

# --- ADDED: East-West directional line as requested ---
ax1.axhline(0, color='gray', linestyle=':', xmin=0.15, xmax=0.85, zorder=0)
ax1.text(3.5, 0, 'East', ha='center', va='center', fontsize=12, color='gray')
ax1.text(-3.5, 0, 'West', ha='center', va='center', fontsize=12, color='gray')
# --------------------------------------------------------

# Time point annotations
times_x = [-1.8, -1.0, 1.0, 1.8]
times_y = [0.5 * t**2 + 1.5 for t in times_x]
labels_a = ['10 AM', '11 AM', '1 PM', '2 PM']
ax1.scatter(times_x, times_y, c='black', s=40, zorder=5)
for i, label in enumerate(labels_a):
    ax1.text(times_x[i], times_y[i] + 0.2, label, ha='center', va='bottom', fontsize=12)
ax1.text(noon_x, noon_y + 0.2, '12 PM', ha='center', va='bottom', fontsize=12, weight='bold')

# Set consistent limits
ax1.set_xlim(-4, 4)
ax1.set_ylim(-1, 4.5)


# =============================================================================
# Panel (b): Method of Equal Altitudes
# =============================================================================
ax2 = axs[1]
ax2.set_aspect('equal')
ax2.set_title("(b) The 'Method of Equal Altitudes'", fontsize=16)
ax2.axis('off')

# --- Plot elements for Panel (b) ---
# Gnomon and Shadow Path
gnomon_base = (0, 0)
x_b = np.linspace(-2.5, 2.5, 400)
y_b = 0.3 * x_b**2 + 1.5
ax2.plot(x_b, y_b, color='#CC3311', linewidth=2.5) # No label needed, will be shared
ax2.plot(*gnomon_base, 'ko', markersize=12) # No label needed

# Define intersection points
x_am = -1.5
y_am = 0.3 * x_am**2 + 1.5
x_pm = 1.5
y_pm = 0.3 * x_pm**2 + 1.5

# Calculate required radius for the reference circle to pass through the points
ref_radius = np.sqrt(x_pm**2 + y_pm**2)
p5 = patches.Circle(gnomon_base, ref_radius, facecolor='none', edgecolor='gray', linestyle='--', linewidth=1.5, label='Reference Circle')
ax2.add_patch(p5)

# Mark Crossover Points
p6 = ax2.scatter([x_am, x_pm], [y_am, y_pm], c='blue', s=100, zorder=5, label='Crossover Points')
ax2.text(x_am - 0.2, y_am, 'AM', ha='right', va='center', fontsize=12, color='blue')
ax2.text(x_pm + 0.2, y_pm, 'PM', ha='left', va='center', fontsize=12, color='blue')

# Lines and Angle Bisector (Meridian)
ax2.plot([0, x_am], [0, y_am], 'k:', zorder=1)
ax2.plot([0, x_pm], [0, y_pm], 'k:', zorder=1)
ax2.plot([0, 0], [-1, 4.5], 'r-', linewidth=2.5, zorder=0) # No label needed

# Annotation
ax2.annotate('Angle Bisector Yields\nPrecise Meridian Line', xy=(0, 2.8), xytext=(-2.5, 3.8),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6, connectionstyle="arc3,rad=0.2"),
            ha='center', va='center', fontsize=14, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=1))

# Set consistent limits
ax2.set_xlim(-4, 4)
ax2.set_ylim(-1, 4.5)

# =============================================================================
# Combined Legend and Final Touches
# =============================================================================
# Manually define handles and labels for a clean, ordered legend
handles = [p1, p2, p4, p3, p5, p6]
labels = [h.get_label() for h in handles]
fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 0.01), ncol=3, fontsize=14)

# Adjust layout to prevent title/legend overlap
fig.tight_layout(rect=[0, 0.08, 1, 0.95])

plt.savefig("figure_meridian_comparison_with_axis.png", dpi=300)
plt.show()