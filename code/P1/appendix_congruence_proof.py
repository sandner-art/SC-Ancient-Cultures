import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup for Consistent, Publication-Quality Fonts ---
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 21
plt.rcParams['axes.labelsize'] = 17
plt.rcParams['xtick.labelsize'] = 15
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['figure.titlesize'] = 20

# --- Constants ---
PHI = (1 + np.sqrt(5)) / 2
S_P = np.pi / 6  # Outer pentagon side length = 1 royal cubit
S_I = S_P / (PHI**2) # Inner pentagon side length

# --- Calculate Radii needed for plotting ---
R_P = S_P / (2 * np.sin(np.pi / 5))
R_I = S_I / (2 * np.sin(np.pi / 5))

# --- Create Figure ---
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_title(r'Geometric Derivation of the 1-Meter Congruence', y=1.02)

# --- Calculate Vertices ---
# Outer pentagon (rotated for flat base)
angles_p = np.linspace(0, 2 * np.pi, 6)[:-1] - np.pi/10
x_p = R_P * np.cos(angles_p)
y_p = R_P * np.sin(angles_p)

# Inner pentagon (rotated by 180 degrees, or pi)
angles_i = angles_p + np.pi
x_i = R_I * np.cos(angles_i)
y_i = R_I * np.sin(angles_i)

# --- Draw Geometry ---
ax.plot(np.append(x_p, x_p[0]), np.append(y_p, y_p[0]),
        color='black', lw=2, label=r'Outer Pentagon ($s_p$)')
ax.plot(np.append(x_i, x_i[0]), np.append(y_i, y_i[0]),
        color='red', lw=2.5, label=r'Inner Pentagon ($s_i$)')
for i in range(5):
    ax.plot([x_p[i], x_p[(i + 2) % 5]], [y_p[i], y_p[(i + 2) % 5]],
            color='blue', linestyle='--', lw=1.5, alpha=0.8)

# --- Add Annotations and Proofs ---
ax.text(0, y_p[3] - 0.05, r'Initial Condition: $s_p = 1$ royal cubit = $\frac{\pi}{6}$ m',
        ha='center', va='top', fontsize=14, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black"))

ax.annotate(r'Theorem: $s_i = \frac{s_p}{\phi^2}$',
            xy=((x_i[0]+x_i[1])/2, y_i[0]), xytext=(-0.5, -0.2),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6),
            ha='center', va='center', fontsize=18, bbox=dict(fc="white", ec="red"))

bbox_props = dict(boxstyle="round,pad=0.5", fc="#FFFFFF", ec="black", lw=1.4)
ax.text(0, 0.285,
        r'Resulting Perimeter of Inner Pentagon:' '\n'
        r'$P_i = 5 \cdot s_i = 5 \cdot \frac{(\pi/6)}{\phi^2} \approx \mathbf{0.99998 \, m}$' '\n'
        r'(A 99.998\% congruence with 1 meter)'
        ,
        ha='center', va='center', fontsize=15, color='purple', bbox=bbox_props)

# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14)
ax.set_ylabel('Meters', fontsize=14)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.5)
ax.legend(loc='upper right')

lim = R_P * 1.2
ax.set_xlim(-lim, lim)
ax.set_ylim(-lim, lim)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()