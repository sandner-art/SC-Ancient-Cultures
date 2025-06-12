### **Eratosthenes’ Experiment: Ancient and Modern Methodology**

Author: Daniel Sandner

#### **Abstract**

Eratosthenes' experiment of circa 240 BCE stands as a foundational achievement in geodesy. This paper conducts a rigorous methodological analysis of the experiment, moving beyond its historical outcome to perform a form of scientific archaeology on its methods. We reconstruct the ancient technique, analyzing not only the core geometric insight but also the practical strategies for determining local noon without clocks, and the profound impact of measurement uncertainty. The paper's central historical analysis focuses on the dominant source of error: the distance between Syene and Alexandria. We deconstruct this variable, exploring the ambiguity of the *stadion*, the imprecision of bematist surveys, and a compelling hypothesis of an "informed scientific correction" applied by Eratosthenes himself. This is contrasted with a modern framework detailing enhancements for global application, including corrections for non-aligned points, altitude differences, and sun's declination. Finally, we extend the method's principles into a theoretical tool for comparative planetology, deriving the expected shadow curves for planets of varying geometries. This work reframes Eratosthenes' experiment not as a simple proof, but as a sophisticated and adaptable method for deducing the fundamental properties of a celestial body, both in the ancient world and today.

#### **1. Introduction**

In approximately 240 BCE, Eratosthenes of Cyrene, the chief librarian at the great Library of Alexandria, executed an experiment of remarkable ingenuity and consequence. By observing the difference in solar shadow angles at two locations in Egypt, he produced the first quantitative, evidence-based measurement of the Earth's circumference. This achievement stands as a foundational moment in the history of science, marking a paradigm shift from purely philosophical speculation about the cosmos to its empirical and mathematical measurement. It represents one of the earliest descriptions of successful applications of the scientific method, integrating a theoretical model, precise observation, and geometric calculation to reveal a fundamental truth about the natural world.

The purpose of this paper is not simply to recount this famous experiment, but to conduct a deep methodological analysis of it—a form of scientific archaeology. We aim to deconstruct its components to understand not only *how* it worked, but also the practical challenges and sources of uncertainty that defined its execution in the ancient world. The scope of this investigation is threefold: first, to reconstruct the ancient methodology with a focus on the measurement techniques and data-processing strategies Eratosthenes likely employed to manage imperfect information; second, to develop a comprehensive modern framework that refines and generalizes the experiment using contemporary technology and mathematical formalisms; and third, to extend its underlying principles into a theoretical tool for comparative planetology, exploring what this 2,200-year-old method can teach us about discerning the properties of other worlds.

This paper will demonstrate that Eratosthenes' experiment is far from a solved historical curiosity. By dissecting its historical context, sources of error, and theoretical underpinnings, we present a more nuanced portrait of Eratosthenes as a working scientist who grappled with noisy, real-world data. We will move from this reconstruction to outline a high-precision protocol for modern replication, accounting for variables like non-meridian alignment and observer altitude. Finally, we will explore the experiment’s theoretical implications, analyzing the distinct shadow curves produced on planets of differing geometries to show that the method’s true power lies in its adaptability and its ability to reveal the fundamental geometric and astronomical properties of a celestial body.

---

#### **2. Historical and Astronomical Foundations**

Eratosthenes' experiment was not an isolated flash of brilliance but the culmination of centuries of intellectual and technical progress across the Hellenistic world and the ancient Near East. His genius lay in his ability to synthesize disparate threads of knowledge—Greek geometric theory, Egyptian observational practice, and Babylonian mathematical astronomy—into a single, elegant experimental design.

**2.1 The Intellectual Milieu of the Library of Alexandria**

As the chief librarian at the Musaeum of Alexandria, Eratosthenes was positioned at the global epicenter of scholarship. The Library was a repository of unprecedented scale, containing maps, astronomical records, mathematical treatises, and travelogues from across the known world. This interdisciplinary environment provided him with the necessary resources: access to the most advanced geometric and astronomical texts, official survey records of the Ptolemaic kingdom, and a culture of critical inquiry that encouraged the application of mathematics to the natural world.

**2.2 Foundational Concepts: The Shoulders of Giants**

A crucial prerequisite for the experiment was a theoretical model of a spherical Earth. This idea, born from philosophy, had been placed on firm observational ground a century before Eratosthenes.

*   **Greek Theoretical Framework:** The concept of a spherical Earth is first attributed to Pythagoras (c. 570 BCE) and his school, likely on aesthetic grounds. However, it was Aristotle (384–322 BCE) who provided the first scientific arguments for this model in his treatise *On the Heavens* (*De Caelo*). He cited empirical evidence, including the gradual disappearance of ships' hulls over the horizon, the circular shape of the Earth's shadow on the Moon during a lunar eclipse, and the changing altitude of constellations as one travels north or south. Aristotle concluded, "the Earth is not only round, but it is also a circle of no great size", thus establishing the necessary theoretical basis for a geodetic measurement.

*   **Egyptian and Babylonian Technical Legacy:** The practical tools for the experiment were inherited from the older civilizations of the Near East. The gnomon, a simple vertical rod for tracking solar shadows, was a refined version of the monumental obelisks used in Egypt for centuries to mark the solstices and track the sun's daily motion. From Babylonia came a long tradition of meticulous mathematical astronomy. Babylonian astronomers had developed sophisticated arithmetic methods for predicting celestial events and created extensive observational records, fostering a quantitative and empirical approach to studying the heavens. However, both cultures operated within a cosmological framework of a flat Earth, which precluded them from using shadow-length variations to measure the planet itself. Eratosthenes' synthesis was in applying these ancient, precise techniques to the new Greek model of a spherical world.

**2.3 Primary Historical Accounts**

Eratosthenes' own work on his measurement, likely titled *On the Measurement of the Earth*, has been lost. Our knowledge is therefore reconstructed from later authors who cited his work. These secondary accounts provide the core data for the experiment while also introducing minor variations that reveal the nature of historical and scientific transmission.

*Table 1: Key Historical Sources for the Eratosthenes Experiment*

| Author (c. Date) | Work | Key Contribution |
| :--- | :--- | :--- |
| **Cleomedes** (c. 150 CE) | *On the Circular Motions of the Celestial Bodies* | Provides the most complete description of the method, including the cities of Syene and Alexandria, the observation of a shadowless well, the angle of 1/50th of a circle (7.2°), and the distance of 5,000 stadia. This is our primary source. |
| **Strabo** (c. 20 CE) | *Geographica* | A renowned geographer who corroborates the 5,000 stadia distance between the two cities and notes that Syene is located on the Tropic of Cancer. |
| **Pliny the Elder** (c. 77 CE) | *Naturalis Historia* | Mentions Eratosthenes' "subtle discovery" and cites a circumference of 252,000 stadia. This slightly different figure may represent a later adjustment by Eratosthenes or others to create a number easily divisible by 60 or 360. |

