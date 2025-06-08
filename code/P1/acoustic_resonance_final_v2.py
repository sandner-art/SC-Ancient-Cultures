import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup for Consistent, Publication-Quality Fonts ---
# Use a serif font that mimics the 'LaTeX' look of the previous figures.
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral', 'Times New Roman', 'DejaVu Serif']
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.titlesize'] = 20


# --- Constants and Dimensions ---
ROYAL_CUBIT = np.pi / 6  # ≈ 0.5236 meters
L_CUBITS = 20
W_CUBITS = 10
L_METERS = L_CUBITS * ROYAL_CUBIT  # ≈ 10.47 m
W_METERS = W_CUBITS * ROYAL_CUBIT  # ≈ 5.23 m

# --- Figure Creation ---
fig, ax = plt.subplots(figsize=(12, 8))
fig.suptitle('Acoustic Resonance in the King\'s Chamber', y=0.98)

# --- Draw the Chamber ---
chamber = patches.Rectangle(
    (0, 0), L_METERS, W_METERS,
    linewidth=2, edgecolor='black', facecolor='#F5DEB3', alpha=0.6,
    label='Chamber Floor Plan'
)
ax.add_patch(chamber)


# --- Illustrate the Standing Waves (The Octave) ---
# The fundamental mode is half a sine wave (n=1)
# Amplitude for visualization
amplitude = 1.0

# 1. Longitudinal Wave (Length)
x_wave_L = np.linspace(0, L_METERS, 500)
# Wavelength lambda_L = 2 * L
y_wave_L = W_METERS / 2 + amplitude * np.sin(np.pi * x_wave_L / L_METERS)
ax.plot(x_wave_L, y_wave_L, color='red', lw=2.5, label=r'Length Mode ($f_L$): $\lambda_L = 2L$')

# 2. Transverse Wave (Width)
y_wave_W = np.linspace(0, W_METERS, 500)
# Wavelength lambda_W = 2 * W
x_wave_W = L_METERS / 2 + amplitude * np.sin(np.pi * y_wave_W / W_METERS)
ax.plot(x_wave_W, y_wave_W, color='blue', lw=2.5, label=r'Width Mode ($f_W$): $\lambda_W = 2W$')


# --- Add Annotations and Labels ---
# Dimension Labels
ax.text(L_METERS / 2, -0.5, f'Length = {L_CUBITS} royal cubits', ha='center', va='top', fontsize=14)
ax.text(-0.5, W_METERS / 2, f'Width = {W_CUBITS} royal cubits', ha='right', va='center', fontsize=14, rotation='vertical')

# Central Annotation Box
bbox_props = dict(boxstyle="round,pad=0.5", fc="#FFFF99", ec="black", lw=1)
ax.text(
    L_METERS / 2, W_METERS * 0.9,
    r'Dimension Ratio: $\frac{L}{W} = \frac{20}{10} = 2:1$' '\n'
    r'Frequency Ratio: $f_W = 2 \times f_L \Rightarrow$ Perfect Musical Octave',
    ha='center', va='bottom', fontsize=15, color='purple', bbox=bbox_props
)


# --- Final Plot Adjustments ---
ax.set_xlabel('Meters', fontsize=14, labelpad=10)
ax.set_ylabel('Meters', fontsize=14, labelpad=10)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)

# Set axis limits to give some padding
ax.set_xlim(-2, L_METERS + 2)
ax.set_ylim(-2, W_METERS + 2)

ax.legend(loc='upper right', frameon=True, shadow=True, edgecolor='black')

plt.tight_layout(rect=[0, 0, 1, 0.95]) # Adjust for suptitle
plt.show()