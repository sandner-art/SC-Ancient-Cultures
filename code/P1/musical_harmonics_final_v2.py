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
plt.rcParams['figure.titlesize'] = 18

# --- Figure and Subplots ---
# Create a figure with 3 rows for the main intervals and a 4th for the conclusion
fig, axs = plt.subplots(4, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [1, 1, 1, 0.5]})
fig.suptitle('The Physics of Musical Consonance: The Monochord and Harmonic Ratios', y=0.98)

# --- Data for plotting ---
L = 1.0  # Length of the string
x = np.linspace(0, L, 500)
amplitude = 0.05

# --- Plot 1: Fundamental ---
ax = axs[0]
ax.plot(x, amplitude * np.sin(np.pi * x / L), color='blue')
ax.plot([0, L], [0, 0], color='black', lw=2)
ax.plot([0, 0], [-0.01, 0.01], color='black', lw=3)
ax.plot([L, L], [-0.01, 0.01], color='black', lw=3)
ax.text(L + 0.05, 0, r'\textbf{Fundamental (1:1)}' '\n' r'Full String Length ($L$)', va='center', fontsize=14)
ax.set_xlim(-0.1, L + 0.5)
ax.axis('off')

# --- Plot 2: Octave ---
ax = axs[1]
x_octave = np.linspace(0, L/2, 250)
ax.plot(x_octave, amplitude * np.sin(2 * np.pi * x_octave / L), color='green')
ax.plot([0, L], [0, 0], color='black', lw=2)
ax.plot([0, 0], [-0.01, 0.01], color='black', lw=3)
ax.plot([L, L], [-0.01, 0.01], color='black', lw=3)
# Movable bridge
ax.add_patch(patches.Polygon([[L/2, 0], [L/2-0.01, -0.02], [L/2+0.01, -0.02]], color='black'))
ax.text(L/2, -0.04, r'$L/2$', ha='center', fontsize=12)
ax.text(L + 0.05, 0, r'\textbf{Octave}' '\n' r'Division by 2 (Frequency Ratio 2:1)', va='center', fontsize=14)
ax.set_xlim(-0.1, L + 0.5)
ax.axis('off')

# --- Plot 3: Perfect Fifth ---
ax = axs[2]
x_fifth = np.linspace(0, 2*L/3, 333)
ax.plot(x_fifth, amplitude * np.sin(1.5 * np.pi * x_fifth / L), color='chocolate')
ax.plot([0, L], [0, 0], color='black', lw=2)
ax.plot([0, 0], [-0.01, 0.01], color='black', lw=3)
ax.plot([L, L], [-0.01, 0.01], color='black', lw=3)
# Movable bridge
ax.add_patch(patches.Polygon([[2*L/3, 0], [2*L/3-0.01, -0.02], [2*L/3+0.01, -0.02]], color='black'))
ax.text(2*L/3, -0.04, r'$2L/3$', ha='center', fontsize=12)
ax.text(L + 0.05, 0, r'\textbf{Perfect Fifth}' '\n' r'Division by 3 (Frequency Ratio 3:2)', va='center', fontsize=14)
ax.set_xlim(-0.1, L + 0.5)
ax.axis('off')

# --- Plot 4: Conclusion Box ---
ax = axs[3]
bbox_props = dict(boxstyle="round,pad=0.5", fc="#EAEAFD", ec="black", lw=1)
ax.text(0.5, 0.5,
        r'A \textbf{Duodecimal (Base-12)} system is uniquely suited for harmony' '\n'
        r'because it is elegantly divisible by both \textbf{2} and \textbf{3},' '\n'
        r'the generators of the most consonant intervals.',
        ha='center', va='center', fontsize=14, color='purple', bbox=bbox_props)
ax.axis('off')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()