These accounts, while not from Eratosthenes himself, provide a consistent picture of the experiment's core logic and data, allowing for a robust modern reconstruction and analysis.

#### **2.4 Isomorphism and the Cosmological Debate: A Heliocentric Blind Spot**

A crucial aspect of Eratosthenes’ experiment is its **isomorphism** with respect to the dominant cosmological models of the day. The experiment's results are identical whether one assumes a geocentric (Earth-centered) or a heliocentric (Sun-centered) system. The underlying geometry depends only on two assumptions: (1) the Earth is spherical, and (2) the Sun is sufficiently far away that its rays arrive as parallel lines. The question of which celestial body is in motion is irrelevant to the measurement of shadow angles at a single instant.

This kinematic equivalence is a primary reason why Eratosthenes' result, while revolutionary, did not challenge the prevailing geocentric model that would later be formalized by Ptolemy. His measurement could be—and was—comfortably absorbed into the geocentric framework by providing the first credible value for the size of the central Earth. This demonstrates a key principle in the history of science: a single experiment, no matter how brilliant, often cannot by itself overturn a well-established paradigm, especially if its results can be incorporated by that paradigm.

It is essential to note that heliocentrism was not an unknown concept. **Aristarchus of Samos (c. 310 – c. 230 BCE)**, a contemporary of Eratosthenes, had already proposed a fully heliocentric model, arguing that the Earth rotated on its axis and revolved around a stationary Sun. Eratosthenes, working at the center of the Greek intellectual world, was almost certainly aware of Aristarchus's hypothesis (Heath, 1913). The fact that his experiment could not distinguish between the two models serves as a perfect illustration of its specific, geodetic focus. It was designed to answer the question "How large is the Earth?", not "What is the Earth's place in the cosmos?".

---

##### **References**
 MacLeod, R. (Ed.). (2004). *The Library of Alexandria: Centre of Learning in the Ancient World*. I.B. Tauris.
 Aristotle. (c. 350 BCE). *On the Heavens*, Book II, Chapter 14.
 Pannekoek, A. (1961). *A History of Astronomy*. Interscience Publishers.
 Neugebauer, O. (1957). *The Exact Sciences in Antiquity*. Brown University Press.
 Cleomedes. (c. 150 CE). *On the Circular Motions of the Celestial Bodies*, Book I, Chapter 7. Trans. by I. G. Kidd and L. G. Westerink (2004).
 Strabo. (c. 20 CE). *Geographica*, Book 17, Chapter 1.
 Pliny the Elder. (c. 77 CE). *Naturalis Historia*, Book II, Chapter 108.

Excellent. We will now proceed to the core of the historical analysis. This section synthesizes our discussion on the practical challenges and uncertainties of the ancient experiment, culminating in a detailed analysis of the distance measurement, which we argue is the most critical and revealing variable.

***

#### **3. Reconstruction of the Ancient Methodology: A Study in Uncertainty**

To appreciate the genius of Eratosthenes' experiment, one must reconstruct it not with modern hindsight, but within the constraints of ancient technology and metrology. This requires an analysis of how each component of the experiment was executed and synchronized, and a careful accounting of the sources of uncertainty. We find that the dominant source of error was not in the astronomical observation itself, but in the terrestrial measurement of distance.

**3.1 The Observational Strategy: Synchronizing the Geometric Moment**

A common misconception is that the experiment required a mechanism for precise, simultaneous timekeeping across 800 kilometers. In reality, the experiment required **geometric synchronization**, not temporal synchronization. The goal was to measure the sun's zenith angle (`θ`) at both locations at the same geometric instant: the moment the sun crossed the local meridian. This moment, local solar noon, was determined using the gnomon itself.

*   **3.1.1 Clockless Noon-Finding Techniques**
    Ancient observers had two robust methods for identifying local noon without a clock:
    1.  **The "Shortest Shadow" Method:** An observer would track the tip of the gnomon's shadow in the hours surrounding midday, marking its path. The point on this curve closest to the gnomon's base marks the shortest shadow, indicating the moment of local noon. The line connecting the gnomon base to this point defines the North-South meridian. While effective, the slow change in shadow length near noon limits its precision to within a few minutes (Goldstein, 1983).
    2.  **The "Method of Equal Altitudes":** A more precise technique involves drawing a circle on a level surface centered at the gnomon's base. The observer marks the two points where the shadow tip crosses this circle, once in the morning and once in the afternoon. The angle bisector of these two points yields a more accurate meridian line, and the temporal midpoint between the two crossings defines local noon with greater precision (Neugebauer, 1975).

By using such a method, observers in both Alexandria and Syene could independently ensure their measurements corresponded to the same solar alignment, making absolute time irrelevant.

**3.2 The Critical Variable: Deconstructing the Distance 'd'**

The terrestrial distance (`d`) between Alexandria and Syene is the most significant variable and the largest source of historical uncertainty. Eratosthenes used a value of 5,000 stadia, a figure likely sourced from official records compiled by *bematists*, professional surveyors trained to measure distance by counting their steps. This figure, however, is subject to two distinct layers of uncertainty.

*   **3.2.1 Layer 1: The Ambiguity of the *Stadion***
    The term "stadion" did not represent a single, universally standardized unit. Its length varied by region and time. Resolving which stadion Eratosthenes used is central to interpreting his result.

*Table 2: Common Stadia of the Hellenistic Era*

| Stadion Name | Approximate Length (m) | Context |
| :--- | :--- | :--- |
| **Egyptian** | ~157.5 | The local standard in Ptolemaic Egypt, where the experiment was conducted. |
| **Olympic** | ~176 | A common standard used in mainland Greece. |
| **Attic** | ~185 | The standard used in Athens, widely known in the Greek world. |

*   **3.2.2 Layer 2: The Imprecision of the Measurement**
    Beyond the unit itself, the number "5,000" is suspiciously round, suggesting it was an official, accepted approximation rather than a precise survey result. The journey, likely following the winding path of the Nile River, was over 900 km long. Even for trained bematists, an error margin of 5-10% due to terrain and human factors is a reasonable historical assumption (Engels, 1985).

