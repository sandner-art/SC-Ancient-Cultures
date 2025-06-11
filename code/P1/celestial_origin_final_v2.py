import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['figure.titlesize'] = 20

# --- Create Figure with 3 Subplots ---
fig = plt.figure(figsize=(18, 7))
fig.suptitle(r'The Proto-Spherical Framework: From Celestial Observation to Metrology', y=1.0)

# --- Panel 1: The Astronomical Observation ---
ax1 = fig.add_subplot(131, projection='3d')
ax1.set_title('1. The Observed Reality:\n12 Hours of Celestial Rotation', pad=20)

# Draw the sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
ax1.plot_wireframe(x, y, z, color='gray', rstride=10, cstride=10, alpha=0.3, lw=1)

# Draw the 12 hour divisions on the equator
for i in range(12):
    angle = i * np.pi / 6
    ax1.plot([0, np.cos(angle)], [0, np.sin(angle)], [0, 0], color='black', linestyle=':', lw=1)
ax1.plot(np.cos(u), np.sin(u), 0, color='blue', lw=1.5) # Equator
ax1.text(0, 0, 1.3, 'Celestial Sphere', ha='center', fontsize=12)
ax1.view_init(elev=35, azim=45)
ax1.axis('off')

# --- Panel 2: The Geometric Principle ---
ax2 = fig.add_subplot(132, projection='3d')
ax2.set_title('2. The Geometric Principle:\nIsolating the 30° Geodesic', pad=20)
ax2.plot_wireframe(x, y, z, color='gray', rstride=10, cstride=10, alpha=0.3, lw=1)

# Isolate the 30-degree arc (geodesic)
arc_angle = np.pi / 6
phi = np.linspace(0, arc_angle, 50)
x_arc, y_arc, z_arc = np.cos(phi), np.sin(phi), np.zeros_like(phi)
ax2.plot(x_arc, y_arc, z_arc, color='red', lw=4, label='1 Hour Arc')
ax2.text(0.8, 0.6, 0, r'$L_{arc}$', color='red', fontsize=16, style='italic')

# Trace the spherical triangle geometry
ax2.plot([0, x_arc[0]], [0, y_arc[0]], [0, z_arc[0]], 'k--', lw=1.5)
ax2.plot([0, x_arc[-1]], [0, y_arc[-1]], [0, z_arc[-1]], 'k--', lw=1.5)
ax2.text(0.4, 0, 0, 'R', color='black', fontsize=16, style='italic')
ax2.text(0.4, 0.2, 0, r'$30^\circ$', color='purple', fontsize=16)
ax2.view_init(elev=35, azim=45)
ax2.axis('off')

# --- Panel 3: The Metrological Result ---
ax3 = fig.add_subplot(133)
ax3.set_title('3. The Metrological Result:\nThe Royal Cubit Standard', pad=20)
# Draw the cubit rod
rod_length = 0.8
ax3.add_patch(plt.Rectangle((0.1, 0.45), rod_length, 0.1, edgecolor='black', facecolor='#DEB887', lw=2))
# Add divisions
for i in range(1, 7):
    ax3.plot([0.1 + i*rod_length/7, 0.1 + i*rod_length/7], [0.45, 0.55], 'k-')
ax3.text(0.5, 0.25, r'Standardized Length:' '\n' r'$L_{rod} = L_{arc}$' '\n' r'$\mathbf{1 \, Royal \, Cubit = \pi/6 \, m}$',
         ha='center', va='center', fontsize=14, color='purple', bbox=dict(fc='white', ec='purple'))
ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.axis('off')

# --- Add Connecting Arrows between panels ---
fig.text(0.34, 0.5, r'$\Rightarrow$', fontsize=30, ha='center', va='center')
fig.text(0.67, 0.5, r'$\Rightarrow$', fontsize=30, ha='center', va='center')

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()