import matplotlib.pyplot as plt
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup (1 row, 2 columns) ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
fig.suptitle("Falsifiability: The Power of a Third Measurement Point", fontsize=16, weight='bold')

# --- Generate "True" Data from a Spherical World ---
true_phi = np.array([15, 50, 70])
true_s = np.tan(np.deg2rad(true_phi))
phi_range = np.linspace(0, 80, 100)

# --- PANEL 1: Two-Point Measurement (Ambiguous) ---
ax1.set_title("Two-Point Measurement: Ambiguous", fontsize=14)
# Plot the two data points
ax1.scatter(true_phi[:2], true_s[:2], color='black', s=80, zorder=10)

# Plot the spherical curve that fits them
s_spherical = np.tan(np.deg2rad(phi_range))
ax1.plot(phi_range, s_spherical, color='#003366', lw=2, label='Spherical Model Fit')

# Plot the flat-earth line that fits them
# Fit a line: y = mx + c (c is 0 for flat model from subsolar point)
m = (true_s[1] - true_s[0]) / (true_phi[1] - true_phi[0])
s_flat = m * phi_range
# A slightly better fit for a line that doesn't go through 0,0
z = np.polyfit(true_phi[:2], true_s[:2], 1)
p = np.poly1d(z)
ax1.plot(phi_range, p(phi_range), color='#CC3311', ls='--', lw=2, label='Flat Model Fit')

ax1.text(40, 1.5, "With only two points,\nboth models are equally valid.", ha='center',
         bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", lw=1))
ax1.legend()
ax1.set_xlabel('Latitude $\\phi$ (degrees)')
ax1.set_ylabel('Shadow Length / Gnomon Height ($s/h$)')


# --- PANEL 2: Three-Point Measurement (Decisive) ---
ax2.set_title("Three-Point Measurement: Decisive", fontsize=14)
# Plot all three points
ax2.scatter(true_phi, true_s, color='black', s=80, zorder=10)

# Plot the same curves from Panel 1
ax2.plot(phi_range, s_spherical, color='#003366', lw=2, label='Spherical Model (Confirmed)')
ax2.plot(phi_range, p(phi_range), color='#CC3311', ls='--', lw=2, label='Flat Model (Falsified)')

# Annotate the failure of the flat model
ax2.annotate('Third point is missed\nby the linear model',
             xy=(true_phi[2], true_s[2]),
             xytext=(45, 0.45),
             arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6, connectionstyle="arc3,rad=0.3"),
             ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=1))
ax2.legend()
ax2.set_xlabel('Latitude $\\phi$ (degrees)')

# --- Final Touches for Both Panels ---
for ax in [ax1, ax2]:
    ax.grid(True, which='both', linestyle=':', linewidth=0.5)
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 3.0)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("figure_14_twopoint_vs_threepoint.png", dpi=300)
plt.show()