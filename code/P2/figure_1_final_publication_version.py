import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 11

# --- Figure and Axis Setup (1 row, 2 columns) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 8))
fig.suptitle("Eratosthenes' Experiment: Geometric Principle and Temporal Rationale", fontsize=18, weight='bold')

# =============================================================================
# PANEL (a): The Core Geometric Principle (Reoriented)
# =============================================================================
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title("(a) The Core Geometric Principle", fontsize=16, pad=15)

# --- Geometric Parameters ---
R = 1.0
angle_deg = 7.2
angle_rad = np.deg2rad(angle_deg)

# --- Draw the Earth and Gnomons ---
earth = patches.Circle((0, 0), R, facecolor='#d4eaff', edgecolor='black', linewidth=1.5, zorder=2)
ax1.add_patch(earth)
ax1.plot(0, 0, 'ko', markersize=5)
gnomon_height = 0.15
syene_pos = (0, R)
alexandria_angle_from_top = np.pi/2 - angle_rad
alexandria_pos = (R * np.cos(alexandria_angle_from_top), R * np.sin(alexandria_angle_from_top))
alexandria_gnomon_top = (alexandria_pos[0] * (1 + gnomon_height/R), alexandria_pos[1] * (1 + gnomon_height/R))
ax1.plot([syene_pos[0], syene_pos[0]], [syene_pos[1], syene_pos[1] + gnomon_height], 'b-', linewidth=3, zorder=3)
ax1.plot([alexandria_pos[0], alexandria_gnomon_top[0]], [alexandria_pos[1], alexandria_gnomon_top[1]], 'b-', linewidth=3, zorder=3)
ax1.plot([0, syene_pos[0]], [0, syene_pos[1]], color='gray', linestyle=':', dashes=(4,4))
ax1.plot([0, alexandria_pos[0]], [0, alexandria_pos[1]], color='gray', linestyle=':', dashes=(4,4))

# --- Draw Sun Rays ---
ray_length = 0.8
for x_pos in [-0.5, 0, 0.5]:
    ax1.arrow(x_pos, R + gnomon_height + ray_length, 0, -ray_length,
              head_width=0.04, head_length=0.06, fc='gold', ec='orange', linewidth=1, zorder=1)
ax1.plot([alexandria_pos[0], alexandria_pos[0]], [alexandria_pos[1], alexandria_gnomon_top[1]+0.2],
         '--', color='gold', dashes=(5,5), lw=1.5)

# --- Annotations ---
ax1.text(syene_pos[0], syene_pos[1] + gnomon_height + 0.1, 'Syene', ha='center', va='bottom', fontsize=12, weight='bold')
ax1.text(alexandria_pos[0] + 0.1, alexandria_pos[1] - 0.1, 'Alexandria', ha='left', va='top', fontsize=12, weight='bold')
central_arc = patches.Arc((0, 0), 0.8, 0.8, theta1=np.rad2deg(alexandria_angle_from_top), theta2=90, color='darkred', lw=2)
ax1.add_patch(central_arc)
ax1.text(0.2, 0.35, r'$\Delta\theta$', ha='center', va='center', fontsize=16, color='darkred')
shadow_arc = patches.Arc(alexandria_gnomon_top, 0.3, 0.3, theta1=np.rad2deg(alexandria_angle_from_top)-90, theta2=0, color='darkred', lw=2)
ax1.add_patch(shadow_arc)
ax1.text(alexandria_gnomon_top[0] - 0.25, alexandria_gnomon_top[1] + 0.1, r'$\theta$', ha='center', va='center', fontsize=16, color='darkred')
ax1.text(0.75, 0, r"$\theta = \Delta\theta$", fontsize=14, bbox=dict(fc='white', ec='darkred', boxstyle='round,pad=0.3'))
ax1.text(0, R + gnomon_height + ray_length + 0.1, "Parallel Sun Rays", ha='center', va='bottom', fontsize=12)
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 2.8)

