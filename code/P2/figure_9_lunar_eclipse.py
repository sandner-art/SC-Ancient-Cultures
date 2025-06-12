import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('black') # Space background

# --- Draw the Moon ---
moon = patches.Circle((0, 0), 1.0, facecolor='#DDDDDD', edgecolor='gray', zorder=2)
ax.add_patch(moon)
ax.text(0, 0, 'The Moon', ha='center', va='center', color='black', fontsize=14, weight='bold')

# --- Draw the Earth's Shadow (Umbra) ---
# The shadow is cast by a larger body, so its edge has a larger radius of curvature
# We can simulate this with a large circle patch partially overlapping
shadow = patches.Circle((-2.5, 0), 2.0, facecolor='black', alpha=0.7, zorder=3)
ax.add_patch(shadow)

# --- Annotations ---
# Arrow pointing to the curved shadow edge
ax.annotate("Earth's circular shadow", xy=(-0.5, 0.6), xytext=(-2, 1.5),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0.2", color='white', lw=1.5),
            ha='center', va='bottom', fontsize=12, color='white',
            bbox=dict(boxstyle="round,pad=0.3", fc="black", ec="white", lw=1))

# Concluding text
ax.text(0, -1.5,
        "Aristotle's observation:\nA circular shadow is cast only by a spherical object,\n"
        "regardless of its orientation.",
        ha='center', va='center', fontsize=12, color='white', wrap=True)

# --- Final Touches ---
ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 2.5)
ax.set_title("Key Evidence for a Spherical Earth: The Lunar Eclipse", fontsize=16, weight='bold', color='white', pad=20)
plt.tight_layout()
plt.savefig("figure_9_lunar_eclipse.png", dpi=300, facecolor='black')
plt.show()