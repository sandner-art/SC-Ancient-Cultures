import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

# --- GLOBAL STYLE CONFIGURATION FOR PROFESSIONAL FIGURES ---
# This setup ensures a clean, consistent look suitable for journals.
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica", # A clean, standard font
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 10,
    "figure.titlesize": 12,
    "text.usetex": True, # Use LaTeX for all text rendering
    "text.latex.preamble": r'\usepackage{siunitx} \usepackage{amsmath}', # For \SI command
    "figure.dpi": 300 # Set a high DPI for raster parts of figures
})

# Define the color palette from the user's request
COLORS = {
    'black': '#2F2F2F', # A softer black
    'blue': '#0033A0',  # A strong, professional blue
    'red': '#D42121',   # A clear, striking red
    'gray': '#B0B0B0',
    'fill_blue': '#E5ECF6',
    'fill_red': '#F9E9E9',
    'fill_yellow': '#FEF9E7'
}

# --- MATHEMATICAL CONSTANTS ---
PI = np.pi
PHI = (1 + np.sqrt(5)) / 2

def create_figure_1():
    """Generates Figure 1: The Royal Cubit as a fundamental constant."""
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.set_aspect('equal')
    ax.axis('off') # Hide the axes
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1.5, 4.5)

    # 1. Draw the Royal Cubit Rod
    cubit_length = 10
    cubit_height = 0.8
    ax.add_patch(patches.Rectangle((0, 0), cubit_length, cubit_height,
                                   facecolor=COLORS['fill_yellow'], edgecolor=COLORS['black'], lw=1.5))

    # Add subdivisions (7 palms, 28 digits)
    for i in range(1, 7): # Palms
        ax.plot([cubit_length * i / 7, cubit_length * i / 7], [0, cubit_height], color=COLORS['black'], lw=1)
    for i in range(1, 28): # Digits
        ax.plot([cubit_length * i / 28, cubit_length * i / 28], [0, cubit_height * 0.5], color=COLORS['black'], lw=0.5)

    # Add labels for the cubit
    ax.text(cubit_length / 2, cubit_height + 0.2, r'\textbf{Egyptian Royal Cubit (\textit{meh niswt})}',
            ha='center', va='bottom', fontsize=11)
    ax.text(cubit_length / 2, -0.4, r'Length $\approx \SI{52.36}{\centi\meter}$',
            ha='center', va='top', fontsize=10)
    ax.annotate('', xy=(0, -0.2), xytext=(cubit_length, -0.2),
                arrowprops=dict(arrowstyle='<->', color=COLORS['black'], lw=1))

    # 2. Draw the value boxes and connecting arrows
    bbox_style = dict(boxstyle='round,pad=0.5', fc=COLORS['fill_blue'], ec=COLORS['blue'], lw=1)
    target_point = (cubit_length / 2, cubit_height) # Point arrows to the top of the cubit

    # Box 1: pi/6
    p6_val = PI / 6
    p6_text = r'\textbf{Circular Geometry}' + '\n' + r'$\frac{\pi}{6} \approx ' + f'{p6_val:.6f}' + r'\dots$'
    p6_pos = (5, 3.5)
    ax.text(p6_pos[0], p6_pos[1], p6_text, ha='center', va='center', bbox=bbox_style, fontsize=9)
    ax.annotate('', xy=target_point, xytext=p6_pos,
                arrowprops=dict(arrowstyle='->,head_length=0.4,head_width=0.2',
                                color=COLORS['blue'], lw=1.5,
                                connectionstyle="arc3,rad=0"))

    # Box 2: Golden Ratio
    phi2_val = PHI**2 / 5
    phi2_text = r'\textbf{Golden Ratio Relation}' + '\n' + r'$\frac{\phi^2}{5} \approx ' + f'{phi2_val:.6f}' + r'\dots$'
    phi2_pos = (0.5, 2.5)
    ax.text(phi2_pos[0], phi2_pos[1], phi2_text, ha='center', va='center', bbox=bbox_style, fontsize=9)
    ax.annotate('', xy=target_point, xytext=phi2_pos,
                arrowprops=dict(arrowstyle='->,head_length=0.4,head_width=0.2',
                                color=COLORS['blue'], lw=1.5,
                                connectionstyle="arc3,rad=-0.2"))

    # Box 3: Transcendental Difference
    pidiff_val = PI - PHI**2
    pidiff_text = r'\textbf{Transcendental Difference}' + '\n' + r'$\pi - \phi^2 \approx ' + f'{pidiff_val:.6f}' + r'\dots$'
    pidiff_pos = (9.5, 2.5)
    ax.text(pidiff_pos[0], pidiff_pos[1], pidiff_text, ha='center', va='center', bbox=bbox_style, fontsize=9)
    ax.annotate('', xy=target_point, xytext=pidiff_pos,
                arrowprops=dict(arrowstyle='->,head_length=0.4,head_width=0.2',
                                color=COLORS['blue'], lw=1.5,
                                connectionstyle="arc3,rad=0.2"))
    
    fig.suptitle(r'\textbf{Figure 1.} The Royal Cubit as a fundamental mathematical constant.', y=0.05, fontsize=10)
    plt.savefig('fig_cubit_convergence.pdf', bbox_inches='tight')
    plt.close(fig)
    print("Figure 1 saved as fig_cubit_convergence.pdf")


