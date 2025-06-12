import matplotlib.pyplot as plt
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(10, 6))

# --- Define Planetary Models ---
# Latitude in degrees
phi = np.linspace(0, 80, 500) # Up to 80 degrees to avoid extreme tan values
phi_rad = np.deg2rad(phi)

# 1. Spherical Model s = tan(phi)
s_spherical = np.tan(phi_rad)

# 2. Flat Model s = d/H
# Assume Earth-like circumference C=40,000 km and sun altitude H=5,000 km
C = 40000
H = 5000
d = (phi / 360) * C
s_flat = d / H

# --- Plot the theoretical curves ---
ax.plot(phi, s_spherical, label='Spherical Model ($s = \\tan(\\phi)$)', color='#003366', linewidth=2.5)
ax.plot(phi, s_flat, label='Flat Model ($s \\propto d$)', color='#CC3311', linestyle='--', linewidth=2.5)

# --- Generate and plot mock data points ---
# Three data points that fit the spherical model perfectly
mock_phi = np.array([20, 45, 65])
mock_s = np.tan(np.deg2rad(mock_phi))

ax.scatter(mock_phi, mock_s, color='black', zorder=5, s=80, label='Observation Points (n=3)')

# --- Annotations ---
# Annotate the third point to show divergence
ax.annotate(
    'Third data point falsifies\nthe linear (flat) model',
    xy=(mock_phi[2], mock_s[2]),
    xytext=(45, 3.5),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=8),
    ha='center', va='center', fontsize=12,
    bbox=dict(boxstyle="round,pad=0.3", fc="ivory", ec="gray", lw=1)
)

# --- Axis Labels, Title, and Legend ---
ax.set_xlabel('Angular Distance from Subsolar Point (Latitude $\\phi$ in degrees)')
ax.set_ylabel('Shadow Length / Gnomon Height ($s/h$)')
ax.set_title("Distinguishing Planetary Geometries via Shadow Curves", fontsize=16, weight='bold')
ax.legend(loc='upper left')
ax.grid(True, which='both', linestyle=':', linewidth=0.5)

# --- Set axis limits for clarity ---
ax.set_xlim(0, 80)
ax.set_ylim(0, 5)

# --- Final Touches ---
plt.tight_layout()
plt.savefig("figure_2_shadow_curves.png", dpi=300)
plt.show()