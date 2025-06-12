import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup (1 row, 2 columns) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), subplot_kw={'projection': '3d'})
fig.suptitle("Evolution of Eratosthenes' Method", fontsize=16, weight='bold')

# --- Function to draw a sphere ---
def draw_sphere(ax, title):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 1 * np.outer(np.cos(u), np.sin(v))
    y = 1 * np.outer(np.sin(u), np.sin(v))
    z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.3, rstride=5, cstride=5, edgecolor='k', linewidth=0.2)
    ax.set_title(title, fontsize=14, pad=15)
    ax.set_box_aspect([1,1,1]) # Aspect ratio is 1:1:1
    ax.axis('off')

# --- SUBPLOT 1: Ancient Method ---
draw_sphere(ax1, "Ancient Method")
# Draw meridian line
z_meridian = np.linspace(-1, 1, 100)
x_meridian = np.sqrt(1 - z_meridian**2)
y_meridian = np.zeros_like(z_meridian)
ax1.plot(x_meridian, y_meridian, z_meridian, 'k--', dashes=(5,5))
# Points on the same meridian
p1_ancient = (np.cos(np.pi/6), 0, np.sin(np.pi/6))
p2_ancient = (np.cos(-np.pi/12), 0, np.sin(-np.pi/12))
ax1.scatter(*p1_ancient, color='red', s=50, label='$P_1$ (Alexandria)')
ax1.scatter(*p2_ancient, color='blue', s=50, label='$P_2$ (Syene)')
ax1.text(p1_ancient[0]*1.1, p1_ancient[1], p1_ancient[2]*1.1, "$P_1$")
ax1.text(p2_ancient[0]*1.1, p2_ancient[1], p2_ancient[2]*1.1, "$P_2$")
ax1.text(0, -1.5, 0, "Constraints:\n• Same Meridian\n• Local Noon Measurement\n• Solstice Day", ha='center')

# --- SUBPLOT 2: Modern Method ---
draw_sphere(ax2, "Modern Generalized Method")
# Arbitrary points
phi1, lam1 = np.pi/4, np.pi/6
p1_modern = (np.cos(phi1)*np.cos(lam1), np.cos(phi1)*np.sin(lam1), np.sin(phi1))
phi2, lam2 = -np.pi/6, np.pi/2
p2_modern = (np.cos(phi2)*np.cos(lam2), np.cos(phi2)*np.sin(lam2), np.sin(phi2))
ax2.scatter(*p1_modern, color='red', s=50)
ax2.scatter(*p2_modern, color='blue', s=50)
ax2.text(p1_modern[0]*1.1, p1_modern[1]*1.1, p1_modern[2]*1.1, "$P_1(\\phi_1, \\lambda_1)$")
ax2.text(p2_modern[0]*1.1, p2_modern[1]*1.1, p2_modern[2]*1.1, "$P_2(\\phi_2, \\lambda_2)$")
# Great circle path
v1 = np.array(p1_modern)
v2 = np.array(p2_modern)
v3 = np.cross(v1, v2)
v3 /= np.linalg.norm(v3)
v4 = np.cross(v3, v1)
t = np.linspace(0, np.arccos(np.dot(v1, v2)), 100)
arc = np.array([v1*np.cos(ti) + v4*np.sin(ti) for ti in t])
ax2.plot(arc[:,0], arc[:,1], arc[:,2], 'r-', linewidth=2, label='Great-Circle Path')
ax2.text(0, -1.5, 0, "Generalizations:\n• Arbitrary Points\n• Universal Time (UTC)\n• Any Day of Year", ha='center')


# --- Final Touches ---
plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig("figure_7_ancient_vs_modern.png", dpi=300)
plt.show()