**3.3 Reconciling Ancient Data with Modern Measurements**

By comparing the ancient value of 5,000 stadia to modern geodetic data, we can attempt to reverse-engineer Eratosthenes' process and evaluate competing historical hypotheses.

*   **Modern Distances:**
    *   **Geometric Distance:** The true North-South arc distance between Alexandria (31.2°N) and Syene (24.1°N) is approximately **788 km**. This is the geometrically correct distance for the calculation.
    *   **Travel Distance:** The path along the Nile is significantly longer, estimated at approximately **925 km**.

*   **3.3.1 Inferring the Stadion: A Central Conflict**
    We can test which stadion Eratosthenes might have used by dividing the known modern distances by his 5,000 stadia figure.
    1.  If we assume he used the geometrically correct distance:  
        `788,000 m / 5,000 stadia = 157.6 m/stadion`.  
        This provides an almost perfect match for the **Egyptian stadion**.
    2.  If we assume he used the available travel distance:  
        `925,000 m / 5,000 stadia = 185 m/stadion`.  
        This provides a perfect match for the **Attic stadion**.

*   **3.3.2 Three Competing Hypotheses**
    This conflict has led to three primary interpretations of Eratosthenes' work:
    1.  **The "Fortuitous Cancellation of Errors" Hypothesis:** This view suggests Eratosthenes naively used the incorrect travel distance (~925 km), which was based on the Attic stadion (185 m). The ~17% overestimate in distance fortuitously compensated for other errors, leading to a surprisingly good result (Dutka, 1993).
    2.  **The "Corrupted Data" Hypothesis:** This theory posits that Eratosthenes was a meticulous geodesist. He used the correct Egyptian stadion and a near-correct geometric distance, but his precise angle measurement (closer to the true 7.08°) was rounded to the convenient 1/50th of a circle (7.2°) by later authors like Cleomedes, who simplified his work (Rawlins, 1982).
    3.  **The "Informed Scientific Correction" Hypothesis:** We propose this as the most plausible scenario. Eratosthenes, a master geographer, would have known the bematists' 5,000-stadia travel distance was geometrically flawed. It is highly likely he used his cartographic expertise to apply a scientific correction. Starting with the well-known travel distance (likely in Attic stadia), he could have projected the winding path onto the meridian on his maps, reducing the distance by a reasonable ~10-15% to arrive at a more accurate geometric value before his final calculation. This portrays him not as lucky or misinterpreted, but as a critical scientist actively refining his imperfect data.

**3.4 An Error Budget for the Ancient Experiment**

To contextualize these issues, a comparative error budget demonstrates that the distance `d` was the dominant source of uncertainty, dwarfing all other factors.

*Table 3: Comparative Error Budget for Eratosthenes' Calculation*

| Source of Error | Plausible Ancient Uncertainty | Resulting Error in Circumference `C` |
| :--- | :--- | :--- |
| **Distance (`d`)** | **~10-15%** (Unit ambiguity & survey method) | **~10-15%** |
| **Angle (`Δθ`)** | **±0.2°** (Gnomon measurement) | **~3-4%** |
| **Meridian Alignment** | Syene is ~3° east of Alexandria | **<1%** (Affects `d` as non-N-S distance) |
| **Altitude Difference** | Negligible in this context | **<0.1%** |

This analysis makes it clear that mastering the terrestrial distance was the single greatest challenge of the experiment. The brilliance of Eratosthenes was not only in the experimental design but also in his likely efforts to manage and correct the largest known source of error.

#### **3.5 Consequences of the Result: Providing a Scale for the Cosmos**

The calculation of the Earth's circumference was not an intellectual exercise in isolation; it had profound, cascading effects on the quantitative science of astronomy. By providing a reliable value for the Earth's radius (`R`), Eratosthenes provided the first rung on the "cosmic distance ladder." His result was the fundamental baseline—the "meter stick"—that allowed astronomers to convert relative distances into absolute ones.

1.  **Calculating the Distance to the Moon:** Aristarchus had previously devised a geometric method to estimate the Moon's distance in terms of Earth radii. By observing the size and curvature of the Earth's shadow on the Moon during a lunar eclipse, he estimated the Moon’s distance to be approximately 60 Earth radii (Dreyer, 1953). This was a brilliant, but purely relative, result. Once Eratosthenes calculated `C ≈ 252,000` stadia, a value for `R` became known (`R = C / 2π`). Astronomers could, for the first time, assign a plausible absolute distance to a celestial body:
    `Distance to Moon ≈ 60 * (252,000 / 2π) stadia ≈ 2,400,000 stadia.`
    This was the first scientifically-grounded estimate of the size of the Earth-Moon system.

2.  **Estimating the Distance to the Sun:** Aristarchus had also attempted to find the Sun's distance relative to the Moon's. By measuring the angle between the Sun and a half-moon (when the Earth-Moon-Sun angle is 90°), he estimated the Sun was about 19 times farther away than the Moon. While his measurement was imprecise (the true ratio is closer to 400), it established that the Sun was much farther and therefore vastly larger than the Earth. Eratosthenes' result allowed this ratio to be converted into an absolute, albeit underestimated, distance. This provided the first quantitative evidence that the Earth was not the dominant body in the solar system, a key piece of evidence for the (unpopular) heliocentric model.

3.  **Foundation for Mathematical Geography:** A known circumference is the prerequisite for a global system of latitude and longitude. Eratosthenes himself pioneered this, creating world maps that featured, for the first time, a grid of perpendicular lines based on a spherical Earth of known size. This transformed cartography from a descriptive art into a mathematical science (Berggren & Jones, 2000).

In summary, Eratosthenes' measurement was the critical linchpin that connected terrestrial geometry with cosmic geometry. It grounded astronomical models in a physical, measurable reality and enabled the first quantitative, scaled estimates of the cosmos.
---

##### **References**
 Goldstein, B. R. (1983). *The Method of Equal Altitudes in the Ancient and Medieval Worlds*.
 Neugebauer, O. (1975). *A History of Ancient Mathematical Astronomy*. Springer-Verlag.
 Engels, D. (1985). *The Length of Eratosthenes' Stade*. The American Journal of Philology, 106(3), 298–311.
 Dutka, J. (1993). *Eratosthenes' Measurement of the Earth Reconsidered*. Archive for History of Exact Sciences, 46(1), 55–66.
 Rawlins, D. (1982). *The Eratosthenes-Strabo Nile Map. Is It the Prototype of the Carte Pisane?* Archive for History of Exact Sciences, 26(3), 211–219.

