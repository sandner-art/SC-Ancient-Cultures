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
plt.rcParams['figure.titlesize'] = 20

# --- Constants ---
PHI = (1 + np.sqrt(5)) / 2
R = np.pi / 6 # Circumradius = 1 royal cubit

# --- Create Figure ---
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_title(r'Emergent Complexity from Interfering Geometries', y=1.02)

# --- Calculate Vertices ---
# Pentagon 1 (standard orientation)
angles1 = np.linspace(0, 2 * np.pi, 6)[:-1] + np.pi/2
x1 = R * np.cos(angles1)
y1 = R * np.sin(angles1)

# Pentagon 2 (rotated by 36 degrees)
angles2 = angles1 + np.pi / 5
x2 = R * np.cos(angles2)
y2 = R * np.sin(angles2)

# --- Draw Geometry ---
# Pentagram 1
for i in range(5):
    ax.plot([x1[i], x1[(i + 2) % 5]], [y1[i], y1[(i + 2) % 5]],
            color='blue', linestyle='--', lw=1.5, alpha=0.8)
# Pentagram 2
for i in range(5):
    ax.plot([x2[i], x2[(i + 2) % 5]], [y2[i], y2[(i + 2) % 5]],
            color='red', linestyle='--', lw=1.5, alpha=0.8)

# The enclosing circle
ax.add_patch(patches.Circle((0, 0), R, fill=False, color='black', lw=2))

# --- Add Annotations ---
# Central Decagram
ax.text(0, 0, 'Emergent\n10/2 From 10/4\nDecagram', ha='center', va='center', fontsize=14, color='purple',
        bbox=dict(boxstyle="circle", fc="white", ec="purple", lw=1))

# Annotation for segmentation
diag_x = [x1[1], x1[3]]
diag_y = [y1[1], y1[3]]
ax.plot(diag_x, diag_y, color='blue', lw=3, label='Original Pentagram Diagonal')
ax.text(-0.25, -0.25, 'Diagonal now segmented\ninto complex ratios', fontsize=12,
        bbox=dict(fc="white", ec="blue"))

# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14)
ax.set_ylabel('Meters', fontsize=14)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(loc='upper right')

lim = R * 1.3
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()