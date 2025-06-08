import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, PathPatch, Ellipse  # Added Ellipse import
from matplotlib.path import Path

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['figure.titlesize'] = 18

# --- Create Figure with 2x2 Grid ---
fig, axs = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle(r'The Unified Dimensional Framework Derived from the Royal Cubit ($L = \pi/6$)', y=0.98)


# --- 1. Quadrant: Areal (2D) ---
ax = axs[0, 0]
ax.set_title('Areal (2D)')
side = 0.8
ax.add_patch(plt.Rectangle((0.1, 0.1), side, side, edgecolor='black', facecolor='lightblue', alpha=0.6))
ax.text(0.1 + side/2, 0.1 - 0.05, 'L', ha='center', va='top', fontsize=14)
ax.text(0.1 - 0.05, 0.1 + side/2, 'L', ha='right', va='center', fontsize=14)
ax.text(0.5, 1.1, r'$A = L^2 \approx 0.274 \, m^2$',
        ha='center', va='center', fontsize=12, bbox=dict(fc='white'))
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# --- 2. Quadrant: Cubic (3D) ---
ax = axs[0, 1]
ax.set_title('Cubic (3D)')
# Draw an isometric cube
v = np.array([[0,0],[1,0],[1,1],[0,1],[0.5,0.5],[1.5,0.5],[1.5,1.5],[0.5,1.5]])
v = v - v.mean(axis=0)
edges = [[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]]
for edge in edges:
    ax.plot(v[edge,0], v[edge,1], 'k-')
ax.text(0, 0.8, r'$V_{cube} = L^3 \approx 143.6 \, L$', ha='center', fontsize=12, bbox=dict(fc='white'))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axis('off')

# --- 3. Quadrant: Spherical (3D) ---
ax = axs[1, 0]
ax.set_title('Spherical (3D)')
ax.add_patch(plt.Circle((0.5, 0.5), 0.4, color='lightcoral', alpha=0.6))
# Fixed: Use Ellipse from patches, not plt.Ellipse
ax.add_patch(Ellipse((0.5, 0.5), 0.8, 0.2, fill=False, edgecolor='black', lw=1.5))
ax.text(0.5, 1.1, 'From Circumference $c=L$', ha='center', fontsize=12)
ax.text(0.5, 0.0, r'$V_{sphere} = \frac{c^3}{6\pi^2} \approx 2.424 \, L \, (\frac{1}{2} \, hekat)$',
        ha='center', va='center', fontsize=12, bbox=dict(fc='white'))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# --- 4. Quadrant: The Scaling Factor ---
ax = axs[1, 1]
ax.set_title('The System\'s Internal Ratio')
# Simple balance scale icon
ax.plot([0.2, 0.8], [0.8, 0.8], 'black', lw=1) # Beam holder
ax.plot([0.5], [0.8], 'k^', markersize=15) # Fulcrum
# Pans
ax.plot([0.2, 0.2], [0.8, 0.7], 'k-')
ax.plot([0.8, 0.8], [0.8, 0.9], 'k-')
# Tilted beam
ax.plot([0.1, 0.9], [0.65, 0.95], 'gray', lw=4, alpha=0.8)
ax.text(0.15, 0.5, 'Sphere', ha='center')
ax.text(0.85, 0.5, 'Cube', ha='center')

ax.text(0.5, 0.25, r'$\frac{V_{sphere}}{V_{cube}} = \frac{1}{6\pi^2} \approx \frac{1}{59.2}$',
        ha='center', va='center', fontsize=16, bbox=dict(fc='white'))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# --- Central "Source" Text and Arrows ---
fig.text(0.5, 0.5, r'Source:' '\n' r'\textbf{1D Linear Cubit}' '\n' r'$L = \pi/6 \, m$',
         ha='center', va='center', fontsize=16, bbox=dict(boxstyle="circle,pad=0.5", fc="yellow", alpha=0.8))

# Arrows from center to quadrants
def draw_arrow(ax_fig, ax_quad):
    center_coords = ax_fig.transFigure.inverted().transform(ax_fig.transFigure.transform((0.5,0.5)))
    quad_coords = ax_fig.transFigure.inverted().transform(ax_quad.transAxes.transform((0.5,0.5)))
    arrow = FancyArrowPatch(center_coords, quad_coords, transform=ax_fig.transFigure,
                            connectionstyle="arc3,rad=0.2", color="black",
                            arrowstyle="-|>", mutation_scale=25, lw=2, alpha=0.7)
    ax_fig.add_artist(arrow)

draw_arrow(fig, axs[0,0])
draw_arrow(fig, axs[0,1])
draw_arrow(fig, axs[1,0])
draw_arrow(fig, axs[1,1])

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()