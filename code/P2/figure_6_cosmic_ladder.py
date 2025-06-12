import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(12, 7))
ax.set_aspect('equal')
ax.axis('off')
ax.set_xlim(-1, 20)
ax.set_ylim(-5, 5)

# --- Define celestial bodies ---
# Earth
earth_pos = (0, 0)
earth_radius = 1.0
earth = patches.Circle(earth_pos, earth_radius, facecolor='#6699CC', edgecolor='black', zorder=3)
ax.add_patch(earth)
ax.text(earth_pos[0], earth_pos[1] - earth_radius - 0.5, 'Earth', ha='center', weight='bold')

# Moon
moon_pos = (8, 0)
moon_radius = 0.27 # Relative size
moon = patches.Circle(moon_pos, moon_radius, facecolor='#B0B0B0', edgecolor='black', zorder=3)
ax.add_patch(moon)
ax.text(moon_pos[0], moon_pos[1] - moon_radius - 0.5, 'Moon', ha='center', weight='bold')

# Sun
sun_pos = (18, 0) # Not to scale distance-wise, but indicates farther
sun_radius = 2.0
sun = patches.Circle(sun_pos, sun_radius, facecolor='gold', edgecolor='orange', zorder=2)
ax.add_patch(sun)
ax.text(sun_pos[0], sun_pos[1] - sun_radius - 0.5, 'Sun', ha='center', weight='bold')

# --- Draw distance lines and annotations ---
# Step 1: Measure Earth's Radius
ax.plot([earth_pos[0], earth_pos[0]], [0, earth_radius], 'r-', linewidth=2)
ax.text(earth_pos[0] + 0.2, earth_radius / 2, '$R_{Earth}$', va='center', ha='left', color='red', fontsize=14)
ax.annotate('Step 1: Measure Earth\n(Eratosthenes)', xy=(0, 1.2), xytext=(-1, 3),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
            ha='center', va='bottom', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="ivory", ec="gray", lw=1))

# Step 2: Calculate Moon's Distance
ax.plot([earth_pos[0], moon_pos[0]], [2, 2], 'k-')
ax.plot([earth_pos[0], earth_pos[0]], [1.8, 2.2], 'k-')
ax.plot([moon_pos[0], moon_pos[0]], [1.8, 2.2], 'k-')
ax.text(4, 2.3, r'$D_{Moon} \approx 60 \times R_{Earth}$', ha='center', fontsize=12)
ax.annotate('Step 2: Calculate Moon\'s Distance\n(Aristarchus\'s method)', xy=(4, 2), xytext=(4, 4),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
            ha='center', va='bottom', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="ivory", ec="gray", lw=1))
            
# Step 3: Estimate Sun's Distance
ax.plot([moon_pos[0], sun_pos[0]], [-3, -3], 'k-')
ax.plot([moon_pos[0], moon_pos[0]], [-3.2, -2.8], 'k-')
ax.plot([sun_pos[0], sun_pos[0]], [-3.2, -2.8], 'k-')
ax.text(13, -2.7, r'$D_{Sun} \approx 19 \times D_{Moon}$', ha='center', fontsize=12)
ax.annotate('Step 3: Estimate Sun\'s Distance\n(Aristarchus\'s method)', xy=(13, -3), xytext=(13, -4.5),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
            ha='center', va='top', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="ivory", ec="gray", lw=1))

# --- Final Touches ---
ax.set_title("Eratosthenes' Result as the First Rung on the Cosmic Distance Ladder", fontsize=16, weight='bold', pad=20)
plt.tight_layout()
plt.savefig("figure_6_cosmic_ladder.png", dpi=300)
plt.show()