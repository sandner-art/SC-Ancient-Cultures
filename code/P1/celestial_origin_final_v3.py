import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif'] # Using Times for closer match to original
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 14 # Adjusted sizes for new layout
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['figure.titlesize'] = 18

# --- Create Figure with a wider, more balanced layout ---
# Increased width to make subplot cells closer to square
fig = plt.figure(figsize=(24, 8))
fig.suptitle(r'The Proto-Spherical Framework: From Celestial Observation to Metrology', y=0.98)


# --- Panel 1: The Observed Cosmos ---
ax1 = fig.add_subplot(131, projection='3d')
# Titles are now placed manually using fig.text for better control
fig.text(0.18, 0.85, '1. The Observed Cosmos\n(Unified Celestial Sphere)', ha='center', va='center', fontsize=14)

# Draw a semi-transparent sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
ax1.plot_surface(x, y, z, color='black', rstride=10, cstride=10, alpha=0.05, lw=0)

# Draw key wireframes
ax1.plot_wireframe(x, y, z, color='gray', rstride=10, cstride=10, alpha=0.2, lw=1)
ax1.plot(np.cos(u), np.sin(u), 0, color='blue', lw=1.5, alpha=0.7) # Equator
ax1.text(0, 0, 1.1, 'Celestial Sphere', ha='center', va='center', fontsize=10)

# Add Circumpolar ("Eternal") Stars
pole_angle = np.linspace(0, 2*np.pi, 5)
ax1.plot(0.2*np.cos(pole_angle), 0.2*np.sin(pole_angle), 0.98, 'k*', markersize=5)
ax1.text(0, 0, 0.9, 'Eternal Stars', ha='center', va='center', fontsize=10)

# Add the Sun on the equator, matching the reference image
ax1.plot([-1.01], [0], [0], 'o', color='gold', markersize=15, markeredgecolor='black')
ax1.text(-1.15, 0, 0.15, 'Sun', ha='center', fontsize=10)

# Draw the 12 hour divisions on the equator
for i in range(12):
    angle = i * np.pi / 6
    ax1.plot([0, np.cos(angle)], [0, np.sin(angle)], [0, 0], color='black', linestyle=':', lw=1, alpha=0.5)

# Adjust view to match reference
ax1.view_init(elev=15, azim=-70)
ax1.axis('off')
# --- KEY CORRECTION: Force the 3D box to have a 1:1:1 aspect ratio ---
ax1.set_box_aspect((1, 1, 1))


# --- Panel 2: The Geometric Principle ---
ax2 = fig.add_subplot(132, projection='3d')
fig.text(0.5, 0.85, '2. The Geometric Principle:\nIsolating the 1-Hour Geodesic', ha='center', va='center', fontsize=14)

# Re-use sphere data
ax2.plot_wireframe(x, y, z, color='gray', rstride=10, cstride=10, alpha=0.2, lw=1)

# Isolate the 30-degree arc
arc_angle = np.pi / 6
phi = np.linspace(0, arc_angle, 50)
x_arc, y_arc, z_arc = np.cos(phi), np.sin(phi), np.zeros_like(phi)
ax2.plot(x_arc, y_arc, z_arc, color='red', lw=4)
ax2.text(0.8, 0.6, 0, r'$L_{arc}$', color='red', fontsize=16, style='italic')

# Trace the spherical triangle geometry
ax2.plot([0, x_arc[0]], [0, y_arc[0]], [0, z_arc[0]], 'k--', lw=1.5)
ax2.plot([0, x_arc[-1]], [0, y_arc[-1]], [0, z_arc[-1]], 'k--', lw=1.5)
ax2.text(0.4, 0.05, 0, 'R', color='black', fontsize=16, style='italic')
ax2.text(0.45, 0.2, 0, r'$30^\circ$', color='purple', fontsize=16)

# Match view angle and turn off axis
ax2.view_init(elev=15, azim=-70)
ax2.axis('off')
# --- KEY CORRECTION: Force the 3D box to have a 1:1:1 aspect ratio ---
ax2.set_box_aspect((1, 1, 1))


# --- Panel 3: The Metrological Instrument ---
ax3 = fig.add_subplot(133)
fig.text(0.83, 0.85, '3. The Metrological Result:\nA Dual-Scale Instrument', ha='center', va='center', fontsize=14)
ax3.set_ylim(0, 10)
ax3.set_xlim(0, 30)

# Hide all spines and y-axis ticks/labels, keep top spine for scales
ax3.spines[['bottom', 'left', 'right']].set_visible(False)
ax3.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

# Configure the primary (top) axis for Degrees
ax3.xaxis.set_ticks_position('top')
ax3.xaxis.set_label_position('top')
ax3.set_xlabel('Degrees of Arc', labelpad=5)
ax3.set_xticks([0, 10, 20, 30])

# Create a secondary axis for Nocturnal Hours, offset above the first
ax_hr = ax3.secondary_xaxis('top', functions=(lambda x: x / 30.0, lambda x: x * 30.0))
ax_hr.spines['top'].set_position(('outward', 40)) # Offset this axis
ax_hr.set_xlabel('Nocturnal Hours', labelpad=5)
ax_hr.set_xticks([0, 0.5, 1.0])

# Draw the cubit rod
rod_y = 4.5
rod_h = 1.5
ax3.add_patch(plt.Rectangle((0, rod_y), 30, rod_h, edgecolor='black', facecolor='#8B4513', lw=2))

# Subdivisions: 7 Palms, 28 Fingers
for i in range(1, 28):
    x_pos = (i / 28.0) * 30.0
    if i % 4 == 0: # Palm division
        ax3.plot([x_pos, x_pos], [rod_y, rod_y + rod_h], 'k-', lw=1.5)
    else: # Finger division
        ax3.plot([x_pos, x_pos], [rod_y, rod_y + rod_h * 0.5], 'k-', lw=0.5)

ax3.text(15, 3.5, '7 Palms / 28 Fingers', ha='center', fontsize=12)


# --- Add Connecting Arrows between panels ---
fig.text(0.335, 0.5, r'$\Longrightarrow$', fontsize=40, ha='center', va='center', color='gray')
fig.text(0.665, 0.5, r'$\Longrightarrow$', fontsize=40, ha='center', va='center', color='gray')

# Use tight_layout and adjust rect to prevent titles from overlapping
plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.show()