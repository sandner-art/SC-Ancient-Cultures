import matplotlib.pyplot as plt
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup (1 row, 3 columns) ---
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle("Shadow Behavior on Worlds with Different Geometries", fontsize=16, weight='bold')

def setup_ax(ax, title, curvature_label):
    ax.axis('off')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-0.2, 1)
    ax.set_title(title, fontsize=14)
    ax.text(0, -0.15, curvature_label, ha='center', fontsize=12, style='italic')

def draw_gnomon_and_shadow(ax, base_x, surface_y, ray_slope, gnomon_h=0.3):
    gnomon_base = (base_x, surface_y)
    gnomon_top = (base_x, surface_y + gnomon_h)
    ax.plot([base_x, base_x], [surface_y, gnomon_top[1]], 'b-', lw=2) # Gnomon
    
    # Shadow calculation
    shadow_end_x = base_x + (surface_y - gnomon_top[1]) / ray_slope
    ax.plot([base_x, shadow_end_x], [surface_y, surface_y], 'r-', lw=3) # Shadow
    
    # Sun ray
    ax.plot([shadow_end_x, gnomon_top[0]], [surface_y, gnomon_top[1]], '--', color='gold', lw=1.5)
    return shadow_end_x - base_x

# --- Panel 1: Spherical (Positive Curvature) ---
setup_ax(ax1, 'Spherical Planet', 'Positive Curvature')
x = np.linspace(-1, 1, 100)
y = -0.5 * x**2 + 0.5 # Curved surface
ax1.plot(x, y, 'k')
draw_gnomon_and_shadow(ax1, -0.6, -0.5*(-0.6)**2+0.5, ray_slope=-1.5)
s2 = draw_gnomon_and_shadow(ax1, 0.6, -0.5*(0.6)**2+0.5, ray_slope=-1.5)
ax1.text(0, 0.8, 'Shadow lengthens\nnon-linearly', ha='center', color='red')

# --- Panel 2: Flat Plane (Zero Curvature) ---
setup_ax(ax2, 'Flat Planet', 'Zero Curvature')
ax2.plot([-1, 1], [0.1, 0.1], 'k') # Flat surface
# For a local sun, rays diverge
sun_pos = (0, 3)
draw_gnomon_and_shadow(ax2, -0.6, 0.1, ray_slope=(0.1 - sun_pos[1])/(-0.6-sun_pos[0]))
draw_gnomon_and_shadow(ax2, 0.6, 0.1, ray_slope=(0.1 - sun_pos[1])/(0.6-sun_pos[0]))
ax2.plot(sun_pos[0], sun_pos[1], 'o', color='gold', markersize=15)
ax2.text(sun_pos[0], sun_pos[1]+0.1, "Local Sun")
ax2.text(0, 0.8, 'Shadow lengthens\nlinearly', ha='center', color='red')


# --- Panel 3: Hyperbolic (Negative Curvature) ---
setup_ax(ax3, 'Hyperbolic Planet', 'Negative Curvature')
x = np.linspace(-1, 1, 100)
y = 0.5 * x**2 # "Saddle" shape cross-section
ax3.plot(x, y, 'k')
draw_gnomon_and_shadow(ax3, -0.6, 0.5*(-0.6)**2, ray_slope=-1.5)
s2_hyp = draw_gnomon_and_shadow(ax3, 0.6, 0.5*(0.6)**2, ray_slope=-1.5)
ax3.text(0, 0.8, 'Shadow lengthens\nsuper-linearly', ha='center', color='red')

# --- Final Touches ---
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig("figure_12_hypothetical_geometries.png", dpi=300)
plt.show()