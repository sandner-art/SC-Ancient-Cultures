import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Ellipse, Rectangle, Circle, Polygon
from matplotlib.path import Path
import matplotlib.patches as mpatches

# --- Publication-Quality Setup ---
plt.style.use('default')
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Computer Modern Roman', 'Times New Roman', 'DejaVu Serif'],
    'mathtext.fontset': 'cm',
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.titlesize': 14,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'axes.linewidth': 0.8,
    'grid.linewidth': 0.5,
    'lines.linewidth': 1.0,
    'patch.linewidth': 0.8,
    'text.usetex': False,
})

# Professional color palette (colorblind-friendly)
colors = {
    'primary': '#2E86AB',      # Professional blue
    'secondary': '#A23B72',    # Magenta
    'accent': '#F18F01',       # Orange
    'neutral': '#C73E1D',      # Red
    'light_blue': '#A8DADC',   # Light blue
    'light_gray': '#F1FAEE',   # Very light gray
    'dark_gray': '#457B9D',    # Dark blue-gray
    'text': '#1D3557'          # Dark blue for text
}

# Calculate precise cubit value
L = np.pi / 6  # Royal cubit in meters
L_cm = L * 100  # Convert to cm for display

# --- Create Figure with Manual Layout Control ---
fig = plt.figure(figsize=(13, 11))

# Define precise subplot positions to avoid overlaps
# [left, bottom, width, height] in figure coordinates
subplot_positions = {
    'top_left': [0.08, 0.55, 0.38, 0.32],      # Panel A
    'top_right': [0.54, 0.55, 0.38, 0.32],     # Panel B  
    'bottom_left': [0.08, 0.15, 0.38, 0.32],   # Panel C
    'bottom_right': [0.54, 0.15, 0.38, 0.32],  # Panel D
}

# Main title with proper spacing
fig.suptitle(r'Unified Dimensional Framework: Royal Cubit System ($L = \pi/6$ m)', 
             fontsize=16, fontweight='bold', y=0.95, color=colors['text'])

# --- Panel A: Areal Dimension (2D) ---
ax1 = fig.add_axes(subplot_positions['top_left'])
ax1.set_title('A. Areal Dimension', fontweight='bold', pad=12, color=colors['text'])

# Draw precise square with professional styling
square_size = 0.55
square_x, square_y = 0.225, 0.3
square = Rectangle((square_x, square_y), square_size, square_size, 
                  facecolor=colors['light_blue'], edgecolor=colors['primary'], 
                  linewidth=2, alpha=0.8)
ax1.add_patch(square)

# Add dimension lines with professional styling
# Horizontal dimension
ax1.annotate('', xy=(square_x + square_size + 0.04, square_y), 
            xytext=(square_x + square_size + 0.04, square_y + square_size),
            arrowprops=dict(arrowstyle='<->', color=colors['dark_gray'], lw=1.5))
ax1.text(square_x + square_size + 0.07, square_y + square_size/2, r'$L$', 
         rotation=90, va='center', ha='left', fontsize=12, color=colors['text'])

# Vertical dimension
ax1.annotate('', xy=(square_x, square_y - 0.04), 
            xytext=(square_x + square_size, square_y - 0.04),
            arrowprops=dict(arrowstyle='<->', color=colors['dark_gray'], lw=1.5))
ax1.text(square_x + square_size/2, square_y - 0.07, r'$L$', 
         ha='center', va='top', fontsize=12, color=colors['text'])

# Mathematical expression with proper positioning
area_value = L**2
ax1.text(0.5, 0.08, f'$A = L^2 = {area_value:.3f}$ m²\n$= {area_value*10000:.0f}$ cm²', 
         transform=ax1.transAxes, ha='center', va='bottom', fontsize=10,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=colors['light_gray'], 
                  edgecolor=colors['primary'], alpha=0.9))

ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.set_aspect('equal')
ax1.axis('off')

# --- Panel B: Cubic Volume (3D) ---
ax2 = fig.add_axes(subplot_positions['top_right'])
ax2.set_title('B. Cubic Volume', fontweight='bold', pad=12, color=colors['text'])