# =============================================================================
# PANEL (b): The Rationale for the Summer Solstice
# =============================================================================
ax2.set_facecolor('#F5F5F5')
ax2.axis('off')
ax2.set_title("(b) The Rationale for the Summer Solstice", fontsize=16, pad=15)

def setup_earth_ax(ax):
    # CRITICAL FIX: Enforce equal aspect ratio to prevent deformation
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')

def draw_tilted_earth(ax, tilt_deg):
    earth = patches.Circle((0, 0), 1.0, facecolor='#d4eaff', edgecolor='k', alpha=0.8, zorder=2)
    ax.add_patch(earth)
    tilt_rad = np.deg2rad(tilt_deg)
    ax.plot([np.sin(tilt_rad), -np.sin(tilt_rad)], 
            [-np.cos(tilt_rad), np.cos(tilt_rad)], 'k-', lw=1.5, label='Earth\'s Axis')
    # Draw equator as a proper projection
    t_eq = np.linspace(-np.pi/2, np.pi/2, 100)
    ax.plot(np.cos(t_eq), np.sin(t_eq) * np.sin(tilt_rad), 'r--', lw=1.5, label='Equator')
    # Draw sun rays from the right
    for y_ray in np.linspace(-0.8, 0.8, 4):
        ax.arrow(2.5, y_ray, -1.2, 0, head_width=0.08, head_length=0.1, fc='gold', ec='orange', zorder=1)

# --- Sub-panel for Solstice ---
ax_solstice = fig.add_axes([0.5, 0.5, 0.4, 0.4]) # [left, bottom, width, height]
setup_earth_ax(ax_solstice)
draw_tilted_earth(ax_solstice, 23.5)
ax_solstice.text(0, 1.7, "Summer Solstice", ha='center', weight='bold', fontsize=12)
syene_solstice_pos = (np.cos(np.deg2rad(23.5)), np.sin(np.deg2rad(23.5)))
ax_solstice.plot(*syene_solstice_pos, 'bo', markersize=8)
ax_solstice.annotate('Syene receives direct sunlight\n(No Shadow)', xy=syene_solstice_pos, xytext=(0, -1.2),
                     ha='center', va='center', color='blue',
                     arrowprops=dict(arrowstyle="->", color="blue", shrinkA=5, shrinkB=5,
                                     connectionstyle="arc3,rad=0.3"))

# --- Sub-panel for Equinox ---
ax_equinox = fig.add_axes([0.5, 0.1, 0.4, 0.4])
setup_earth_ax(ax_equinox)
draw_tilted_earth(ax_equinox, 0) # No tilt relative to sun
ax_equinox.text(0, 1.7, "Equinox", ha='center', weight='bold', fontsize=12)
syene_equinox_pos = (np.cos(np.deg2rad(23.5)), np.sin(np.deg2rad(23.5)))
ax_equinox.plot(*syene_equinox_pos, 'ro', markersize=8)
ax_equinox.plot([syene_equinox_pos[0]-0.25, syene_equinox_pos[0]], 
              [syene_equinox_pos[1], syene_equinox_pos[1]], 'r-', lw=5) # Shadow
ax_equinox.annotate('Syene is not aligned\n(Casts a Shadow)', xy=syene_equinox_pos, xytext=(0, -1.2),
                     ha='center', va='center', color='red',
                     arrowprops=dict(arrowstyle="->", color="red", shrinkA=5, shrinkB=5,
                                     connectionstyle="arc3,rad=-0.3"))

# --- Final Central Explanation Text for Panel (b) ---
ax2.text(0.5, 0.5,
         "The experiment required a location where the Sun was\n"
         "at the zenith ($\theta=0^\circ$). This only occurs on the\n"
         "Tropic of Cancer ($\phi=23.5^\circ$N) on the one day\n"
         "the Earth's tilt maximally faces the Sun:\n"
         "the summer solstice.",
         ha='center', va='center', transform=ax2.transAxes, fontsize=13,
         bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=1))

# --- Final Figure Touches ---
plt.savefig("figure_1_final_publication_version.png", dpi=300)
plt.show()