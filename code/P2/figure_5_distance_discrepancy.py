import matplotlib.pyplot as plt
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_aspect('equal')
ax.axis('off')

# --- Stylized Map Elements ---
# City positions
alexandria = (0.5, 8.5)
syene = (1.0, 1.0)

# Mediterranean Sea
ax.fill_between([-1, 2], [9, 9], 10, color='lightblue', alpha=0.5)
ax.text(0.5, 9.5, 'Mediterranean Sea', ha='center', style='italic', color='navy')

# Draw cities
ax.plot(alexandria[0], alexandria[1], 'ko', markersize=10)
ax.text(alexandria[0] + 0.1, alexandria[1], 'Alexandria', va='center', ha='left', weight='bold')
ax.plot(syene[0], syene[1], 'ko', markersize=10)
ax.text(syene[0] + 0.1, syene[1], 'Syene (Aswan)', va='center', ha='left', weight='bold')

# --- Draw the two distance paths ---
# 1. Geometric North-South Distance (Meridian)
ax.plot([alexandria[0], syene[0]], [alexandria[1], syene[1]], 'r--', dashes=(6, 4), 
        linewidth=2, label='Geometric Distance (~788 km)')
        
# 2. Winding Nile Travel Distance
# Create a curvy path for the Nile
n_points = 100
x_nile = np.linspace(syene[0], alexandria[0], n_points)
y_nile = np.linspace(syene[1], alexandria[1], n_points)
# Add sinusoidal wiggle
x_wiggle = 0.5 * np.sin(np.linspace(0, 4 * np.pi, n_points))
ax.plot(x_nile + x_wiggle, y_nile, color='#0066CC', linewidth=2.5, 
        solid_capstyle='round', label='Travel Distance along Nile (~925 km)')

# --- Annotations and Hypotheses ---
# Annotate Geometric Distance
ax.annotate('Hypothesis A: Geometric Distance\n$d = 5000$ Egyptian Stadia\n(157.6 m/stadion)',
            xy=(0.75, 5.0), xytext=(2.0, 5.0),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6, connectionstyle="arc3,rad=-0.2"),
            ha='left', va='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=1, alpha=0.8))

# Annotate Travel Distance
ax.annotate('Hypothesis B: Travel Distance\n$d = 5000$ Attic Stadia\n(185 m/stadion)',
            xy=(1.4, 3.0), xytext=(2.0, 3.0),
            arrowprops=dict(facecolor='#0066CC', shrink=0.05, width=1, headwidth=6, connectionstyle="arc3,rad=-0.2"),
            ha='left', va='center', fontsize=11, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#0066CC", lw=1, alpha=0.8))

# --- Final Touches ---
ax.set_xlim(-1, 4)
ax.set_ylim(0, 11)
ax.set_title("Interpreting the Distance 'd': Key to the Result", fontsize=16, weight='bold', pad=20)
legend = ax.legend(loc='lower right', bbox_to_anchor=(1.05, -0.05), frameon=True, shadow=True)
legend.get_frame().set_edgecolor('k')

plt.tight_layout()
plt.savefig("figure_5_distance_discrepancy.png", dpi=300)
plt.show()