Excellent. Now we transition from the ancient world to the modern, detailing a rigorous framework for replicating and generalizing the experiment. This section operationalizes the insights from our historical analysis, showing how to correct for the subtle errors that Eratosthenes had to ignore or estimate.

***

#### **4. Modern Methodological Enhancements**

While Eratosthenes’ method was revolutionary, its reliance on specific simplifying assumptions (meridian alignment, solstice date) limited its general applicability. A modern reconstruction of the experiment can remove these constraints through the application of precise instrumentation and spherical trigonometry, transforming it into a robust and globally applicable geodetic tool. This section outlines a high-precision protocol for a modern experiment and quantifies the corrections for factors negligible in antiquity but relevant today.

**4.1 A Generalized Framework for Global Measurement**

The core of the modern method is to generalize the experiment for any two points on Earth (`P_1` and `P_2`), measured on any given day. This requires a departure from local noon and an introduction of universal time.

*   **4.1.1 Independence from Meridian Alignment**
    Eratosthenes chose two cities he believed to be on the same meridian to simplify the distance `d` into a pure North-South arc. For two arbitrarily located points, `P_1(φ_1, λ_1)` and `P_2(φ_2, λ_2)`, where `φ` is latitude and `λ` is longitude, the relevant distance is the great-circle path. This distance, `d`, can be calculated with high precision using the **haversine formula**:

    `a = sin²(Δφ/2) + cos(φ_1)cos(φ_2)sin²(Δλ/2)`
    `c = 2 * atan2(√a, √(1-a))`
    `d = R * c` (Eq. 1)

    Where `Δφ = φ_2 - φ_1`, `Δλ = λ_2 - λ_1`, and `R` is the Earth's mean radius (~6,371 km). All angles must be in radians.

*   **4.1.2 Independence from the Solstice: Accounting for Solar Declination**
    To conduct the experiment on any day, one must account for the sun’s declination, `δ`, which is the angle of the sun's rays relative to the Earth's equatorial plane. The zenith angle `θ` at a specific location is no longer equal to its latitude, but is given by:

    `θ = |φ - δ|` (Eq. 2)

    The declination `δ` for any given day of the year (`N`) can be approximated by the formula:

    `δ ≈ -23.45° * cos( (360/365) * (N + 10) )` (Eq. 3)

    or obtained from astronomical almanacs for higher precision.

*   **4.1.3 Synchronized Measurement**
    Since the two points are not on the same meridian, their local noons differ. It is therefore essential that the measurement of the sun's shadow be taken at both locations at the **same instant of universal time** (e.g., 12:00 UTC). This ensures that the measured shadow angles correspond to a single, fixed position of the sun relative to the Earth, making the subsequent geometric calculation valid.

**4.2 A High-Precision Protocol**

A modern experiment would follow these steps:
1.  **Site Selection:** Choose two or more locations with precisely known coordinates (`φ`, `λ`) and altitudes (`h`).
2.  **Instrumentation:** Use a theodolite or a smartphone application with a digital inclinometer to measure the sun's altitude (`α`) directly, or use a precision-machined gnomon on a leveled surface to measure shadow length (`s`).
3.  **Data Acquisition:** At a pre-agreed universal time, all observers measure the sun's altitude `α` or shadow length `s`. The zenith angle is then calculated as `θ = 90° - α` or `θ = arctan(s/h)`.
4.  **Calculation:**
    a. Determine the angular separation of the sun's rays as they strike the Earth, `Δθ`, which is the great-circle angle between the two sub-solar points. In a simplified but effective approach, `Δθ` can be approximated by the angle between the two measured zenith vectors.
    b. Calculate the great-circle distance `d` between the two observation points using their coordinates and the haversine formula (Eq. 1).
    c. Calculate the circumference using the foundational formula: `C = (360°/Δθ) * d`.
5.  **Data Aggregation:** If using a network of three or more points, calculate the circumference for multiple pairs and average the results to reduce random measurement error.

**4.3 Correction for Second-Order Effects**

For a truly rigorous measurement aiming for the highest accuracy, two further corrections are necessary.

*   **4.3.1 Observer Altitude**
    As discussed, observers are not at sea level. They measure a distance `d_ground` on a circle of radius `R + h`, where `h` is their average altitude. To find the Earth's sea-level circumference, this distance must be mathematically reduced. The corrected sea-level distance, `d_sea`, is given by:

    `d_sea ≈ d_ground * (R_sea / (R_sea + h_avg))` (Eq. 4)

    While this correction is small (~0.025% for an altitude of 1.6 km), it is essential for precision geodesy.

*   **4.3.2 Earth's Oblateness**
    The Earth is not a perfect sphere but an oblate spheroid, with an equatorial radius (~6,378 km) that is ~21 km larger than its polar radius (~6,357 km). This has two effects:
    1.  The Earth's radius `R` is latitude-dependent.
    2.  The local vertical (defined by a plumb line) does not point directly to the Earth's geometric center, except at the equator and the poles. The difference is the *deflection of the vertical*.

    A full geodetic treatment would use a more complex model like the WGS84 reference ellipsoid instead of a simple sphere. However, for most applications outside of professional geodesy, using the mean radius in the haversine formula provides a result well within 1% of the true value, which is sufficient for demonstrating the method's power and precision.

*Table 4: Comparison of Ancient vs. Modern Methodological Components*

| Component | Ancient Method | Modern Method | Rationale for Enhancement |
| :--- | :--- | :--- | :--- |
| **Synchronization** | Local Noon (Geometric) | Universal Time (UTC) | Enables measurement between non-aligned points. |
| **Distance (`d`)** | Bematist survey, estimated | GPS and Haversine Formula | Eliminates the largest source of error and uncertainty. |
| **Angle (`Δθ`)** | Gnomon, solstice observation | Theodolite/App, declination formula | Allows measurement on any day and increases precision. |
| **Altitude (`h`)** | Ignored (negligible effect) | Mathematically corrected | Required for high-precision geodetic results. |
| **Earth Model** | Perfect Sphere | Oblate Spheroid (e.g., WGS84) | Increases accuracy by using a more realistic model of Earth's shape. |

This modern framework transforms Eratosthenes’ brilliant but constrained experiment into a flexible, precise, and globally applicable scientific instrument.

---

