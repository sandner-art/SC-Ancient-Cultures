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
ax.set_title(r'Deep Harmony of the Royal Cubit Dodecagon', y=1.02)

# --- Calculate Vertices ---
angles = np.linspace(0, 2 * np.pi, N_SIDES + 1)[:-1] + np.pi/2
x_verts = R_DODECAGON * np.cos(angles)
y_verts = R_DODECAGON * np.sin(angles)

# --- Draw Geometry ---
# 1. The Dodecagon (as a faint guide)
ax.plot(np.append(x_verts, x_verts[0]), np.append(y_verts, y_verts[0]),
        color='blue', lw=1.5, alpha=0.4, linestyle=':', label=r'Dodecagon ($s_{12} = \pi/6$)')

# 2. First Equilateral Triangle (Vertices 0, 4, 8)
tri1_verts_x = [x_verts[0], x_verts[4], x_verts[8], x_verts[0]]
tri1_verts_y = [y_verts[0], y_verts[4], y_verts[8], y_verts[0]]
ax.plot(tri1_verts_x, tri1_verts_y, color='green', lw=3, label='Primary Equilateral Triangle')

# 3. Second, Interlocking Equilateral Triangle (Vertices 2, 6, 10)
tri2_verts_x = [x_verts[2], x_verts[6], x_verts[10], x_verts[2]]
tri2_verts_y = [y_verts[2], y_verts[6], y_verts[10], y_verts[2]]
ax.plot(tri2_verts_x, tri2_verts_y, color='orange', lw=3, label='Secondary Equilateral Triangle')

# 4. The Circumscribing Circle and Radius Trace
ax.add_patch(patches.Circle((0, 0), R_DODECAGON, fill=False, color='red', linestyle='--', lw=1.5, label=r'Circumradius ($R_{12}$)' ))
ax.plot([0, x_verts[0]], [0, y_verts[0]], color='red', linestyle=':', lw=2) # Trace R12
ax.text(x_verts[0] * 0.5, y_verts[0] * 0.6, r'$R_{12}$', color='red', fontsize=16)

# --- Add Annotation Box ---
bbox_props = dict(boxstyle="round,pad=0.5", fc="#FFFF99", ec="black", lw=1.5)
ax.text(
    0, 0,
    r'\textbf{Geometric Proof of Harmony}:' '\n'
    r'The dodecagon is composed of' '\n'
    r'\textbf{two interlocking equilateral triangles},' '\n'
    r'forming a perfect hexagram.' '\n\n'
    r'When $s_{12} = \pi/6$, then $R_{12} \approx \mathbf{1.0116 \, m}$',
    ha='center', va='center', fontsize=15, color='purple', bbox=bbox_props
)

# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14)
ax.set_ylabel('Meters', fontsize=14)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.15))

lim = R_DODECAGON * 1.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()