def create_figure_2():
    """Generates Figure 2: Practical application of hexagonal geometry."""
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')
    ax.axis('off')

    radius = 1.5 # The circumradius of the hexagon
    h_dist = radius * np.sqrt(3)

    def draw_hexagon(ax, center, radius, **kwargs):
        """Helper function to draw a single hexagon."""
        vertices = [
            (center[0] + radius * np.cos(angle), center[1] + radius * np.sin(angle))
            for angle in np.linspace(0, 2 * PI, 7)[:-1]
        ]
        hexagon = patches.Polygon(vertices, **kwargs)
        ax.add_patch(hexagon)

    # Draw the background grid of hexagons
    for row in range(-1, 2):
        for col in range(-1, 2):
            center_x = col * h_dist + (row % 2) * h_dist / 2
            center_y = row * 1.5 * radius
            draw_hexagon(ax, (center_x, center_y), radius,
                         facecolor=COLORS['fill_blue'], edgecolor=COLORS['blue'], lw=1.0)

    # Highlight the central hexagon
    draw_hexagon(ax, (0, 0), radius, facecolor=COLORS['fill_red'],
                 edgecolor=COLORS['red'], lw=2.0, zorder=10)

    # Draw the construction circle and radius for the highlighted hexagon
    circle = patches.Circle((0, 0), radius, facecolor='none',
                            edgecolor=COLORS['red'], linestyle='--', lw=1, zorder=11)
    ax.add_patch(circle)
    
    # Radius line and label
    corner_1 = (radius * np.cos(PI/6), radius * np.sin(PI/6))
    ax.plot([0, corner_1[0]], [0, corner_1[1]], color=COLORS['red'], lw=1.5, zorder=12)
    ax.text(corner_1[0] * 0.5, corner_1[1] * 0.5 + 0.1, r'$r = \pi/6$',
            color=COLORS['black'], ha='center', va='bottom', rotation=30, fontsize=10, zorder=13)

    # Add annotation text
    ax.set_title(r'\textbf{Modular Hexagonal Grid}', fontsize=12)
    description = (
        'The perfect fit of the hexagon within the $\pi/6$ system enables\n'
        'efficient, space-filling tessellation for construction, requiring\n'
        'only the base cubit unit for layout.'
    )
    ax.text(0, -2.5, description, ha='center', va='top', fontsize=10, wrap=True)
    
    ax.autoscale_view()
    fig.suptitle(r'\textbf{Figure 2.} Practical application of hexagonal geometry in the $\pi/6$ system.', y=0.08, fontsize=10)
    plt.savefig('fig_hexagonal_tessellation.pdf', bbox_inches='tight')
    plt.close(fig)
    print("Figure 2 saved as fig_hexagonal_tessellation.pdf")


def create_figure_3():
    """Generates Figure 3: Perfect integration of hexagonal geometry."""
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)

    radius = 2.0
    
    # Vertices of the hexagon
    vertices = np.array([
        (radius * np.cos(theta), radius * np.sin(theta))
        for theta in np.arange(0, 2*PI, PI/3)
    ])

    # Draw the main circle
    ax.add_patch(patches.Circle((0, 0), radius, facecolor='none', edgecolor=COLORS['gray'], lw=1.5))
    ax.plot(0, 0, 'o', color=COLORS['black'], markersize=4)
    ax.text(-0.1, -0.2, '$O$', ha='right', va='top')

    # Draw the inscribed hexagon
    ax.add_patch(patches.Polygon(vertices, facecolor='none', edgecolor=COLORS['blue'], lw=2))

    # Label the radius and side length
    ax.plot([0, vertices[0, 0]], [0, vertices[0, 1]], color=COLORS['black'], linestyle='--', lw=1)
    ax.text(vertices[0, 0] * 0.5, vertices[0, 1] * 0.5 - 0.1, r'$r = \pi/6$',
            color=COLORS['blue'], ha='center', va='top', rotation=0, fontsize=10)
    ax.text(np.mean(vertices[0:2, 0]), np.mean(vertices[0:2, 1]) + 0.1, r'$s=r=\pi/6$',
            color=COLORS['blue'], ha='center', va='bottom', rotation=30, fontsize=10)

    # Draw and label the angles
    # Angle arc for 60 degrees
    angle_arc_60 = patches.Arc((0, 0), 1.2, 1.2, angle=0, theta1=0, theta2=60,
                               edgecolor=COLORS['red'], lw=1.0)
    ax.add_patch(angle_arc_60)
    ax.text(0.75, 0.25, r'$60^\circ = \frac{\pi}{3}$', color=COLORS['red'], ha='center', fontsize=10)

    # Angle arc for 120 degrees
    v1, v2, v3 = vertices[0], vertices[1], vertices[2]
    angle_arc_120 = patches.Arc(v2, 1.2, 1.2, angle=0, theta1=180, theta2=300,
                                edgecolor=COLORS['red'], lw=1.0)
    ax.add_patch(angle_arc_120)
    ax.text(v2[0] + 0.3, v2[1] - 0.2, r'$120^\circ = \frac{2\pi}{3}$', color=COLORS['red'], ha='left', fontsize=10)

    fig.suptitle(r'\textbf{Figure 3.} Perfect integration of hexagonal geometry in the $\pi/6$ system.', y=0.1, fontsize=10)
    plt.savefig('fig_hexagon_geometry.pdf', bbox_inches='tight')
    plt.close(fig)
    print("Figure 3 saved as fig_hexagon_geometry.pdf")


