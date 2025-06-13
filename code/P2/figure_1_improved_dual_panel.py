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
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
fig.suptitle("Eratosthenes' Experiment: Geometric Principle and Temporal Rationale", fontsize=16, weight='bold')

# =============================================================================
# PANEL (a): The Core Geometric Principle (Reoriented)
# =============================================================================
ax1.set_aspect('equal')
ax1.axis('off')
ax1.set_title("(a) The Core Geometric Principle", fontsize=14, pad=10)

# --- Geometric Parameters ---
R = 1.0  # Earth Radius
angle_deg = 7.2
angle_rad = np.deg2rad(angle_deg)

# --- Draw the Earth ---
earth = patches.Circle((0, 0), R, facecolor='#cce6ff', edgecolor='black', linewidth=1.5, zorder=2)
ax1.add_patch(earth)
ax1.plot(0, 0, 'ko', markersize=5) # Center of Earth

# --- Positions of Cities (Top-Down Orientation) ---
syene_pos = (0, R)
alexandria_angle_from_top = np.pi/2 - angle_rad
alexandria_pos = (R * np.cos(alexandria_angle_from_top), R * np.sin(alexandria_angle_from_top))

# --- Draw Gnomons and Radial Lines ---
gnomon_height = 0.15
# Syene Gnomon (at the top)
ax1.plot([syene_pos[0], syene_pos[0]], [syene_pos[1], syene_pos[1] + gnomon_height], 'b-', linewidth=2, zorder=3)
ax1.plot([0, syene_pos[0]], [0, syene_pos[1]], 'k:', dashes=(4,4)) # Radial line
# Alexandria Gnomon
alexandria_gnomon_top = (alexandria_pos[0] * (1 + gnomon_height/R), alexandria_pos[1] * (1 + gnomon_height/R))
ax1.plot([alexandria_pos[0], alexandria_gnomon_top[0]], [alexandria_pos[1], alexandria_gnomon_top[1]], 'b-', linewidth=2, zorder=3)
ax1.plot([0, alexandria_pos[0]], [0, alexandria_pos[1]], 'k:', dashes=(4,4)) # Radial line

# --- Draw Parallel Sun Rays (Vertical) ---
ray_length = 0.8
for x_pos in [-0.5, 0, 0.5]:
    ax1.arrow(x_pos, R + gnomon_height + ray_length, 0, -ray_length,
              head_width=0.04, head_length=0.06, fc='gold', ec='orange', linewidth=1, zorder=1)
# Ray that casts the shadow
ax1.plot([alexandria_pos[0], alexandria_pos[0]], [alexandria_pos[1], alexandria_gnomon_top[1]+0.2],
         '--', color='gold', dashes=(5,5), lw=1.5)

# --- Annotations and Labels ---
# City labels
ax1.text(syene_pos[0], syene_pos[1] + gnomon_height + 0.1, 'Syene', ha='center', va='bottom', fontsize=11, weight='bold')
ax1.text(alexandria_pos[0] + 0.1, alexandria_pos[1] - 0.1, 'Alexandria', ha='left', va='top', fontsize=11, weight='bold')

# Angle labels
# Central angle Δθ
central_arc = patches.Arc((0, 0), 0.8, 0.8, theta1=np.rad2deg(alexandria_angle_from_top), theta2=90, color='k', linestyle='-')
ax1.add_patch(central_arc)
ax1.text(0.2, 0.35, r'$\Delta\theta$', ha='center', va='center', fontsize=14)

# Shadow angle θ
shadow_arc = patches.Arc(alexandria_pos, 0.3, 0.3, theta1=np.rad2deg(alexandria_angle_from_top)-90, theta2=0, color='r', linestyle='-')
ax1.add_patch(shadow_arc)
ax1.text(alexandria_pos[0] - 0.25, alexandria_pos[1] - 0.1, r'$\theta = \Delta\theta$', ha='center', va='center', fontsize=14, color='r')

# Sun's Rays label
ax1.text(0, R + gnomon_height + ray_length + 0.1, "Parallel Sun Rays", ha='center', va='bottom', fontsize=11)
ax1.set_xlim(-1.5, 1.5)
ax1.set_ylim(-1.5, 2.8)


# =============================================================================
# PANEL (b): The Rationale for the Summer Solstice
# =============================================================================
ax2.set_facecolor('#F0F0F0')
ax2.axis('off')
ax2.set_title("(b) The Rationale for the Summer Solstice", fontsize=14, pad=10)

def draw_tilted_earth(ax, y_offset, tilt_deg, title):
    # Earth
    earth = patches.Circle((0, y_offset), 1.0, facecolor='lightblue', edgecolor='k', alpha=0.6, zorder=2)
    ax.add_patch(earth)
    ax.text(0, y_offset + 1.2, title, ha='center', weight='bold')
    
    # Axis and Equator
    tilt_rad = np.deg2rad(tilt_deg)
    ax.plot([np.sin(tilt_rad), -np.sin(tilt_rad)], 
            [y_offset - np.cos(tilt_rad), y_offset + np.cos(tilt_rad)], 'k-', lw=1.5)
    equator = patches.Ellipse((0, y_offset), 2.0, 2*np.sin(tilt_rad), angle=0, facecolor='none', edgecolor='r', ls='--', lw=1.5)
    ax.add_patch(equator)

    # Sun's Rays (coming from the right)
    for y_ray in np.linspace(-0.8, 0.8, 4):
        ax.arrow(2.5, y_offset + y_ray, -1.2, 0, head_width=0.08, head_length=0.1, fc='gold', ec='orange', zorder=1)

# --- Mini-Diagram 1: Summer Solstice ---
draw_tilted_earth(ax2, 1.8, 23.5, "Summer Solstice")
# Syene on Tropic of Cancer (23.5 N) is directly under the sun
syene_x_solstice = np.cos(np.deg2rad(23.5))
syene_y_solstice = 1.8 + np.sin(np.deg2rad(23.5))
ax2.plot(syene_x_solstice, syene_y_solstice, 'bo', markersize=6)
ax2.plot([syene_x_solstice, 0.3], [syene_y_solstice, syene_y_solstice], 'b--')
ax2.text(syene_x_solstice, syene_y_solstice + 0.15, "Syene: No Shadow\n($\\theta=0^\circ$)", ha='center', va='bottom', color='blue')


# --- Mini-Diagram 2: Equinox ---
draw_tilted_earth(ax2, -1.8, 0, "Equinox") # No tilt relative to sun
# Syene is at 23.5 N latitude, but sun is over equator
syene_x_equinox = np.cos(np.deg2rad(23.5))
syene_y_equinox = -1.8 + np.sin(np.deg2rad(23.5))
ax2.plot(syene_x_equinox, syene_y_equinox, 'ro', markersize=6)
# Show shadow
ax2.plot([syene_x_equinox-0.3, syene_x_equinox], [syene_y_equinox, syene_y_equinox], 'r-', lw=4)
ax2.text(syene_x_equinox, syene_y_equinox + 0.15, "Syene: Has a Shadow\n($\\theta=23.5^\circ$)", ha='center', va='bottom', color='red')

# --- Explanation Text ---
ax2.text(0, 0,
         "The experiment required a location where the Sun was\n"
         "at the zenith ($0^\\circ$ shadow angle). This only occurs\n"
         "on the Tropic of Cancer ($\phi = 23.5^\\circ$N) on the\n"
         "day the Earth's tilt maximally faces the Sun:\n"
         "the summer solstice.",
         ha='center', va='center', bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="black"))
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3.5, 3.5)

# --- Final Touches ---
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("figure_1_improved_dual_panel.png", dpi=300)
plt.show()