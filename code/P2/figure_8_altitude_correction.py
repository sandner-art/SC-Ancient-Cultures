import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')

# --- Geometric Elements ---
center = (0, 0)
R_sea = 1.0
h_avg = 0.2
R_h = R_sea + h_avg
angle_subtended_deg = 60
angle_rad = np.deg2rad(angle_subtended_deg)

# Draw sea-level arc
arc_sea = patches.Arc(center, 2*R_sea, 2*R_sea, theta1=90-angle_subtended_deg/2, theta2=90+angle_subtended_deg/2, 
                      color='navy', linewidth=2.5, label='Sea-level Arc ($d_{sea}$)')
ax.add_patch(arc_sea)

# Draw ground-level arc
arc_ground = patches.Arc(center, 2*R_h, 2*R_h, theta1=90-angle_subtended_deg/2, theta2=90+angle_subtended_deg/2, 
                         color='saddlebrown', linewidth=2.5, label='Ground Arc ($d_{ground}$)')
ax.add_patch(arc_ground)

# Draw radial lines from center
p1_angle = np.deg2rad(90-angle_subtended_deg/2)
p2_angle = np.deg2rad(90+angle_subtended_deg/2)
ax.plot([0, R_h * np.cos(p1_angle)], [0, R_h * np.sin(p1_angle)], 'k--', dashes=(5,5))
ax.plot([0, R_h * np.cos(p2_angle)], [0, R_h * np.sin(p2_angle)], 'k--', dashes=(5,5))
ax.plot(0, 0, 'ko', markersize=6, label="Earth's Center")

# --- Annotations ---
# Radii and Altitude
ax.plot([0, 0], [0, R_sea], 'k-')
ax.plot([0, 0], [R_sea, R_h], 'r-')
ax.text(0.1, R_sea/2, '$R_{sea}$', ha='left', va='center', fontsize=14)
ax.text(0.1, R_sea + h_avg/2, '$h_{avg}$', ha='left', va='center', fontsize=14, color='red')

# Central angle
arc_center = patches.Arc(center, 0.5, 0.5, theta1=90-angle_subtended_deg/2, theta2=90+angle_subtended_deg/2, color='gray')
ax.add_patch(arc_center)
ax.text(0, 0.6, '$c$', ha='center', va='center', fontsize=14)

# Arc labels
ax.text(0.7, 1.1, '$d_{ground}$', ha='center', va='center', color='saddlebrown', fontsize=12, weight='bold')
ax.text(0.6, 0.9, '$d_{sea}$', ha='center', va='center', color='navy', fontsize=12, weight='bold')

# --- Final Touches ---
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-0.2, 1.5)
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.05))
ax.set_title("Geometric Basis for Observer Altitude Correction", fontsize=16, weight='bold')

plt.tight_layout()
plt.savefig("figure_8_altitude_correction.png", dpi=300)
plt.show()