# Draw isometric cube with proper perspective
def draw_isometric_cube(ax, center, size, color_face, color_edge):
    x0, y0 = center
    s = size
    
    # Improved isometric projection with 30-degree angles
    # Front face vertices
    front = np.array([[x0-s/2, y0-s/2], [x0+s/2, y0-s/2], 
                     [x0+s/2, y0+s/2], [x0-s/2, y0+s/2]])
    
    # Back face with proper isometric offset (30° projection)
    offset_x, offset_y = s*0.35, s*0.35  # Better 3D effect
    back = front + [offset_x, offset_y]
    
    # Draw back edges first (hidden line style)
    for i in range(4):
        j = (i+1) % 4
        ax.plot([back[i,0], back[j,0]], [back[i,1], back[j,1]], 
                color=color_edge, linewidth=1, alpha=0.4, linestyle='--')
    
    # Draw connecting edges (depth lines)
    for i in range(4):
        ax.plot([front[i,0], back[i,0]], [front[i,1], back[i,1]], 
                color=color_edge, linewidth=1.5, alpha=0.6)
    
    # Draw faces with proper z-ordering
    # Right face (highest z-order for visibility)
    right = np.array([[x0+s/2, y0-s/2], [x0+s/2+offset_x, y0-s/2+offset_y], 
                     [x0+s/2+offset_x, y0+s/2+offset_y], [x0+s/2, y0+s/2]])
    right_patch = Polygon(right, facecolor=color_face, edgecolor=color_edge, 
                         linewidth=1.5, alpha=0.6, zorder=1)
    ax.add_patch(right_patch)
    
    # Top face
    top = np.array([[x0-s/2, y0+s/2], [x0+s/2, y0+s/2], 
                   [x0+s/2+offset_x, y0+s/2+offset_y], [x0-s/2+offset_x, y0+s/2+offset_y]])
    top_patch = Polygon(top, facecolor=color_face, edgecolor=color_edge, 
                       linewidth=1.5, alpha=0.8, zorder=2)
    ax.add_patch(top_patch)
    
    # Front face (most visible)
    front_patch = Polygon(front, facecolor=color_face, edgecolor=color_edge, 
                         linewidth=2, alpha=0.9, zorder=3)
    ax.add_patch(front_patch)

draw_isometric_cube(ax2, (0.5, 0.55), 0.4, colors['light_blue'], colors['primary'])

# Add dimension label with better positioning
ax2.text(0.25, 0.4, r'$L$', fontsize=12, ha='center', va='center', 
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.9))

# Mathematical expression
volume_cube = L**3
ax2.text(0.5, 0.08, f'$V_{{\\mathrm{{cube}}}} = L^3 = {volume_cube:.4f}$ m³\n$= {volume_cube*1000000:.0f}$ cm³', 
         transform=ax2.transAxes, ha='center', va='bottom', fontsize=10,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=colors['light_gray'], 
                  edgecolor=colors['primary'], alpha=0.9))

ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.set_aspect('equal')
ax2.axis('off')

# --- Panel C: Spherical Volume ---
ax3 = fig.add_axes(subplot_positions['bottom_left'])
ax3.set_title('C. Spherical Volume', fontweight='bold', pad=12, color=colors['text'])

# Sphere from circumference constraint
radius = L / (2 * np.pi)  # If circumference = L, then r = L/(2π)

# Draw sphere with enhanced 3D indication
center_sphere = (0.5, 0.55)
sphere = Circle(center_sphere, 0.22, facecolor=colors['accent'], 
               edgecolor=colors['neutral'], linewidth=2, alpha=0.8)
ax3.add_patch(sphere)

# Add multiple ellipses for better 3D sphere representation
ellipse1 = Ellipse(center_sphere, 0.44, 0.08, facecolor='none', 
                  edgecolor=colors['neutral'], linewidth=1.5, alpha=0.9)
ax3.add_patch(ellipse1)
ellipse2 = Ellipse((center_sphere[0], center_sphere[1]-0.02), 0.3, 0.06, facecolor='none', 
                  edgecolor=colors['neutral'], linewidth=1, alpha=0.7)
