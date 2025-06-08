import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 11
plt.rcParams['figure.titlesize'] = 18

# --- Constants ---
ROYAL_CUBIT = np.pi / 6  # Circumradius R
PHI = (1 + np.sqrt(5)) / 2

# --- Create Figure ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharey=True)
fig.suptitle(r'Comparative Geometry within the Royal Cubit (R = $\pi/6$) Framework', y=0.98)

# --- Panel 1: Pentagon ---
ax1.set_title(r'Pentagon ($\phi$-based Geometry)')
# Calculate vertices
angles_p = np.linspace(0, 2 * np.pi, 6)[:-1] + np.pi/2
x_p = ROYAL_CUBIT * np.cos(angles_p)
y_p = ROYAL_CUBIT * np.sin(angles_p)

# Draw circumcircle
ax1.add_patch(patches.Circle((0,0), ROYAL_CUBIT, fill=False, color='black', linestyle='--', lw=1, alpha=0.5, label='Circumcircle'))
# Draw pentagon
ax1.plot(np.append(x_p, x_p[0]), np.append(y_p, y_p[0]), color='blue', lw=2, label=r'Pentagon Sides ($s_{penta}$)')
# Draw diagonal
ax1.plot([x_p[0], x_p[2]], [y_p[0], y_p[2]], color='orange', linestyle=':', lw=2, label=r'Diagonal (d)')

# Annotations for Pentagon
ax1.plot([0, x_p[0]], [0, y_p[0]], color='red', linestyle='--', lw=1.5)
ax1.text(0.02, y_p[0]/2, r'$R = \frac{\pi}{6}$', color='red', fontsize=15)
ax1.text((x_p[3]+x_p[4])/2, (y_p[3]+y_p[4])/2 - 0.05, r'$s_{penta}$', color='blue', fontsize=15, style='italic', ha='center')
ax1.text((x_p[0]+x_p[2])/2-0.08, (y_p[0]+y_p[2])/2, r'$d = \phi \cdot s_{penta}$', color='orange', fontsize=15)
ax1.text(x_p[3]+0.03, y_p[3]+0.05, r'$108^\circ$', color='purple', fontsize=15)

# --- Panel 2: Hexagon ---
ax2.set_title(r'Hexagon (Perfect $\pi$-based Geometry)')
# Calculate vertices
angles_h = np.linspace(0, 2 * np.pi, 7)[:-1] + np.pi/2
x_h = ROYAL_CUBIT * np.cos(angles_h)
y_h = ROYAL_CUBIT * np.sin(angles_h)

# Draw circumcircle
ax2.add_patch(patches.Circle((0,0), ROYAL_CUBIT, fill=False, color='black', linestyle='--', lw=1, alpha=0.5))
# Draw hexagon
ax2.plot(np.append(x_h, x_h[0]), np.append(y_h, y_h[0]), color='green', lw=2, label=r'Hexagon Sides ($s_{hex}$)')

# Annotations for Hexagon
ax2.plot([0, x_h[0]], [0, y_h[0]], color='red', linestyle='--', lw=1.5)
ax2.text(0.02, y_h[0]/2, r'$R = \frac{\pi}{6}$', color='red', fontsize=15)
ax2.text((x_h[1]+x_h[2])/2 + 0.03, (y_h[1]+y_h[2])/2, r'$s_{hex}$', color='green', fontsize=15, style='italic')

# Central annotation box for hexagon's perfect properties
bbox_props_hex = dict(boxstyle="round,pad=0.3", fc="white", ec="purple", lw=1, alpha=0.8)
ax2.text(0, -0.2, r'$s_{hex} = R = \frac{\pi}{6}$' '\n' r'$120^\circ = 4 \times 30^\circ$',
         ha='center', va='center', fontsize=16, color='purple', bbox=bbox_props_hex)

# --- Final Plot Adjustments for both panels ---
for ax in [ax1, ax2]:
    ax.set_xlabel('Meters', fontsize=14, labelpad=10)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(loc='upper right')
    ax.set_xlim(-0.6, 0.6)
    ax.set_ylim(-0.6, 0.6)

ax1.set_ylabel('Meters', fontsize=14, labelpad=10)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()