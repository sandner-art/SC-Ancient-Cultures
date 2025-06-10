import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 20

# --- Constants and Calculations ---
S_LENGTH = np.pi / 6  # Side length = 1 royal cubit
N_SIDES = 12
# Formula for circumradius R from side s for n-gon: R = s / (2 * sin(pi/n))
R_DODECAGON = S_LENGTH / (2 * np.sin(np.pi / N_SIDES)) # ≈ 1.0116 m

# --- Create Figure ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title(r'The Dodecagon-Circumradius Congruence', y=1.02)

# --- Calculate Vertices ---
# Start angle chosen to place one vertex at the top
angles = np.linspace(0, 2 * np.pi, N_SIDES + 1)[:-1] + np.pi/2
x_verts = R_DODECAGON * np.cos(angles)
y_verts = R_DODECAGON * np.sin(angles)

# --- Draw Geometry ---
# Circumscribing Circle
ax.add_patch(patches.Circle((0, 0), R_DODECAGON, fill=False, color='red', linestyle='--', lw=2, label=r'Circumradius ($R_{12}$)' ))
# Dodecagon
ax.plot(np.append(x_verts, x_verts[0]), np.append(y_verts, y_verts[0]),
        color='blue', lw=2.5, label=r'Dodecagon Side ($s_{12}$)')

# --- Add Annotations ---
# Label a side
side_mid_x = (x_verts[0] + x_verts[1]) / 2
side_mid_y = (y_verts[0] + y_verts[1]) / 2
ax.text(side_mid_x * 1.05, side_mid_y * 1.05, r'$s_{12} = \frac{\pi}{6}$ m', color='blue', fontsize=14, ha='center')

# Label the radius
ax.plot([0, x_verts[2]], [0, y_verts[2]], color='red', linestyle=':', lw=2)
ax.text(x_verts[2] * 0.5, y_verts[2] * 0.5 + 0.1, r'$R_{12}$', color='red', fontsize=16)

# Central "Punchline" Annotation Box
bbox_props = dict(boxstyle="round,pad=0.5", fc="#FFFF99", ec="black", lw=1.5)
ax.text(
    0, 0,
    r'\textbf{Result}:' '\n'
    r'$R_{12} = \frac{s_{12}}{2 \sin(15^\circ)} = \frac{\pi/6}{2 \sin(15^\circ)} \approx \mathbf{1.0116 \, m}$' '\n'
    r'(A 99\% congruence with 1 meter)',
    ha='center', va='center', fontsize=15, color='purple', bbox=bbox_props
)

# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14)
ax.set_ylabel('Meters', fontsize=14)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper right')

lim = R_DODECAGON * 1.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()