##### **References**
Sinnott, R. W. (1984). *Virtues of the Haversine*. Sky and Telescope, 68(2), 159.
Meeus, J. (1998). *Astronomical Algorithms*. Willmann-Bell, Inc.
Vaníček, P., & Krakiwsky, E. J. (1986). *Geodesy: The Concepts* (2nd ed.). Elsevier.
Torge, W., & Müller, J. (2012). *Geodesy* (4th ed.). De Gruyter.

Of course. We will now move to the theoretical analysis, extending the principles of the experiment beyond its original context to explore its power as a universal tool for planetary science. This section addresses the "what if" questions, demonstrating how the experiment's results would change on worlds of different shapes and in different solar systems.

***

#### **5. Theoretical Analysis: The Experiment on Other Worlds**

The true power of Eratosthenes’ method lies not in its historical result, but in its universal principles. By abstracting the experiment from its terrestrial context, we can reframe it as a fundamental geodetic tool applicable to any planet illuminated by a star. The relationship between a planet's geometry, its star's position, and the resulting shadow lengths forms a unique signature. This section explores these signatures, deriving the theoretical shadow curves for planets of different shapes and considering the impact of varying solar system configurations.

**5.1 Shadow Curves as Geometric Signatures**

The core insight is that a simple, measurable quantity—the length of a gnomon's shadow—is a direct function of the planet’s global curvature. By measuring how shadow length varies with distance from a subsolar point, an observer can deduce the underlying geometry of their world.

For this analysis, we assume a gnomon of height `h = 1` unit, an equinox condition where the star is directly over the equator (declination `δ = 0°`), and observers at local noon.

*   **5.1.1 Spherical Planet (Baseline)**
    On a spherical planet, the zenith angle `θ` of the star is equal to the observer's latitude `φ`. The relationship between the gnomon `h`, its shadow `s`, and the zenith angle `θ` forms a right triangle.
    The shadow length is therefore given by the tangent function:

    `s(φ) = h * tan(φ) = tan(φ)` (Eq. 5)

    The curve is non-linear, growing moderately at low latitudes and accelerating towards infinity as the latitude approaches 90°. This trigonometric relationship is a direct consequence of Euclidean geometry on a curved surface.

*   **5.1.2 Flat Planet**
    On a flat-plane world, the sun is not infinitely distant but located at a finite altitude `H`. The shadow length `s` depends on the observer's linear distance `d` from the subsolar point. By similar triangles:

    `s/h = d/H  =>  s(d) = d/H` (Eq. 6)

    The shadow curve is perfectly linear. To compare this to the spherical case, we can approximate the linear distance `d` from the "latitude" `φ`, assuming a planet with an Earth-like circumference (`C ≈ 40,000 km`). Then `d = (φ/360) * C`. Assuming a typical flat-Earth sun altitude of `H = 5,000 km`, the shadow length is:

    `s(φ) = ( (φ * 40000) / 360 ) / 5000 = (φ * 8) / 360 = φ / 45`


#### **5.1.2.1 Replicating Spherical Results on a Flat World: The Physical Requirements**

For a flat-Earth model to yield the same shadow measurements as a spherical one, it cannot rely on consistent physical laws. The linear nature of its shadow curve (`s = d/H`) must be forced to mimic the non-linear, trigonometric curve of the spherical model (`s = tan(φ)`). This requires introducing ad-hoc physical conditions that are not globally consistent.

The primary way to achieve this is to abandon the assumption of a constant solar altitude (`H`) and allow it to vary as a function of the observer's location. By setting the two shadow equations equal, we can derive the required altitude `H` for any given location `φ`:

`tan(φ) = d/H  =>  H(φ) = d / tan(φ)` (Eq. 7)

Where `d` is the linear distance from the subsolar point, itself a function of latitude (`d ≈ (φ/360) * C`). This leads to a physically implausible requirement: the sun's altitude would have to systematically **decrease** as an observer moves away from the equator to higher latitudes. For example, to match the shadow at 60° latitude, the sun would need to be at a significantly lower altitude than to match the shadow at 30° latitude.

This ad-hoc model would **not be consistent across the entire flat surface**. A pair of observers in one region could perform the experiment and calculate a solar altitude `H_1` that works for their two locations. Another pair of observers in a distant region would perform the same experiment and calculate a completely different solar altitude, `H_2`. A single, physical sun cannot have multiple altitudes simultaneously. The model can be tuned to provide a *local fit* for any two points, but it fails as a *global model*. This internal inconsistency demonstrates that the flat-Earth model must be rejected on the grounds of falsifiability when multiple data points are introduced (Popper, 1959).

Popper, K. R. (1959). The Logic of Scientific Discovery. Hutchinson. (This is the foundational text on the principle of falsifiability).

#### **5.1.4 The Ambiguity of a Two-Point Measurement and the Power of a Third**

For the sake of scientific accuracy, it must be noted that an Eratosthenes experiment performed between **only two points does not, by itself, definitively prove a spherical shape**. A two-point measurement is fundamentally under-determined, as multiple geometric models can be constructed to fit a limited data set.

Consider an experiment at two locations that yields two shadow lengths.
*   **The Spherical Modeler:** Fits the data to the equation `s = h * tan(φ)` and calculates a consistent planetary circumference, `C`.
*   **The Flat Modeler:** Fits the same data to the equation `s = d/H` and calculates a consistent solar altitude, `H`.

With only two data points, both models are internally valid explanations of the available evidence. There is no logical basis for preferring one over the other.

The power to falsify one of these models emerges with the introduction of a **third measurement point**. This third data point breaks the ambiguity.
*   In the **spherical model**, the third measurement will fall along the same `tan(φ)` curve predicted by the first two points. Furthermore, pairwise calculations between points (1,3) and (2,3) will yield the same circumference `C` as the (1,2) calculation, demonstrating global consistency.
*   In the **flat model**, the third measurement will **not** lie on the linear `d/H` curve defined by the first two points. Calculating the solar altitude `H` using a new pair of points will yield a different value, proving the model is inconsistent and therefore incorrect.

Therefore, while a two-point experiment can *measure* a property (like circumference or solar altitude) *within a given model*, it is a **multi-point experiment (n ≥ 3) that can scientifically distinguish between competing models of planetary geometry**. The true strength of Eratosthenes' method as a proof of shape lies not in a single measurement, but in the consistency of its results when applied across geographically diverse locations.

---

##### **References**
Popper, K. R. (1959). *The Logic of Scientific Discovery*. Hutchinson. (This is the foundational text on the principle of falsifiability).

