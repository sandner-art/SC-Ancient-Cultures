import matplotlib.pyplot as plt
import numpy as np

# --- Setup for Professional Publication Quality ---
plt.style.use('seaborn-v0_8-paper')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 14

# --- Data from Table 3 (using upper bounds for clarity) ---
sources = [
    'Altitude Difference', 
    'Meridian Alignment', 
    'Angle ($\Delta\\theta$)', 
    'Distance ($d$)'
]
errors = [0.1, 1.0, 4.0, 15.0] # Using max plausible percentage error
colors = ['#AAAAAA', '#AAAAAA', '#AAAAAA', '#CC3311']

# --- Figure and Axis Setup ---
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(sources, errors, color=colors)

# --- Annotations and Labels ---
ax.set_xlabel('Resulting Error in Circumference Calculation (%)')
ax.set_title("Dominance of Distance Uncertainty in the Ancient Experiment", fontsize=16, weight='bold')
ax.invert_yaxis() # Puts the most significant error source at the top

# Add value labels to the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 0.2
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width}%', 
            va='center', fontsize=12)

# Highlight the main source of error
ax.text(errors[-1] / 2, len(sources) - 0.9, 'Dominant Error Source',
        ha='center', va='center', color='white', weight='bold', fontsize=12)

# --- Final Touches ---
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(0, 17) # Give space for labels
plt.tight_layout()
plt.savefig("figure_11_error_budget.png", dpi=300)
plt.show()