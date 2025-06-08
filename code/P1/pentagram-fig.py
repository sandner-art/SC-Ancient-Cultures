import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup for Consistent, Publication-Quality Fonts ---
# Use a serif font that mimics the 'LaTeX' look of the other figures.
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 20

# --- Constants ---
ROYAL_CUBIT = np.pi / 6  # Circumradius R
PHI = (1 + np.sqrt(5)) / 2

# --- Create Figure ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title(r'Pentagram Geometry Quantized by the Royal Cubit (R = $\pi/6$)', y=1.02)

# --- Calculate Vertices ---
# Start angle chosen to place one vertex at the top
angles = np.linspace(0, 2 * np.pi, 6)[:-1] + np.pi/2
x_verts = ROYAL_CUBIT * np.cos(angles)
y_verts = ROYAL_CUBIT * np.sin(angles)

# --- Draw Enclosing Pentagon ---
ax.plot(np.append(x_verts, x_verts[0]), np.append(y_verts, y_verts[0]),
        color='black', linestyle='--', lw=1, alpha=0.7, label='Enclosing Pentagon')

# --- Draw Pentagram Diagonals ---
# Connect every other vertex
pentagram_lines = []
for i in range(5):
    line, = ax.plot([x_verts[i], x_verts[(i + 2) % 5]], [y_verts[i], y_verts[(i + 2) % 5]],
                     color='blue', lw=2)
pentagram_lines.append(line)
pentagram_lines[0].set_label('Pentagram Diagonals') # Label only the first line for a clean legend

# --- Add Annotations ---
# Radius (R)
ax.plot([0, x_verts[0]], [0, y_verts[0]], color='red', linestyle=':', lw=2)
ax.text(0.02, y_verts[0] / 2, r'$R = \frac{\pi}{6}$', color='red', fontsize=16, ha='left')

# Side of enclosing pentagon (s)
ax.text((x_verts[0] + x_verts[1])/2 + 0.05, (y_verts[0] + y_verts[1])/2, 's', color='black', fontsize=16, style='italic')

# Side of pentagram (d = diagonal)
diag_x_mid = (x_verts[1] + x_verts[3]) / 2
diag_y_mid = (y_verts[1] + y_verts[3]) / 2
ax.text(diag_x_mid - 0.1, diag_y_mid, r'$d = \phi \cdot s$', color='blue', fontsize=16, ha='right')

# Vertex Angle (36 degrees)
# Add a small arc to denote the angle
angle_arc = patches.Arc((x_verts[2][0], y_verts[2][0]), 0.2, 0.2, angle=0,
                        theta1=162, theta2=198, color='purple', lw=1.5)
ax.add_patch(angle_arc)
ax.text(x_verts[2] + 0.08, y_verts[2], r'$36^\circ$', color='purple', fontsize=16, va='center')

# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14, labelpad=10)
ax.set_ylabel('Meters', fontsize=14, labelpad=10)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right', frameon=True, shadow=True, edgecolor='black')

# Set axis limits
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(-0.6, 0.6)

plt.show()