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
plt.rcParams['legend.fontsize'] = 11
plt.rcParams['figure.titlesize'] = 20

# --- Constants ---
R = np.pi / 6  # Royal Cubit Radius

# --- Create Figure ---
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_title(r'The Unified Geometric Framework (R = $\pi/6$)', y=1.02)

# --- Layer 1: The Duodecimal Canvas ---
# Draw the 12 radial lines for the 30-degree divisions
for i in range(12):
    angle = i * np.pi / 6
    ax.plot([0, R * np.cos(angle)], [0, R * np.sin(angle)],
            color='gray', linestyle=':', lw=1, alpha=0.8)

# --- Layer 2: Hexagonal System (6-Fold Symmetry) ---
angles_h = np.linspace(0, 2 * np.pi, 7)[:-1]
x_h = R * np.cos(angles_h)
y_h = R * np.sin(angles_h)
# Hexagon
ax.plot(np.append(x_h, x_h[0]), np.append(y_h, y_h[0]),
        color='green', lw=2.5, label='Hexagon (Perfect Fit)')
# Hexagram (Star of David)
for i in range(6):
    ax.plot([x_h[i], x_h[(i + 2) % 6]], [y_h[i], y_h[(i + 2) % 6]],
            color='green', linestyle='--', lw=1.5, alpha=0.7, label='Hexagram' if i == 0 else "")


# --- Layer 3: Pentagonal System (5-Fold Symmetry) ---
angles_p = np.linspace(0, 2 * np.pi, 6)[:-1] + np.pi/10 # Offset to avoid vertex overlap
x_p = R * np.cos(angles_p)
y_p = R * np.sin(angles_p)
# Pentagon
# ax.plot(np.append(x_p, x_p[0]), np.append(y_p, y_p[0]),
#        color='blue', lw=2, label='Pentagon (Harmonious Fit)')
# Pentagram
#for i in range(5):
#    ax.plot([x_p[i], x_p[(i + 2) % 5]], [y_p[i], y_p[(i + 2) % 5]],
#            color='blue', linestyle='--', lw=1.5, alpha=0.7, label='Pentagram' if i == 0 else "")


# --- Layer 4: The Unifying Circle ---
ax.add_patch(patches.Circle((0, 0), R, fill=False, color='black', lw=3))
ax.text(0, R + 0.05, r'(Radius = 1 RC = $\pi/6$ m)',
        ha='center', va='bottom', fontsize=14)

# --- Strategic Annotations ---
# Annotation for Hexagon perfect fit
hex_vertex = (x_h[1], y_h[1]) # 60 degrees
ax.annotate('Perfect Alignment:\nHexagon vertex on\n60° grid line',
            xy=hex_vertex, xytext=(hex_vertex[0] + 0.15, hex_vertex[1] + 0.15),
            arrowprops=dict(facecolor='green', shrink=0.05, width=1, headwidth=6),
            ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="green", lw=1))

# Annotation for Pentagon harmonious fit
# penta_vertex = (x_p[0], y_p[0]) # 36 degrees
# ax.annotate('Harmonious Fit:\nPentagon vertex\n(not aligned)',
#             xy=penta_vertex, xytext=(penta_vertex[0] + 0.2, penta_vertex[1] - 0.1),
#            arrowprops=dict(facecolor='blue', shrink=0.05, width=1, headwidth=6),
#            ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="blue", lw=1))


# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14, labelpad=10)
ax.set_ylabel('Meters', fontsize=14, labelpad=10)
ax.set_aspect('equal')
ax.grid(False) # Grid is replaced by the duodecimal lines
ax.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.15), ncol=2)

# Set axis limits
lim = R * 1.5
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

plt.show()