ax3.add_patch(ellipse2)
ellipse3 = Ellipse((center_sphere[0], center_sphere[1]+0.02), 0.35, 0.07, facecolor='none', 
                  edgecolor=colors['neutral'], linewidth=1, alpha=0.6)
ax3.add_patch(ellipse3)
ax3.add_patch(ellipse2)

# Add circumference indication with better spacing
ax3.annotate('', xy=(center_sphere[0] + 0.22, center_sphere[1]), 
            xytext=(center_sphere[0] - 0.22, center_sphere[1]),
            arrowprops=dict(arrowstyle='<->', color=colors['dark_gray'], lw=1.5))
ax3.text(center_sphere[0], center_sphere[1] + 0.05, r'$c = L$', 
         ha='center', va='bottom', fontsize=11, color=colors['text'])

# Mathematical expressions with proper spacing
volume_sphere = (L**3) / (6 * np.pi**2)

ax3.text(0.5, 0.08, f'$V_{{\\mathrm{{sphere}}}} = \\frac{{c^3}}{{6\\pi^2}} = {volume_sphere:.4f}$ m³\n' + 
         f'$= {volume_sphere*1000000:.0f}$ cm³', 
         transform=ax3.transAxes, ha='center', va='bottom', fontsize=10,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=colors['light_gray'], 
                  edgecolor=colors['accent'], alpha=0.9))

ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)
ax3.set_aspect('equal')
ax3.axis('off')

# --- Panel D: Dimensional Relationships ---
ax4 = fig.add_axes(subplot_positions['bottom_right'])
ax4.set_title('D. Dimensional Ratios', fontweight='bold', pad=12, color=colors['text'])

# Professional ratio visualization
ratio_sphere_cube = volume_sphere / volume_cube

# Create a clean comparison
y_pos = [0.7, 0.3]
volumes_scaled = [volume_sphere * 1e6, volume_cube * 1e6]  # Convert to cm³
colors_bars = [colors['accent'], colors['primary']]
labels = ['Sphere', 'Cube']

# Horizontal bar chart for better space usage
bars = ax4.barh(y_pos, volumes_scaled, color=colors_bars, alpha=0.7, 
                edgecolor=[colors['neutral'], colors['primary']], linewidth=1.5, height=0.15)

# Add value labels
for i, (bar, value, label) in enumerate(zip(bars, volumes_scaled, labels)):
    width = bar.get_width()
    ax4.text(width + width*0.02, bar.get_y() + bar.get_height()/2,
             f'{value:.2f} cm³', ha='left', va='center', fontsize=9)
    ax4.text(-width*0.02, bar.get_y() + bar.get_height()/2,
             label, ha='right', va='center', fontsize=10, fontweight='bold')

ax4.set_xlabel('Volume (cm³)', fontsize=10, color=colors['text'])
ax4.tick_params(axis='both', colors=colors['text'])
ax4.set_ylim(0, 1)

# Add ratio information with better positioning
ax4.text(0.5, 0.15, f'Ratio: $\\frac{{V_{{\\mathrm{{sphere}}}}}}{{V_{{\\mathrm{{cube}}}}}} = \\frac{{1}}{{6\\pi^2}}$\n' +
         f'$= {ratio_sphere_cube:.4f} = \\frac{{1}}{{{1/ratio_sphere_cube:.1f}}}

ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['left'].set_visible(False)
ax4.set_yticks([])
ax4.grid(True, alpha=0.3, axis='x')

# --- Central Source Element with Proper Positioning ---
# Position central text to avoid overlaps
central_text_pos = [0.46, 0.49, 0.08, 0.04]  # [left, bottom, width, height]
central_ax = fig.add_axes(central_text_pos)
central_ax.text(0.5, 0.5, f'Royal Cubit\n$L = \\frac{{\\pi}}{{6}}$ m\n$\\approx {L_cm:.2f}$ cm', 
                ha='center', va='center', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.5", facecolor=colors['light_gray'], 
                         edgecolor=colors['text'], linewidth=2, alpha=0.95),
                color=colors['text'], transform=central_ax.transAxes)
central_ax.set_xlim(0, 1)
central_ax.set_ylim(0, 1)
central_ax.axis('off')

