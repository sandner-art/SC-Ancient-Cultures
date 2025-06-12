import matplotlib.pyplot as plt
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 12

# --- Figure and Axis Setup ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.axis('off')

# --- Step 1: Raw Data (Bematist Survey) ---
ax.text(0.1, 0.9, "Step 1: Raw Data", ha='center', fontsize=14, weight='bold')
# Winding Path
y = np.linspace(0, 5, 100)
x = 0.5 * np.sin(y * 2) + 1
ax.plot(x, y, color='#0066CC', lw=3, label="Bematist's Path")
ax.text(1.5, 2.5, "Raw Survey Data:\n5,000 Stadia\n(likely Attic Stadia)", ha='left',
        bbox=dict(boxstyle="round,pad=0.3", fc="lightblue", alpha=0.5))

# --- Step 2: Geographer's Knowledge ---
ax.text(0.5, 0.6, "Step 2: Cartographic Knowledge", ha='center', fontsize=14, weight='bold')
# Stylized Map/Grid
for i in np.linspace(0, 1, 6):
    ax.axhline(i*5, color='gray', ls=':', xmin=0.35, xmax=0.75)
    ax.axvline(i*3, color='gray', ls=':', ymin=0.1, ymax=0.8)
ax.text(1.5, 0.2, "Eratosthenes, as a geographer,\nknows the path is not a straight\nNorth-South line.",
        ha='center', bbox=dict(boxstyle="round,pad=0.3", fc="lightgoldenrodyellow", alpha=0.5))

# --- Step 3: The Correction ---
ax.text(0.8, 0.35, "Step 3: The Scientific Correction", ha='center', fontsize=14, weight='bold')
# Projection Lines
for y_val in np.linspace(0.5, 4.5, 8):
    x_val = 0.5 * np.sin(y_val * 2) + 1
    ax.plot([x_val, 3.0], [y_val, y_val], 'r--', dashes=(2, 2), lw=0.8)
# Arrow showing the process
ax.annotate("", xy=(2.8, 2.5), xytext=(2.2, 2.5),
            arrowprops=dict(arrowstyle="->", color='red', lw=2))
ax.text(2.5, 2.8, "Projection\nonto Meridian", ha='center', color='red')


# --- Step 4: Corrected Geometric Distance ---
ax.text(0.8, 0.1, "Step 4: Refined Data for Calculation", ha='center', fontsize=14, weight='bold')
# The "corrected" straight line
ax.plot([3.0, 3.0], [0, 5], color='red', lw=3, label="Corrected Geometric Distance")
ax.text(3.5, 2.5, "Corrected Distance:\n~4,250 Stadia\n(a geometrically plausible value)", ha='left',
        bbox=dict(boxstyle="round,pad=0.3", fc="lightcoral", alpha=0.5))

# --- Final Touches ---
ax.set_xlim(-1, 5)
ax.set_ylim(-0.5, 6.5)
fig.suptitle("Visualizing the 'Informed Scientific Correction' Hypothesis", fontsize=16, weight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("figure_13_scientific_correction.png", dpi=300)
plt.show()