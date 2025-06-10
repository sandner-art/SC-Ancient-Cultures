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
R_DODECAGON = S_LENGTH / (2 * np.sin(np.pi / N_SIDES)) # ≈ 1.0116 m

# --- Create Figure ---
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_title(r'Geometric Harmonies of the Royal Cubit Dodecagon', y=1.02)

# --- Calculate Vertices ---
# Start angle chosen to place one vertex at the top
angles = np.linspace(0, 2 * np.pi, N_SIDES + 1)[:-1] + np.pi/2
x_verts = R_DODECAGON * np.cos(angles)
y_verts = R_DODECAGON * np.sin(angles)

# --- Draw Geometry ---
# 1. The Dodecagram (Inner Star)
for i in range(N_SIDES):
    ax.plot([x_verts[i], x_verts[(i + 5) % N_SIDES]], [y_verts[i], y_verts[(i + 5) % N_SIDES]],
            color='purple', linestyle=':', lw=1, alpha=0.8, label='Dodecagram' if i==0 else "")

# 2. The Main Equilateral Triangle (Vertices 0, 4, 8)
tri_verts_x = [x_verts[0], x_verts[4], x_verts[8], x_verts[0]]
tri_verts_y = [y_verts[0], y_verts[4], y_verts[8], y_verts[0]]
ax.plot(tri_verts_x, tri_verts_y, color='green', lw=2.5, label='Emergent Equilateral Triangle')

# 3. The Dodecagon
ax.plot(np.append(x_verts, x_verts[0]), np.append(y_verts, y_verts[0]),
        color='blue', lw=2, alpha=0.7, label=r'Dodecagon Side ($s_{12} = \pi/6$)')

# 4. The Circumscribing Circle
ax.add_patch(patches.Circle((0, 0), R_DODECAGON, fill=False, color='red', linestyle='--', lw=1.5, label=r'Circumradius ($R_{12}$)' ))

# --- THIS IS THE ADDED SECTION ---
# 5. Trace the Radius R12 for clarity
# We draw a line from the center to the top vertex
ax.plot([0, x_verts[0]], [0, y_verts[0]], color='red', linestyle=':', lw=2.5)
# Add a text label next to the traced radius
ax.text(x_verts[0] * 0.4, y_verts[0] * 0.6, r'$R_{12}$', color='red', fontsize=18, ha='center')
# --- END OF ADDED SECTION ---


# --- Add Annotations ---
# Label the emergent triangle
ax.text(0, -0.2, 'Perfect Equilateral\nTriangle Emerges', ha='center', color='green', fontsize=14,
        bbox=dict(fc='white', alpha=0.7, ec='none'))

# Central "Punchline" Annotation Box
bbox_props = dict(boxstyle="round,pad=0.5", fc="#FFFFFF", ec="black", lw=1.5)
ax.text(
    0, R_DODECAGON * 0.4,
    r'Result:' '\n'
    r'When $s_{12} = \frac{\pi}{6}$ m (1 royal cubit),' '\n'
    r'The Circumradius $R_{12} \approx \mathbf{1.0116 \, m}$' '\n'
    r'(A 99% congruence with 1 meter)',
    ha='center', va='center', fontsize=15, color='purple', bbox=bbox_props
)

# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14)
ax.set_ylabel('Meters', fontsize=14)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='lower left', bbox_to_anchor=(0.0125, 0.0125))

lim = R_DODECAGON * 1.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()