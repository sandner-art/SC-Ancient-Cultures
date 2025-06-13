import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 14
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['legend.fontsize'] = 12
plt.rcParams['figure.autolayout'] = False

# --- Figure and Layout Setup ---
fig = plt.figure(figsize=(16, 9))
gs = gridspec.GridSpec(2, 2, figure=fig, width_ratios=[1, 1], height_ratios=[1, 1])
fig.suptitle("Eratosthenes' Experiment: Geometric Principle and Temporal Rationale", fontsize=20)

# =============================================================================
# PANEL (a): The Core Geometric Principle
# =============================================================================
ax1 = fig.add_subplot(gs[:, 0])
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title("(a) The Core Geometric Principle", fontsize=18, pad=20)
R = 1.0
angle_deg = 7.2
angle_rad = np.deg2rad(angle_deg)
earth_a = patches.Circle((0, 0), R, facecolor="#ffffff", edgecolor='black', linewidth=2, zorder=2)
ax1.add_patch(earth_a)
ax1.plot(0, 0, 'ko', markersize=6, zorder=3)
gnomon_height = 0.15
syene_pos = (0, R)
alexandria_angle_from_top = np.pi / 2 - angle_rad
alexandria_pos = (R * np.cos(alexandria_angle_from_top), R * np.sin(alexandria_angle_from_top))
alexandria_gnomon_top = (alexandria_pos[0] * (1 + gnomon_height / R), alexandria_pos[1] * (1 + gnomon_height / R))
ax1.plot([syene_pos[0], syene_pos[0]], [syene_pos[1], syene_pos[1] + gnomon_height], 'b-', linewidth=3, zorder=4)
ax1.plot([alexandria_pos[0], alexandria_gnomon_top[0]], [alexandria_pos[1], alexandria_gnomon_top[1]], 'b-', linewidth=3, zorder=4)
ax1.plot([0, syene_pos[0]], [0, syene_pos[1]], color='gray', linestyle='--', dashes=(4, 4), zorder=3)
ax1.plot([0, alexandria_pos[0]], [0, alexandria_pos[1]], color='gray', linestyle='--', dashes=(4, 4), zorder=3)
ray_length = 0.7
for x_pos in [-0.5, 0, 0.5]:
    ax1.arrow(x_pos, R + gnomon_height + ray_length + 0.1, 0, -ray_length,
              head_width=0.04, head_length=0.06, fc='gold', ec='orange', linewidth=1.5, zorder=1)
ax1.plot([alexandria_gnomon_top[0], alexandria_gnomon_top[0]], [alexandria_pos[1] - 0.1, alexandria_gnomon_top[1] + 0.2],
         '--', color='orange', dashes=(5, 5), lw=1.5, zorder=3)
ax1.text(syene_pos[0] + 0.01, syene_pos[1] + gnomon_height + 0.1, 'Syene', ha='left', va='bottom', fontsize=16)
ax1.text(alexandria_pos[0] + 0.1, alexandria_pos[1] + 0.1, 'Alexandria', ha='left', va='top', fontsize=16)
ax1.text(-0.5, R + gnomon_height + ray_length + 0.15, "Parallel Sun Rays", ha='center', va='bottom', fontsize=16)
central_arc = patches.Arc((0, 0), 0.6, 0.6, theta1=np.rad2deg(alexandria_angle_from_top), theta2=90, color='darkred', lw=2)
ax1.add_patch(central_arc)
ax1.text(0.2, 0.25, r'$\Delta\theta$', ha='center', va='center', fontsize=22, color='darkred')
shadow_arc = patches.Arc(alexandria_pos, 0.4, 0.4, theta1=90, theta2=90 + angle_deg, color='darkred', lw=2)
ax1.add_patch(shadow_arc)
ax1.text(alexandria_pos[0] + 0.25, alexandria_pos[1] + 0.2, r'$\theta$', ha='center', va='center', fontsize=22, color='darkred')
shadow_on_surface = patches.Arc((0, 0), 2 * R, 2 * R,
                                theta1=np.rad2deg(alexandria_angle_from_top - angle_rad),
                                theta2=np.rad2deg(alexandria_angle_from_top),
                                color='darkred', lw=5, zorder=3)
ax1.add_patch(shadow_on_surface)
ax1.text(0.8, -0.2, r"By geometry, $\theta = \Delta\theta$", fontsize=16, bbox=dict(fc='white', ec='darkred', boxstyle='round,pad=0.3'))
ax1.set_xlim(-1.8, 1.8)
ax1.set_ylim(-1.2, 2.8)

# =============================================================================
# PANEL (b): The Rationale for the Summer Solstice (GEOMETRY CORRECTED)
# =============================================================================
ax_b_container = fig.add_subplot(gs[:, 1])
ax_b_container.axis('off')
ax_b_container.set_title("(b) The Rationale for the Summer Solstice", fontsize=18, pad=20)

def setup_earth_ax(ax):
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-1.8, 1.8)
    ax.axis('off')
    for y_ray in np.linspace(-0.8, 0.8, 4):
        ax.arrow(2.2, y_ray, -0.7, 0, head_width=0.08, head_length=0.12, fc='gold', ec='orange', zorder=1)

gs_b = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs[:, 1], hspace=0.2, height_ratios=[1, 0.8, 1])
ax_solstice = fig.add_subplot(gs_b[0, 0])
ax_equinox = fig.add_subplot(gs_b[2, 0])
ax_text = fig.add_subplot(gs_b[1, 0])
ax_text.axis('off')

