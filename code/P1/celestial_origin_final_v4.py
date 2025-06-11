import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- Setup for Consistent, Publication-Quality Fonts to Match Reference ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['figure.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['xtick.labelsize'] = 9

# --- Create a wide figure to accommodate the sparse layout ---
fig = plt.figure(figsize=(22, 9))
fig.suptitle('The Proto-Spherical Framework: From Celestial Observation to Metrology', y=0.95, fontsize=18)

# --- Define sphere data (used by Panel 1 and 2) ---
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sphere = 1 * np.outer(np.cos(u), np.sin(v))
y_sphere = 1 * np.outer(np.sin(u), np.sin(v))
z_sphere = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

# ==============================================================================
# --- Panel 1: The Observed Cosmos (Manual Placement) ---
# ==============================================================================
ax1 = fig.add_axes([0.05, 0.1, 0.3, 0.7], projection='3d')
fig.text(0.2, 0.82, '1. The Observed Cosmos\n(Unified Celestial Sphere)', ha='center', fontsize=12, linespacing=1.5)

# Draw a very light gray sphere surface
ax1.plot_surface(x_sphere, y_sphere, z_sphere, color='#f0f0f0', rstride=5, cstride=5, alpha=1.0)
# Draw a light gray wireframe over it
ax1.plot_wireframe(x_sphere, y_sphere, z_sphere, color='gray', rstride=10, cstride=10, alpha=0.3, lw=1)

# Draw the blue equator
ax1.plot(np.cos(u), np.sin(u), 0, color='blue', lw=1.5, alpha=0.9)

# Draw the dotted radial lines
for i in range(12):
    angle = i * np.pi / 6
    ax1.plot([0, np.cos(angle)], [0, np.sin(angle)], [0, 0], color='black', linestyle=':', lw=1, alpha=0.5)

# Add Circumpolar ("Eternal") Stars near the top pole
ax1.text(0, 0, 1.1, 'Celestial Sphere', ha='center', va='center', fontsize=10)
ax1.plot([0.1, 0.25, -0.05], [0.1, -0.1, -0.2], [0.98, 0.95, 0.96], 'k*', markersize=5)
ax1.text(0, 0, 0.9, 'Eternal Stars', ha='center', va='center', fontsize=10)


# Add the Sun on the far left of the equator
ax1.plot([-1.0], [0], [0], 'o', color='gold', markersize=15, markeredgecolor='black', zorder=10)
ax1.text(-1.3, 0, 0.0, 'Sun', ha='center', fontsize=10)

# Set view angle to match reference (side-on) and turn off axis decorations
ax1.view_init(elev=12, azim=-85)
ax1.axis('off')

# CRITICAL FIX: Ensure the 3D box has a 1:1:1 aspect ratio to prevent squishing
ax1.set_box_aspect((1, 1, 1))
ax1.set_xlim(-1.1, 1.1)
ax1.set_ylim(-1.1, 1.1)
ax1.set_zlim(-1.1, 1.1)


# ==============================================================================
# --- Panel 2: The Geometric Principle (Manual Placement) ---
# ==============================================================================
ax2 = fig.add_axes([0.35, 0.1, 0.3, 0.7], projection='3d')
fig.text(0.5, 0.82, '2. The Geometric Principle:\nIsolating the 1-Hour Geodesic', ha='center', fontsize=12, linespacing=1.5)

# Draw only the wireframe for a sparser look
ax2.plot_wireframe(x_sphere, y_sphere, z_sphere, color='gray', rstride=10, cstride=10, alpha=0.3, lw=1)

# Isolate the 30-degree arc on the equator
arc_angle = np.pi / 6
phi = np.linspace(0, arc_angle, 50)
x_arc, y_arc, z_arc = np.cos(phi), np.sin(phi), np.zeros_like(phi)
ax2.plot(x_arc, y_arc, z_arc, color='red', lw=4, zorder=10)
ax2.text(0.85, 0.55, 0, r'$L_{arc}$', color='red', fontsize=16, style='italic')

# Trace the spherical triangle geometry
ax2.plot([0, x_arc[0]], [0, y_arc[0]], [0, z_arc[0]], 'k--', lw=1.5)
ax2.plot([0, x_arc[-1]], [0, y_arc[-1]], [0, z_arc[-1]], 'k--', lw=1.5)
ax2.text(0.4, 0.05, 0, 'R', color='black', fontsize=16, style='italic')
ax2.text(0.5, 0.25, 0, r'$30^\circ$', color='purple', fontsize=16)

# Match view angle and axis properties from Panel 1
ax2.view_init(elev=12, azim=-85)
ax2.axis('off')
ax2.set_box_aspect((1, 1, 1))
ax2.set_xlim(-1.1, 1.1)
ax2.set_ylim(-1.1, 1.1)
ax2.set_zlim(-1.1, 1.1)


# ==============================================================================
# --- Panel 3: The Metrological Instrument (Manual Placement) ---
# ==============================================================================
ax3 = fig.add_axes([0.67, 0.1, 0.3, 0.7])
fig.text(0.82, 0.82, '3. The Metrological Result:\nA Dual-Scale Instrument', ha='center', fontsize=12, linespacing=1.5)

# Configure the primary axis (bottom of the two) for Degrees
ax3.spines[['left', 'right', 'bottom']].set_visible(False)
ax3.tick_params(left=False, labelleft=False, bottom=False, labelbottom=False)
ax3.spines['top'].set_position(('axes', 0.8)) # Position the axis line
ax3.set_xlim(0, 30)
ax3.set_xticks([0, 10, 20, 30])
ax3.set_xlabel('Degrees of Arc', labelpad=5)
ax3.xaxis.set_label_position('top')
ax3.xaxis.set_ticks_position('top')

# Create a secondary axis for Nocturnal Hours, offset above the first
ax_hr = ax3.secondary_xaxis('top', functions=(lambda x: x / 30.0, lambda x: x * 30.0))
ax_hr.spines['top'].set_position(('outward', 35)) # Further offset this axis
ax_hr.set_xlabel('Nocturnal Hours', labelpad=5)
ax_hr.set_xticks([0.0, 0.5, 1.0])

# Draw the cubit rod
rod_y = 0.55
rod_h = 0.15
ax3.add_patch(plt.Rectangle((0, rod_y), 30, rod_h, edgecolor='black', facecolor='#8B4513', lw=1.5))

# Subdivisions: 7 Palms, 28 Fingers
for i in range(1, 28):
    x_pos = (i / 28.0) * 30.0
    if i % 4 == 0: # Palm division
        ax3.plot([x_pos, x_pos], [rod_y, rod_y + rod_h], 'k-', lw=1.5)
    else: # Finger division
        ax3.plot([x_pos, x_pos], [rod_y, rod_y + rod_h * 0.6], 'k-', lw=0.7)

ax3.text(15, 0.45, '7 Palms / 28 Fingers', ha='center', va='center', fontsize=11)
ax3.set_ylim(0, 1) # Set limits to contain all elements
ax3.patch.set_visible(False) # Make background transparent


# ==============================================================================
# --- Add Connecting Arrows between panels ---
# ==============================================================================
fig.text(0.35, 0.45, r'$\Longrightarrow$', fontsize=40, ha='center', va='center', color='#606060')
fig.text(0.65, 0.45, r'$\Longrightarrow$', fontsize=40, ha='center', va='center', color='#606060')

plt.show()