def create_figure_4():
    """Generates Figure 4: The unified spherical volume system."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 5))

    # --- Part A: Sphere ---
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_xlim(-2.5, 2.5)
    ax1.set_ylim(-3.5, 3.5)
    
    # Draw sphere with 3D effect
    ax1.add_patch(patches.Circle((0, 0), 2, facecolor=COLORS['fill_blue'], edgecolor=COLORS['blue'], lw=1.5))
    ax1.add_patch(patches.Ellipse((0, 0), 4, 1.2, facecolor='none', edgecolor=COLORS['blue'], alpha=0.6, lw=1))
    ax1.add_patch(patches.Ellipse((0, 0), 1.2, 4, facecolor='none', edgecolor=COLORS['blue'], alpha=0.6, lw=1))

    # Labels for sphere
    ax1.set_title(r'\textbf{A. Sphere with Cubit Circumference}', y=0.9)
    ax1.text(0, -2.5, r'Circumference $c = 1$ royal cubit $= \pi/6$ m', ha='center', va='center')
    ax1.text(0, 0, r'Radius $r = \frac{c}{2\pi} = \frac{1}{12}$ m', ha='center', va='center')

    # --- Part B: Hekat Vessel ---
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_xlim(-2.5, 2.5)
    ax2.set_ylim(-3.5, 3.5)

    # Draw a stylized vessel
    verts = [
        (1.2, 1.5),  # Top right
        (1.5, 0.5), (1.5, -1.5), (0, -2.0), # Right curve to bottom
        (-1.5, -1.5), (-1.5, 0.5), (-1.2, 1.5), # Bottom to top left
    ]
    codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CURVE4]
    path = Path(verts, codes)
    ax2.add_patch(patches.PathPatch(path, facecolor='#EADDCA', edgecolor='#6D4C41', lw=1.5))
    ax2.add_patch(patches.Ellipse((0, 1.5), 2.4, 0.6, facecolor='none', edgecolor='#6D4C41', lw=1.5))
    
    # Labels for vessel
    ax2.set_title(r'\textbf{B. Standard Volume Unit}', y=0.9)
    ax2.text(0, 0, r'$\frac{1}{2}$ Hekat' + '\n' + r'$\approx 2.424$ liters', ha='center', va='center')
    ax2.text(0, -2.5, r'Archaeological Standard', ha='center', va='center')

    # --- Arrow and Formula connecting the two ---
    # Use figure coordinates for arrow placement between axes
    con = patches.ConnectionPatch(xyA=(-0.2, 0.5), xyB=(0.2, 0.5),
                                  coordsA='axes fraction', coordsB='axes fraction',
                                  axesA=ax1, axesB=ax2,
                                  arrowstyle="-|>,head_width=8,head_length=8",
                                  color=COLORS['red'], lw=2.5)
    fig.add_artist(con)
    fig.text(0.5, 0.55, 'Unifies Length and Volume', ha='center', va='center',
             color=COLORS['black'], fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

    # The Core Formula box
    formula_text = (r'\textbf{The Unifying Relationship}' + '\n' +
                    r'$V_{\text{sphere}} = \frac{c^3}{6\pi^2} = \frac{(\pi/6)^3}{6\pi^2} = \frac{\pi}{1296}\,\text{m}^3 = \frac{1}{2}\,\text{hekat}$')
    fig.text(0.5, 0.2, formula_text, ha='center', va='center', fontsize=11,
             bbox=dict(boxstyle='round,pad=0.5', fc=COLORS['fill_red'], ec=COLORS['red'], lw=1))
    
    fig.suptitle(r'\textbf{Figure 4.} The unified spherical volume system.', y=0.08, fontsize=10)
    plt.tight_layout(rect=[0, 0.1, 1, 0.9]) # Adjust layout
    plt.savefig('fig_spherical_volume.pdf')
    plt.close(fig)
    print("Figure 4 saved as fig_spherical_volume.pdf")


if __name__ == '__main__':
    print("Generating professional figures for journal publication...")
    create_figure_1()
    create_figure_2()
    create_figure_3()
    create_figure_4()
    print("\nAll figures generated successfully.")
    print("You can now include them in your LaTeX document using:")
    print(r"\usepackage{graphicx}")
    print(r"\includegraphics[width=\textwidth]{fig_cubit_convergence.pdf}")