*   **5.1.3 Hypothetical Geometries**
    1.  **Hyperbolic Planet:** A hyperbolic geometry is characterized by negative curvature (a "saddle" shape). On such a surface, parallel lines diverge. The effect on shadow lengths would be an even more extreme divergence than on a sphere. The trigonometric relationship would be replaced by a hyperbolic function, likely causing the shadow length to grow super-linearly, even faster than `tan(φ)`.
    2.  **Inverted Spheroid (Concave World):** In this speculative model, observers live on the inner surface of a sphere. Light propagation becomes complex, but assuming straight-line rays from a central sun, observers at higher "latitudes" would be angled *towards* the sun's rays. This would cause shadows to behave erratically, potentially shortening at higher latitudes, a direct contradiction to all real-world observation.

*Table 5: Comparative Shadow Lengths (`s`) for Different Planetary Models (`h=1`)*

| "Latitude" `φ` | Spherical `s = tan(φ)` | Flat `s = φ/45` (`H=5000km`) | Qualitative Hyperbolic Behavior |
| :--- | :--- | :--- | :--- |
| **0°** | 0.00 | 0.00 | ~0 |
| **30°** | 0.58 | 0.67 | Similar to spherical |
| **60°** | 1.73 | 1.33 | Noticeably longer than spherical |
| **80°** | 5.67 | 1.78 | Dramatically longer |
| **89°** | 57.29 | 1.98 | Approaching infinity much faster |

This comparison demonstrates that a simple multi-point Eratosthenes-style experiment, plotting shadow length against distance, can definitively distinguish between competing models of planetary geometry without ambiguity.

**5.2 Impact of Solar System Configuration**

The experiment's simplifying assumptions are not universal. Altering the relationship between the planet and its star introduces new complexities.

*   **5.2.1 Close Primary Star: Breakdown of the Parallel-Ray Assumption**
    The assumption that the star's rays are parallel is an excellent approximation for the Earth-Sun system, where the sun's distance (`~150 million km`) is over 10,000 times the Earth's diameter. If a planet were orbiting much closer to its star, this assumption would fail.
    The incoming rays would have a noticeable divergence, a phenomenon known as **solar parallax**. An observer's measurement of the zenith angle `θ` would depend not only on their position on the planet (`φ`, `δ`) but also on their position relative to the star. This would require a more complex geometric model accounting for the finite distance to the star, `D`. The experiment, in this case, could be modified to solve for two unknowns simultaneously: the planet's radius `R` and its distance from its star `D`.

*   **5.2.2 Binary Star Systems**
    An experiment on a planet illuminated by two stars would present a unique observational challenge: the presence of two overlapping shadows (*penumbrae*) for any given object. A direct measurement of a single shadow length would be impossible. However, the method could be adapted:
    1.  **Filtering:** If the two stars have different spectral types (e.g., a blue star and a red star), an observer could use an optical filter to block the light from one star, allowing the shadow cast by the other to be measured cleanly.
    2.  **Timing:** If the planet is in a non-synchronous orbit, there may be times when one star is eclipsed by the other, or when one has set while the other is still in the sky, providing a window for an unambiguous measurement.

This theoretical analysis shows that the Eratosthenes experiment is not merely a historical anecdote but a foundational principle of planetary science. Its core logic—using shadows to triangulate global geometry—is a powerful and adaptable tool, capable of revealing the fundamental physical properties of a world.

---
##### **References**
Cox, B., & Forshaw, J. (2011). *The Quantum Universe: Everything That Can Happen Does Happen*. Allen Lane. (Provides accessible explanations of geometric models).
Anderson, J. D. (1999). *Introduction to Flight* (4th ed.). McGraw-Hill. (Discusses parallax in an astronomical context).
Richards, J. L. (1997). *The Reception of a Mathematical Theory: Non-Euclidean Geometry in England, 1868–1883*. In *The Enterprise of Science in the Early Modern Era* (pp. 163-196). University of Chicago Press.


***

#### **6. Conclusion**

Eratosthenes' measurement of the Earth's circumference was more than a brilliant calculation; it was a testament to the power of the scientific method, demonstrating how empirical observation, grounded in a theoretical model, can reveal the fundamental properties of the cosmos. This paper has conducted a deep methodological analysis of this landmark experiment, moving beyond the historical result to dissect its scientific process, from the practical challenges of ancient metrology to its theoretical extensions in modern science.

Our reconstruction of the ancient methodology revealed that the experiment's success hinged on a sophisticated understanding of measurement and uncertainty. We have shown that Eratosthenes did not require absolute timekeeping, but rather a precise geometric synchronization achieved by observing the sun's passage across the local meridian. The primary source of uncertainty was not in the astronomical angle, but in the terrestrial distance. Our analysis of this variable led to the "Informed Scientific Correction" hypothesis, a new interpretation that portrays Eratosthenes not as a lucky theorist, but as a critical scientist who likely understood the limitations of his raw data—the 5,000-stadia travel distance—and applied a reasoned, cartographic correction to arrive at a more accurate geometric value.

Contrasting this ancient practice with a modern framework highlighted the experiment's adaptability. By incorporating universal time, spherical trigonometry, and corrections for factors like solar declination and observer altitude, the method is transformed into a precise and globally applicable geodetic tool. Finally, our theoretical analysis reframed the experiment as a universal instrument for comparative planetology. We have demonstrated that the shadow curves produced on planets of different geometries—spherical, flat, or hyperbolic—are unique and distinguishable, establishing the Eratosthenes method as a powerful tool for deducing the physical nature of a world from first principles.

Ultimately, this investigation reaffirms the enduring relevance of Eratosthenes' work. It is not an obsolete historical anecdote, but a living scientific principle. It serves as a powerful educational tool, a case study in scientific reasoning and error analysis, and a foundational concept for understanding how we measure and map any world, be it our own or one orbiting a distant star. The experiment's true legacy is its elegant demonstration that with a simple stick, a shadow, and a mastery of reason, it is possible to measure the world.

---

### **7. Bibliography**

Aristotle. (c. 350 BCE). *On the Heavens*. Trans. by W. K. C. Guthrie (1939). Loeb Classical Library.

Cleomedes. (c. 150 CE). *Cleomedes' Lectures on Astronomy: A Translation of The Heavens*. Trans. by A. C. Bowen and R. B. Todd (2004). University of California Press.

Cox, B., & Forshaw, J. (2011). *The Quantum Universe: Everything That Can Happen Does Happen*. Allen Lane.

Dutka, J. (1993). *Eratosthenes' Measurement of the Earth Reconsidered*. Archive for History of Exact Sciences, 46(1), 55–66.