# Professional arrows connecting central concept to panels
arrow_props = dict(arrowstyle='->', lw=2, alpha=0.6, color=colors['dark_gray'])

# Define arrow positions (from center to each panel) - adjusted for new layout
center = (0.5, 0.51)
panel_centers = [(0.27, 0.71), (0.73, 0.71), (0.27, 0.31), (0.73, 0.31)]

for panel_center in panel_centers:
    arrow = FancyArrowPatch(center, panel_center, transform=fig.transFigure,
                           connectionstyle="arc3,rad=0.1", **arrow_props)
    fig.patches.append(arrow)

# Add figure caption with proper spacing
fig.text(0.5, 0.02, 
         'Figure 1. Unified dimensional framework derived from the Royal Cubit ($L = \\pi/6$ m). ' +
         'The system demonstrates coherent relationships between linear, areal, and volumetric measurements, ' +
         'with the spherical volume maintaining a precise mathematical ratio to the cubic volume.',
         ha='center', va='bottom', fontsize=10, style='italic', wrap=True,
         color=colors['text'], transform=fig.transFigure)

# Use subplots_adjust instead of tight_layout to avoid conflicts
plt.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.10)

plt.show()

# Save as high-quality formats for publication
# plt.savefig('dimensional_framework.pdf', format='pdf', bbox_inches='tight', dpi=300)
# plt.savefig('dimensional_framework.png', format='png', bbox_inches='tight', dpi=300),
         transform=ax4.transAxes, ha='center', va='center', fontsize=10,
         bbox=dict(boxstyle='round,pad=0.4', facecolor=colors['light_gray'], 
                  edgecolor=colors['dark_gray'], alpha=0.9))

ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.spines['left'].set_visible(False)
ax4.set_yticks([])
ax4.grid(True, alpha=0.3, axis='x')

# --- Central Source Element with Proper Positioning ---
# Position central text to avoid overlaps
central_text_pos = [0.46, 0.49, 0.08, 0.04]  # [left, bottom, width, height]
central_ax = fig.add_axes(central_text_pos)
central_ax.text(0.5, 0.5, f'Royal Cubit\n$L = \\frac{{\\pi}}{{6}}$ m\n$\\approx {L_cm:.2f}$ cm', 
                ha='center', va='center', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.5", facecolor=colors['light_gray'], 
                         edgecolor=colors['text'], linewidth=2, alpha=0.95),
                color=colors['text'], transform=central_ax.transAxes)
central_ax.set_xlim(0, 1)
central_ax.set_ylim(0, 1)
central_ax.axis('off')

# Professional arrows connecting central concept to panels
arrow_props = dict(arrowstyle='->', lw=2, alpha=0.6, color=colors['dark_gray'])

# Define arrow positions (from center to each panel) - adjusted for new layout
center = (0.5, 0.51)
panel_centers = [(0.27, 0.71), (0.73, 0.71), (0.27, 0.31), (0.73, 0.31)]

for panel_center in panel_centers:
    arrow = FancyArrowPatch(center, panel_center, transform=fig.transFigure,
                           connectionstyle="arc3,rad=0.1", **arrow_props)
    fig.patches.append(arrow)

# Add figure caption with proper spacing
fig.text(0.5, 0.02, 
         'Figure 1. Unified dimensional framework derived from the Royal Cubit ($L = \\pi/6$ m). ' +
         'The system demonstrates coherent relationships between linear, areal, and volumetric measurements, ' +
         'with the spherical volume maintaining a precise mathematical ratio to the cubic volume.',
         ha='center', va='bottom', fontsize=10, style='italic', wrap=True,
         color=colors['text'], transform=fig.transFigure)

# Use subplots_adjust instead of tight_layout to avoid conflicts
plt.subplots_adjust(left=0.05, right=0.95, top=0.90, bottom=0.10)

plt.show()

# Save as high-quality formats for publication
# plt.savefig('dimensional_framework.pdf', format='pdf', bbox_inches='tight', dpi=300)
# plt.savefig('dimensional_framework.png', format='png', bbox_inches='tight', dpi=300)