# --- Solstice Sub-panel (Corrected Geometry) ---
ax_solstice.set_title("Summer Solstice", fontsize=14, pad=5)
setup_earth_ax(ax_solstice)
tilt_deg = 23.5
tilt_rad = np.deg2rad(tilt_deg)
earth_b1 = patches.Circle((0, 0), R, facecolor="#fefefe", edgecolor='k', linewidth=2, zorder=2)
ax_solstice.add_patch(earth_b1)

# Axis of rotation is tilted towards sun (slope = cot(90-tilt) = tan(tilt)) - Correction, slope is cot(tilt)
x_ax = R * np.cos(np.pi/2 - tilt_rad)
y_ax = R * np.sin(np.pi/2 - tilt_rad)
ax_solstice.plot([-x_ax, x_ax], [-y_ax, y_ax], 'k-', lw=2, zorder=3)

# Equator plane is perpendicular to axis (slope = -tan(tilt))
x_eq = R * np.cos(tilt_rad)
y_eq = R * np.sin(tilt_rad)
ax_solstice.plot([-x_eq, x_eq], [y_eq, -y_eq], 'r--', lw=1.5, zorder=4)
ax_solstice.text(-x_eq - 0.15, y_eq - 0.015, "Equator", color='red', ha='right', va='top', rotation=-tilt_deg)

# Syene is at the subsolar point (R, 0), which by definition is on the Tropic of Cancer
syene_solstice_pos = (R, 0)
ax_solstice.plot(*syene_solstice_pos, 'bo', markersize=8, zorder=5)
ax_solstice.annotate('Tropic of Cancer',
                     xy=syene_solstice_pos, xytext=(R + 0.1, 0),
                     ha='left', va='center', color='blue')

ax_solstice.text(0, -1.9, 'Syene on Tropic of Cancer:\nReceives direct sunlight (No Shadow)', 
                 ha='center', va='center', color='blue', fontsize=12)

# --- Equinox Sub-panel (Shadow Corrected) ---
ax_equinox.set_title("Equinox", fontsize=14, pad=5)
setup_earth_ax(ax_equinox)
lat_rad = np.deg2rad(23.5)
earth_b2 = patches.Circle((0, 0), R, facecolor="#fbfbfb", edgecolor='k', linewidth=2, zorder=2)
ax_equinox.add_patch(earth_b2)
ax_equinox.plot([0, 0], [-R, R], 'k-', lw=2, zorder=3)
ax_equinox.plot([-R, R], [0, 0], 'r--', lw=2, zorder=4)
ax_equinox.text(R + 0.2, 0, "Equator", color='red', ha='left', va='center')
y_tropic = R * np.sin(lat_rad)
x_tropic = R * np.cos(lat_rad)
ax_equinox.plot([-x_tropic, x_tropic], [y_tropic, y_tropic], 'b--', lw=1.5, zorder=4)
ax_equinox.text(x_tropic + 0.2, y_tropic, "Tropic of Cancer", color='blue', ha='left', va='center')
syene_equinox_pos = (R * np.cos(lat_rad), R * np.sin(lat_rad))
gnomon_h = 0.15
gnomon_tip = ((R + gnomon_h) * np.cos(lat_rad), (R + gnomon_h) * np.sin(lat_rad))
ax_equinox.plot(*syene_equinox_pos, 'ro', markersize=8, zorder=5)
ax_equinox.plot([syene_equinox_pos[0], gnomon_tip[0]], [syene_equinox_pos[1], gnomon_tip[1]], 'r-', lw=3, zorder=5)
shadow_end_y = gnomon_tip[1]
shadow_end_x = np.sqrt(R**2 - shadow_end_y**2)
ax_equinox.plot([gnomon_tip[0], shadow_end_x], [gnomon_tip[1], shadow_end_y], 'darkred', linestyle='--', dashes=(4,4), lw=1.5, zorder=4)

# FIX: Ensure theta1 < theta2 for patches.Arc to draw a small CCW arc
shadow_angle_start_rad = np.arctan2(shadow_end_y, shadow_end_x)
theta1 = np.rad2deg(lat_rad)
theta2 = np.rad2deg(shadow_angle_start_rad)
shadow_arc = patches.Arc((0,0), 2*R, 2*R, 
                         theta1=theta1, 
                         theta2=theta2, 
                         color='darkred', lw=5, zorder=4)
ax_equinox.add_patch(shadow_arc)

ax_equinox.text(0, -1.9, 'Syene is not aligned with direct sunlight\n(Casts a Shadow)', 
                  ha='center', va='center', color='red', fontsize=12)

# --- Central Explanation Text ---
ax_text.text(0.5, 0.5,
             "The experiment required a location where the Sun was\n"
             r"at the zenith ($\theta=0^\circ$). This only occurs on the" "\n"
             r"Tropic of Cancer ($\phi=23.5^\circ$N) on the one day" "\n"
             "the Earth's tilt maximally faces the Sun:\n"
             "the summer solstice.",
             ha='center', va='center', fontsize=13,
             bbox=dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=1))

# --- Final Figure Touches ---
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("Eratosthenes_Experiment_Final_Corrected.png", dpi=300, bbox_inches='tight')
plt.show()