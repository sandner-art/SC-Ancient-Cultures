import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['figure.titlesize'] = 20

# --- Constants ---
SIDE_LENGTH = np.pi / 6  # Common side length for all polygons

# --- Create Figure ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title(r'Locus of Vertices for Polygons of Common Side Length ($s = \pi/6$ m)', y=1.02)

# --- Calculations ---
n_sides_range = range(3, 13)
colors = plt.cm.viridis(np.linspace(0, 1, len(n_sides_range)))
top_vertex = (0, 0)
second_vertices_x = []
second_vertices_y = []

# --- Draw each polygon's first side ---
for i, n in enumerate(n_sides_range):
    angle_from_vertical = np.pi / n
    # Second vertex coords relative to top vertex at (0,0)
    vx2 = SIDE_LENGTH * np.sin(angle_from_vertical)
    vy2 = -SIDE_LENGTH * np.cos(angle_from_vertical)
    second_vertices_x.append(vx2)
    second_vertices_y.append(vy2)

    # Draw the first side of the polygon
    line, = ax.plot([top_vertex[0], vx2], [top_vertex[1], vy2],
                    color=colors[i], lw=2.5, label=f'n={n}')
    
    # Highlight the special case n=6
    if n == 6:
        line.set_linewidth(4)
        line.set_linestyle('--')
        line.set_color('red')
        ax.annotate(r'\textbf{n=6 (Hexagon)}' '\n' r'Angle = $30^\circ = \pi/6$ rad',
                    xy=(vx2, vy2), xytext=(vx2 + 0.2, vy2),
                    arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
                    ha='center', va='center', fontsize=14, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red"))

# --- Draw the Locus Curve ---
ax.plot(second_vertices_x, second_vertices_y, 'k--', lw=1.5,
        label='Locus of 2nd Vertices', alpha=0.8)
ax.scatter(second_vertices_x, second_vertices_y, c=colors, s=50, zorder=5)


# --- Add General Annotations ---
ax.plot(top_vertex[0], top_vertex[1], 'ko', markersize=10, zorder=10)
ax.text(top_vertex[0], top_vertex[1] + 0.05, 'Common Top Vertex', ha='center', fontsize=14)
ax.text(0.3, -0.6, 'Each line segment shown\nhas length = 1 royal cubit',
        ha='center', fontsize=12, bbox=dict(fc='white', alpha=0.8))


# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14)
ax.set_ylabel('Meters', fontsize=14)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='lower right')

ax.set_xlim(-0.1, 0.6)
ax.set_ylim(-0.8, 0.2)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()