import matplotlib.pyplot as plt
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(8, 7))
ax.set_aspect('equal')

# --- Create the shadow path (a hyperbola) ---
# We can approximate with a parabola for simplicity
x = np.linspace(-2, 2, 400)
y = 0.5 * x**2 + 1.5 # y is the distance from gnomon base

# Plot the shadow path
ax.plot(x, y, color='#CC3311', linewidth=2, label="Path of Gnomon's Shadow Tip")

# Gnomon base at (0,0)
ax.plot(0, 0, 'ko', markersize=10, label='Gnomon Base')

# --- Find and mark the shortest shadow ---
noon_x, noon_y = 0, 1.5
ax.plot([0, noon_x], [0, noon_y], 'b--', dashes=(5, 5), linewidth=1.5, label='Shortest Shadow (Local Noon)')

# --- Mark time points on the curve ---
times_x = [-1.8, -1.0, 1.0, 1.8]
times_y = [0.5 * t**2 + 1.5 for t in times_x]
labels = ['10 AM', '11 AM', '1 PM', '2 PM']
ax.scatter(times_x, times_y, c='black', s=30, zorder=5)
for i, label in enumerate(labels):
    ax.text(times_x[i], times_y[i] + 0.15, label, ha='center', va='bottom', fontsize=10)
ax.text(noon_x, noon_y + 0.15, '12 PM', ha='center', va='bottom', fontsize=10, weight='bold')


# --- Draw the North-South Meridian ---
ax.axhline(0, color='gray', linestyle=':', xmin=0.1, xmax=0.9, zorder=0)
ax.axvline(0, color='gray', linestyle=':', ymin=0, ymax=0.4, zorder=0)
ax.annotate('North-South Meridian', xy=(0, 0), xytext=(0, -0.5),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0", color='gray'),
            ha='center', va='top', fontsize=10, color='gray')
ax.text(2.5, 0, 'East', ha='center', va='center', fontsize=10, color='gray')
ax.text(-2.5, 0, 'West', ha='center', va='center', fontsize=10, color='gray')

# --- Final Touches ---
ax.set_xlim(-3, 3)
ax.set_ylim(-0.8, 4)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc='upper right')
ax.set_title("Determining Local Noon via the 'Shortest Shadow' Method", fontsize=14, weight='bold')

plt.tight_layout()
plt.savefig("figure_4_shortest_shadow.png", dpi=300)
plt.show()