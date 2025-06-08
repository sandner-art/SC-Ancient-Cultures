import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['figure.titlesize'] = 20

# --- Figure Creation ---
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_title(r'Visual Proof of Exact Trigonometric Values at $\theta = \pi/6$', y=1.02)

# --- Draw Unit Circle and Axes ---
ax.add_patch(patches.Circle((0, 0), 1, fill=False, color='black', lw=2))
ax.axhline(0, color='black', alpha=0.5, lw=1)
ax.axvline(0, color='black', alpha=0.5, lw=1)

# --- Define the 30-degree angle (pi/6) ---
angle = np.pi / 6
x_coord = np.cos(angle)
y_coord = np.sin(angle)

# --- Draw the 30-60-90 Triangle ---
# Radius (Hypotenuse)
ax.plot([0, x_coord], [0, y_coord], color='red', lw=2.5, label=r'Radius (Hypotenuse) = 1')
# Opposite side (sin)
ax.plot([x_coord, x_coord], [0, y_coord], color='blue', linestyle='--', lw=2, label=r'Opposite Side = $\sin(\pi/6)$')
# Adjacent side (cos)
ax.plot([0, x_coord], [0, 0], color='green', linestyle='--', lw=2, label=r'Adjacent Side = $\cos(\pi/6)$')

# --- Add Annotations and Proofs ---
# Angle marker
ax.add_patch(patches.Arc((0, 0), 0.4, 0.4, angle=0, theta1=0, theta2=30, color='purple', lw=1.5))
ax.text(0.25, 0.06, r'$30^\circ = \frac{\pi}{6}$', color='purple', fontsize=18)

# Labels for side lengths
ax.text(x_coord / 2, y_coord / 2 + 0.06, 'R=1', color='red', fontsize=16, rotation=30)
ax.text(x_coord + 0.02, y_coord / 2, r'$\sin(\frac{\pi}{6}) = \frac{1}{2}$', color='blue', fontsize=18)
ax.text(x_coord / 2, -0.14, r'$\cos(\frac{\pi}{6}) = \frac{\sqrt{3}}{2}$', color='green', fontsize=18)

# Point on circle
ax.plot(x_coord, y_coord, 'ro')
ax.text(x_coord + 0.03, y_coord + 0.03, r'$(\frac{\sqrt{3}}{2}, \frac{1}{2})$', fontsize=18)

# --- Final Plot Adjustments ---
ax.set_xlabel('x-axis', fontsize=14)
ax.set_ylabel('y-axis', fontsize=14)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='lower right', frameon=True, shadow=True, edgecolor='black')

lim = 1.3
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()