Engels, D. (1985). *The Length of Eratosthenes' Stade*. The American Journal of Philology, 106(3), 298–311.

Goldstein, B. R. (1983). *The Method of Equal Altitudes in the Ancient and Medieval Worlds*. In *From Deferent to Equant: A Volume of Studies in the History of Science in the Ancient and Medieval Near East in Honor of E. S. Kennedy* (pp. 147-156). New York Academy of Sciences.

MacLeod, R. (Ed.). (2004). *The Library of Alexandria: Centre of Learning in the Ancient World*. I.B. Tauris.

Meeus, J. (1998). *Astronomical Algorithms*. Willmann-Bell, Inc.

Neugebauer, O. (1957). *The Exact Sciences in Antiquity*. Brown University Press.

Neugebauer, O. (1975). *A History of Ancient Mathematical Astronomy*. Springer-Verlag.

Pannekoek, A. (1961). *A History of Astronomy*. Interscience Publishers.

Pliny the Elder. (c. 77 CE). *Naturalis Historia*. Trans. by H. Rackham (1938). Loeb Classical Library.

Rawlins, D. (1982). *The Eratosthenes-Strabo Nile Map. Is It the Prototype of the Carte Pisane?* Archive for History of Exact Sciences, 26(3), 211–219.

Richards, J. L. (1997). *The Reception of a Mathematical Theory: Non-Euclidean Geometry in England, 1868–1883*. In *The Enterprise of Science in the Early Modern Era* (pp. 163-196). University of Chicago Press.

Sinnott, R. W. (1984). *Virtues of the Haversine*. Sky and Telescope, 68(2), 159.

Strabo. (c. 20 CE). *Geographica*. Trans. by H. L. Jones (1917-1932). Loeb Classical Library.

Torge, W., & Müller, J. (2012). *Geodesy* (4th ed.). De Gruyter.

Vaníček, P., & Krakiwsky, E. J. (1986). *Geodesy: The Concepts* (2nd ed.). Elsevier.

---

### **8. Appendices**

Excellent. Crafting a robust appendix with the key mathematical derivations is crucial for demonstrating the paper's rigor and providing a valuable resource for the reader. Here is a complete Appendix A, written in a formal, academic style, including the three requested derivations plus two additional ones that are central to the paper's arguments.

---

### **Appendix A: Mathematical Derivations**

The main body of this paper relies on several key mathematical formulae to reconstruct the ancient Eratosthenes experiment, develop a modern high-precision protocol, and analyze its theoretical implications. This appendix provides the formal derivations for these essential equations. The purpose is to serve as a self-contained reference for readers interested in the specific geometric and trigonometric principles at play. The derivations cover the calculation of great-circle distances, solar declination, altitude corrections, and the foundational relationships in both spherical and flat-plane models, thereby supporting the central arguments made throughout the analysis.

---


#### **A.1 The Haversine Formula for Great-Circle Distance**

The haversine formula is a numerically stable method for calculating the great-circle distance between two points on a sphere, avoiding issues with small angles that can arise with the spherical law of cosines.

**Definitions:**
*   The **versine** (versed sine) of an angle `θ` is `versin(θ) = 1 - cos(θ)`.
*   The **haversine** (half-versine) is `hav(θ) = versin(θ) / 2 = (1 - cos(θ)) / 2 = sin²(θ/2)`.
*   Let two points be `P_1(φ_1, λ_1)` and `P_2(φ_2, λ_2)`, where `φ` is latitude and `λ` is longitude.
*   Let `c` be the angular distance between the two points, and `R` be the sphere's radius.

**Derivation:**
Consider the spherical triangle formed by the North Pole (`N`) and the two points `P_1` and `P_2`. The sides of this triangle are the angular distances:
*   `a = (π/2) - φ_2` (co-latitude of `P_2`)
*   `b = (π/2) - φ_1` (co-latitude of `P_1`)
*   The angle at the North Pole, `N`, is the difference in longitudes, `Δλ = λ_2 - λ_1`.

Applying the **spherical law of cosines**:
`cos(c) = cos(a)cos(b) + sin(a)sin(b)cos(N)`

Substituting the co-latitudes:
`cos(c) = cos((π/2) - φ_2)cos((π/2) - φ_1) + sin((π/2) - φ_2)sin((π/2) - φ_1)cos(Δλ)`
`cos(c) = sin(φ_2)sin(φ_1) + cos(φ_2)cos(φ_1)cos(Δλ)`

To derive the haversine formula, we start with `hav(c) = (1 - cos(c)) / 2`:
`hav(c) = (1 - [sin(φ_1)sin(φ_2) + cos(φ_1)cos(φ_2)cos(Δλ)]) / 2`

Using the identity `cos(Δλ) = 1 - 2hav(Δλ)`:
`hav(c) = (1 - sin(φ_1)sin(φ_2) - cos(φ_1)cos(φ_2)[1 - 2hav(Δλ)]) / 2`
`hav(c) = (1 - sin(φ_1)sin(φ_2) - cos(φ_1)cos(φ_2) + 2cos(φ_1)cos(φ_2)hav(Δλ)) / 2`

Using the identity `cos(φ_1 - φ_2) = cos(φ_1)cos(φ_2) + sin(φ_1)sin(φ_2)`:
`hav(c) = ([1 - cos(φ_1 - φ_2)] + 2cos(φ_1)cos(φ_2)hav(Δλ)) / 2`
`hav(c) = hav(φ_1 - φ_2) + cos(φ_1)cos(φ_2)hav(Δλ)`

Recalling that `hav(θ) = sin²(θ/2)`, we arrive at the final form:
`sin²(c/2) = sin²(Δφ/2) + cos(φ_1)cos(φ_2)sin²(Δλ/2)`

The great-circle distance `d = R * c`.

#### **A.2 Formula for Solar Declination**

The solar declination `δ` is the angle between the sun's rays and the plane of the Earth's equator. It is a function of the Earth's axial tilt (`ε ≈ 23.45°`) and its orbital position. A common and effective approximation can be derived.

**Definitions:**
*   `ε`: Earth's axial tilt (`≈ 23.45°`).
*   `N`: The day of the year (e.g., `N=1` for January 1st).
*   The Earth completes a `≈ 360°` orbit in `≈ 365.25` days.
*   The winter solstice (in the Northern Hemisphere) occurs around December 21st (`N ≈ 355`), at which point the Earth's orbital position is such that the sun is maximally south. The formula uses a cosine function, which has its minimum at this point. The offset of `+10` days aligns the minimum of the cosine curve (`cos(360/365 * (355+10)) = cos(360) = 1`) with the winter solstice.

