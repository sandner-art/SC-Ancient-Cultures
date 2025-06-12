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
plt.rcParams['legend.fontsize'] = 10

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off') # Hide the axes for a clean diagram

# --- Geometric Parameters ---
R = 1.0  # Earth Radius
angle_deg = 7.2
angle_rad = np.deg2rad(angle_deg)

# --- Draw the Earth ---
earth = patches.Circle((0, 0), R, facecolor='#cce6ff', edgecolor='black', linewidth=1.5, zorder=2)
ax.add_patch(earth)
ax.plot(0, 0, 'ko', markersize=5) # Center of Earth

# --- Positions of Cities ---
# Syene (on the Tropic of Cancer, so sun is at zenith)
syene_angle = -np.pi / 2
syene_pos = (R * np.cos(syene_angle), R * np.sin(syene_angle))

# Alexandria (north of Syene by 7.2 degrees)
alexandria_angle = syene_angle + angle_rad
alexandria_pos = (R * np.cos(alexandria_angle), R * np.sin(alexandria_angle))

# --- Draw Gnomons (Vertical Rods) ---
gnomon_height = 0.15
# Syene Gnomon
ax.plot([syene_pos[0], syene_pos[0] * (1 + gnomon_height)], 
        [syene_pos[1], syene_pos[1] * (1 + gnomon_height)], 'b-', linewidth=2, zorder=3)
# Alexandria Gnomon
alexandria_gnomon_base = alexandria_pos
alexandria_gnomon_top = (alexandria_pos[0] * (1 + gnomon_height), alexandria_pos[1] * (1 + gnomon_height))
ax.plot([alexandria_gnomon_base[0], alexandria_gnomon_top[0]],
        [alexandria_gnomon_base[1], alexandria_gnomon_top[1]], 'b-', linewidth=2, zorder=3, label='Gnomon')

# --- Draw Parallel Sun Rays ---
ray_length = 1.5
# Ray to Syene (no shadow)
ax.arrow(syene_pos[0] + ray_length, syene_pos[1], -ray_length, 0,
         head_width=0.03, head_length=0.05, fc='gold', ec='orange', linewidth=1, zorder=1)
# Ray to Alexandria (casts a shadow)
shadow_end_y = alexandria_gnomon_base[1] + gnomon_height * np.tan(angle_rad)
ax.arrow(alexandria_gnomon_top[0] + ray_length, alexandria_gnomon_top[1], -ray_length, 0,
         head_width=0.03, head_length=0.05, fc='gold', ec='orange', linewidth=1, zorder=1)
# Dashed line showing the ray path creating the shadow
ax.plot([alexandria_gnomon_top[0], alexandria_gnomon_base[0] - gnomon_height*np.sin(angle_rad)/np.cos(angle_rad)], 
        [alexandria_gnomon_top[1], alexandria_gnomon_base[1]], 'r--', dashes=(5, 5), linewidth=1, zorder=3)
# Shadow on the ground
ax.plot([alexandria_gnomon_base[0], alexandria_gnomon_base[0] - gnomon_height*np.sin(angle_rad)/np.cos(angle_rad)], 
        [alexandria_gnomon_base[1], alexandria_gnomon_base[1]], 'r-', linewidth=3, zorder=3)


# --- Annotations and Labels ---
# City labels
ax.text(syene_pos[0], syene_pos[1] - 0.1, 'Syene\n(Sun at Zenith)', ha='center', va='top', fontsize=10, weight='bold')
ax.text(alexandria_pos[0] + 0.1, alexandria_pos[1] + 0.1, 'Alexandria', ha='left', va='center', fontsize=10, weight='bold')

# Angle labels
# Central angle
central_arc = patches.Arc((0, 0), 0.5, 0.5, theta1=np.rad2deg(syene_angle), theta2=np.rad2deg(alexandria_angle),
                          color='k', linestyle='--', linewidth=1)
ax.add_patch(central_arc)
ax.text(0.35 * np.cos(syene_angle + angle_rad / 2), 0.35 * np.sin(syene_angle + angle_rad / 2),
        r'$\Delta\theta$', ha='center', va='center', fontsize=14)

# Shadow angle (alternate interior angle)
shadow_arc = patches.Arc(alexandria_gnomon_top, 0.2, 0.2, theta1=180, theta2=180 + angle_deg,
                         color='k', linestyle='--', linewidth=1)
ax.add_patch(shadow_arc)
ax.text(alexandria_gnomon_top[0] - 0.15, alexandria_gnomon_top[1] + 0.05,
        r'$\theta \approx 7.2^\circ$', ha='center', va='center', fontsize=14)

# Sun's Rays label
ax.text(1.3, 0.2, "Sun's Rays\n(Assumed Parallel)", ha='center', va='bottom', fontsize=10)

# --- Final Touches ---
ax.set_xlim(-1.2, 1.6)
ax.set_ylim(-1.2, 1.2)
plt.title("Geometric Principle of Eratosthenes' Experiment", fontsize=14, weight='bold')
plt.savefig("figure_1_experiment_geometry.png", dpi=300, bbox_inches='tight')
plt.show()