import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['figure.titlesize'] = 20

# --- Create Figure with 3D Axes ---
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')
ax.set_title(r'The Proto-Spherical Framework: From Celestial Observation to Metrology', y=0.95)

# --- 1. Draw the Celestial Sphere ---
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_wireframe(x, y, z, color='gray', rstride=10, cstride=10, alpha=0.3, lw=1)
ax.text(0, 0, 1.3, 'The Celestial Sphere', ha='center', fontsize=14)

# --- 2. Draw the 30-degree Astronomical Arc ---
# This arc represents 1 hour of celestial rotation
arc_angle = np.pi / 6  # 30 degrees
phi = np.linspace(0, arc_angle, 50)
# An arc along the equator (theta = pi/2)
x_arc = np.cos(phi)
y_arc = np.sin(phi)
z_arc = np.zeros_like(phi)
ax.plot(x_arc, y_arc, z_arc, color='red', lw=4, label='1 Hour of Sky Rotation')

# Annotate the arc
ax.text(x_arc[25], y_arc[25] + 0.1, z_arc[25], r'$30^\circ = \pi/6$ rad', color='red', fontsize=16)

# --- 3. "Unroll" the Arc into a Linear Standard ---
# This is a conceptual representation
# Draw the linear cubit rod outside the 3D plot
# We use a secondary 2D axes overlayed for clarity
ax2 = fig.add_axes([0.6, 0.25, 0.3, 0.1])
ax2.plot([0, 1], [0.5, 0.5], color='purple', lw=5)
ax2.text(0.5, 0.65, r'Standardized Linear Unit:' '\n' r'\textbf{1 Royal Cubit ($\pi/6$ m)}',
         ha='center', va='bottom', fontsize=14, color='purple')
ax2.axis('off')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)

# Draw an arrow from the 3D arc to the 2D rod
# This requires converting 3D data coords to 2D display coords
x_arrow_start, y_arrow_start, _ = proj3d.proj_transform(x_arc[-1], y_arc[-1], z_arc[-1], ax.get_proj())
x_arrow_start = x_arrow_start.item()
y_arrow_start = y_arrow_start.item()

# Arrow pointing from the 3D arc to the 2D subplot
arrow = FancyArrowPatch(
    (x_arrow_start, y_arrow_start),
    (0.75, 0.35),
    transform=fig.transFigure,
    connectionstyle="arc3,rad=-0.3",
    color="black",
    arrowstyle="->,head_length=10,head_width=6",
    lw=2
)
fig.add_artist(arrow)
fig.text(0.55, 0.4, 'Conceptual Unrolling\n& Standardization', ha='center', fontsize=12, style='italic')


# --- Final Plot Adjustments ---
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1,1,1]) # Equal aspect ratio
ax.view_init(elev=20, azim=30) # Good viewing angle
ax.axis('off')
ax.legend(loc='upper left')

plt.show()