import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup (1 row, 2 columns) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("The Role of Solar Declination ($\delta$) in Modern Measurements", fontsize=16, weight='bold')

def setup_earth_ax(ax, title):
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=14)
    earth = patches.Circle((0, 0), 1.0, facecolor='lightblue', edgecolor='k', alpha=0.4)
    ax.add_patch(earth)
    ax.axhline(0, color='gray', ls='--', label='Ecliptic Plane') # Sun's path
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(-1.5, 1.5)

def draw_rays(ax):
    for y in np.linspace(-1, 1, 5):
        ax.arrow(-1.5, y, 0.5, 0, head_width=0.05, head_length=0.08, fc='gold', ec='orange')
    ax.text(-1.25, 1.2, "Sun's Rays", ha='center')

# --- PANEL 1: Summer Solstice ---
setup_earth_ax(ax1, "Summer Solstice")
draw_rays(ax1)
# Tilted axis and equator
tilt = np.deg2rad(23.45)
ax1.plot([np.sin(tilt), -np.sin(tilt)], [-np.cos(tilt), np.cos(tilt)], 'k-', lw=1.5, label='Earth\'s Axis')
ax1.plot([-np.cos(tilt), np.cos(tilt)], [-np.sin(tilt), np.sin(tilt)], 'r-', lw=1.5, label='Equatorial Plane')

# Show declination angle
decl_arc = patches.Arc((0,0), 0.4, 0.4, theta1=0, theta2=np.rad2deg(tilt), color='red')
ax1.add_patch(decl_arc)
ax1.text(0.5, 0.1, r'$\delta \approx +23.5^\circ$', color='red', fontsize=12)
ax1.text(1.2, -1.2, r"$\theta_{zenith} = |\phi - \delta|$", bbox={'fc':'white', 'ec':'k'})


# --- PANEL 2: Vernal/Autumnal Equinox ---
setup_earth_ax(ax2, "Equinox")
draw_rays(ax2)
# Axis is tilted "into the page" - appears vertical in 2D
ax2.plot([0, 0], [-1, 1], 'k-', lw=1.5, label='Earth\'s Axis')
ax2.plot([-1, 1], [0, 0], 'r-', lw=1.5, label='Equatorial Plane') # Aligned with ecliptic

# Show declination is zero
ax2.text(0.2, 0.1, r'$\delta = 0^\circ$', color='red', fontsize=12)
ax2.text(1.2, -1.2, r"$\theta_{zenith} = \phi$", bbox={'fc':'white', 'ec':'k'})

# --- Final Touches ---
ax1.legend(loc='lower left')
ax2.legend(loc='lower left')
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig("figure_15_solar_declination.png", dpi=300)
plt.show()