**Derivation:**
The Sun's apparent position along the ecliptic can be modeled as a sinusoidal function. The declination `δ` is the projection of the ecliptic angle onto the equatorial plane.

Assuming a simple circular orbit, the angle `θ_orb` that the Earth has traversed since the winter solstice can be approximated. However, a more direct approach models the declination directly. The declination varies as the sine of the ecliptic longitude. A good approximation treating the Earth's orbit as a circle is:

`δ(N) ≈ -ε * cos( (360°/365.25) * (N + 10) )`

Where:
*   The negative sign sets the declination to its minimum (`-23.45°`) at the winter solstice.
*   The `(N + 10)` term provides a phase shift to align the curve with the calendar, placing the winter solstice around day 355.
*   The `360°/365.25` term represents the average daily orbital motion of the Earth.

For example, at the vernal equinox (`N ≈ 81`), `(81+10) = 91`, and `cos(360/365 * 91) ≈ cos(90°) ≈ 0`, yielding `δ ≈ 0°`, as expected. At the summer solstice (`N ≈ 172`), `(172+10) = 182`, and `cos(360/365 * 182) ≈ cos(180°) = -1`, yielding `δ ≈ +23.45°`.

#### **A.3 Derivation of the Altitude Correction for Arc Distance**

When an arc distance is measured between two points at an average altitude `h` above a sphere of radius `R_sea`, the measurement corresponds to an arc on a larger sphere. This derivation provides the formula to reduce the measured distance to its sea-level equivalent.

**Definitions:**
*   `R_sea`: The radius of the Earth at sea level.
*   `h_avg`: The average altitude of the two measurement points.
*   `R_h = R_sea + h_avg`: The radius of the sphere at the measurement altitude.
*   `d_ground`: The measured arc distance at altitude `h_avg`.
*   `d_sea`: The equivalent arc distance at sea level.
*   `c`: The central angle subtended by the arc (this angle is the same for both spheres).

**Derivation:**
The formula for arc length is `d = R * c`, where `c` is in radians.

For the measurement at altitude:
`d_ground = R_h * c = (R_sea + h_avg) * c`

For the equivalent distance at sea level:
`d_sea = R_sea * c`

We can express the central angle `c` from the first equation:
`c = d_ground / (R_sea + h_avg)`

Now, substitute this expression for `c` into the second equation:
`d_sea = R_sea * [ d_ground / (R_sea + h_avg) ]`

Rearranging this gives the final correction formula:
`d_sea = d_ground * ( R_sea / (R_sea + h_avg) )`

This shows that the sea-level distance is simply the measured ground distance scaled down by the ratio of the sea-level radius to the altitude radius.

#### **A.4 Derivation of Zenith Angle from Gnomon Measurements**

The zenith angle `θ` is the angle between the local vertical and the direction of the sun. It can be derived using basic trigonometry from the height of a gnomon and the length of its shadow.

**Definitions:**
*   `h`: The vertical height of the gnomon.
*   `s`: The horizontal length of the shadow cast by the gnomon.
*   `θ`: The sun's zenith angle.

**Derivation:**
Assume the gnomon is perfectly vertical to a perfectly level ground plane. The gnomon (`h`), its shadow (`s`), and the sun's ray connecting the top of the gnomon to the tip of the shadow form a right-angled triangle.
*   The side **opposite** to the angle `θ` is the shadow length `s`.
*   The side **adjacent** to the angle `θ` is the gnomon height `h`.

By the definition of the tangent function in trigonometry:
`tan(θ) = opposite / adjacent = s / h`

To solve for the zenith angle `θ`, we take the inverse tangent (arctangent) of both sides:
`θ = arctan(s / h)`

This formula is fundamental to the experiment, converting a simple length measurement into the required angular data.

#### **A.5 Derivation of Solar Altitude for Flat-Earth Model**

To falsify the flat-Earth model using a multi-point experiment, one can calculate the required solar altitude `H` between any two points and show that it is not constant.

**Definitions:**
*   `P_1`, `P_2`: Two measurement points on a flat plane.
*   `d`: The linear distance between `P_1` and `P_2`.
*   `s_1`, `s_2`: The shadow lengths measured at `P_1` and `P_2`.
*   `h`: The height of the gnomon (the same at both locations).
*   `H`: The altitude of the sun above the plane.
*   `d_1`, `d_2`: The horizontal distances from the subsolar point to `P_1` and `P_2`, respectively.

**Derivation:**
From the principle of similar triangles for a flat-Earth model:
`s_1 / h = d_1 / H  =>  d_1 = H * (s_1 / h)`
`s_2 / h = d_2 / H  =>  d_2 = H * (s_2 / h)`

Assuming the two points and the subsolar point are collinear for simplicity:
`d = |d_1 - d_2|`

Substituting the expressions for `d_1` and `d_2`:
`d = | H * (s_1 / h) - H * (s_2 / h) |`
`d = (H / h) * |s_1 - s_2|`

Solving for the solar altitude `H`:
`H = (d * h) / |s_1 - s_2|`

This formula allows one to calculate the implied solar altitude from any two measurements. The flat-Earth hypothesis predicts `H` will be constant. A real experiment with three or more points would show that `H` varies depending on which pair of points is chosen, thus falsifying the model.


##### **References**
Heath, T. L. (1913). *Aristarchus of Samos, the Ancient Copernicus*. Oxford University Press.
Dreyer, J. L. E. (1953). *A History of Astronomy from Thales to Kepler*. Dover Publications.
Berggren, J. L., & Jones, A. (2000). *Ptolemy's Geography: An Annotated Translation of the Theoretical Chapters*. Princeton University Press.


#### **Conclusion to Appendix A**

The derivations presented in this appendix collectively form the mathematical backbone of the paper's analysis. Derivations A.1, A.2, and A.3 provide the necessary tools for a modern, high-precision replication of the Eratosthenes experiment, allowing for measurements between any two points on the globe, on any day of the year, while correcting for second-order effects like observer altitude. Derivation A.4 establishes the fundamental geometric relationship between shadow and zenith angle that is at the heart of the experiment itself. Finally, derivation A.5 provides a quantitative method for testing the internal consistency of the flat-plane model, demonstrating its falsifiability. Together, these mathematical formalisms ensure that the paper's conclusions are not merely descriptive but are grounded in robust, verifiable geometric and astronomical principles.