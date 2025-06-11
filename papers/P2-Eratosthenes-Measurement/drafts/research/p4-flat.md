Q: How inconsistent results would be on flat earth? Provide rigorous calculation how the curve of lengths of shadows would differ on spheroid, flat earth, inverted spheroid etc. why is the result exponential powercurve, in case of spheroid? Is it connected to sun position or ecliptic?

A: Below is a detailed and self-contained response to your query about shadow length behavior on different Earth models, addressing the inconsistency on a flat Earth, the curve of shadow lengths across various models, and why the curve on a spheroid is trigonometric (not exponential), along with its connection to the sun’s position and ecliptic.

---

### How Inconsistent Would Results Be on a Flat Earth?

On a flat Earth, shadow lengths would behave differently from what we observe in reality, leading to inconsistent results when compared to measurements taken across different locations. This inconsistency arises because shadow lengths on a flat Earth increase linearly with distance from the point directly beneath the sun (the subsolar point), whereas real-world observations show a non-linear increase consistent with a spherical Earth.

To understand this, consider a simple experiment like Eratosthenes’ measurement of the Earth’s circumference. He used shadow lengths at two locations (Syene and Alexandria) to calculate the Earth’s curvature, assuming a spherical shape. On a flat Earth, the same method would yield varying "circumferences" depending on the locations chosen, because the linear shadow behavior does not match the geometry of a sphere.

- **Flat Earth Model**: Imagine the sun is at a fixed height \( H \) (e.g., 5,000 km, a common flat Earth assumption) above a flat plane. At the subsolar point (where the sun is directly overhead), a vertical stick (gnomon) of height \( h \) casts no shadow. As you move a distance \( d \) away, the shadow length \( s \) is determined by similar triangles:
  \[
  s = h \cdot \frac{d}{H}
  \]
  This is a linear relationship—shadow length increases directly proportional to distance.

- **Real-World Observation**: In reality, shadow lengths grow faster than linearly with distance from the subsolar point, following a trigonometric pattern (explained below). For example, at higher latitudes, shadows lengthen much more rapidly than a flat Earth model predicts, leading to discrepancies when trying to infer global properties like circumference.

- **Inconsistency Example**: If you measure shadows at two points (e.g., 30° and 60° "latitude" equivalents) on a flat Earth and assume the linear model, then use those to calculate a circumference (as Eratosthenes did), the result would differ from a measurement at, say, 10° and 80°. On a spherical Earth, the trigonometric relationship ensures consistency across all latitudes, matching observations.

Thus, the flat Earth model fails to replicate the consistent, non-linear shadow behavior seen globally, making results inconsistent when applied to real-world data.

---

### How Does the Curve of Shadow Lengths Differ Across Models?

Let’s rigorously calculate and compare how shadow lengths behave on a spherical Earth, a flat Earth, and an inverted spheroid, using a gnomon of height \( h = 1 \) meter for simplicity. We’ll assume the equinox at local noon (sun directly above the equator) to standardize conditions.

#### 1. Spherical Earth
On a spherical Earth, shadow length depends on the zenith angle \( \theta \), the angle between the sun’s rays and the vertical. At the equinox at noon:
- The zenith angle \( \theta \) equals the latitude \( \phi \) (in degrees or radians, depending on context).
- Shadow length \( s \) is:
  \[
  s = h \cdot \tan(\theta) = h \cdot \tan(\phi)
  \]
- **Behavior**: The tangent function creates a non-linear curve. For small \( \phi \), \( \tan(\phi) \approx \phi \) (in radians), so \( s \) is nearly linear. As \( \phi \) approaches 90°, \( \tan(\phi) \) approaches infinity, causing a rapid increase.

**Example Calculations**:
- \( \phi = 0^\circ \): \( s = 1 \cdot \tan(0^\circ) = 0 \) m
- \( \phi = 30^\circ \): \( s = 1 \cdot \tan(30^\circ) = \frac{1}{\sqrt{3}} \approx 0.577 \) m
- \( \phi = 60^\circ \): \( s = 1 \cdot \tan(60^\circ) = \sqrt{3} \approx 1.732 \) m
- \( \phi = 80^\circ \): \( s = 1 \cdot \tan(80^\circ) \approx 5.671 \) m

#### 2. Flat Earth
On a flat Earth, assume the sun is at height \( H = 5,000 \) km. The distance \( d \) from the subsolar point relates to an equivalent "latitude" \( \phi \) (in degrees) by approximating \( d \) as an arc length on a circle of Earth’s equatorial circumference (~40,000 km):
- \( d = \frac{\phi}{360} \times 40,000 \) km
- Shadow length:
  \[
  s = h \cdot \frac{d}{H} = 1 \cdot \frac{\frac{\phi}{360} \times 40,000}{5,000} = \frac{\phi}{360} \times 8 = \frac{\phi}{45} \) m
- **Behavior**: This is strictly linear—shadow length increases proportionally with \( \phi \).

**Example Calculations**:
- \( \phi = 0^\circ \): \( s = \frac{0}{45} = 0 \) m
- \( \phi = 30^\circ \): \( s = \frac{30}{45} = 0.667 \) m
- \( \phi = 60^\circ \): \( s = \frac{60}{45} = 1.333 \) m
- \( \phi = 80^\circ \): \( s = \frac{80}{45} \approx 1.778 \) m

#### 3. Inverted Spheroid (Concave Earth)
An inverted spheroid, where the Earth is a concave surface with the sun inside, is speculative and less defined. However, we can hypothesize:
- Light rays might converge or diverge due to the inward curvature.
- Shadow length could follow an inverse trigonometric or hyperbolic function, depending on the geometry. For example, if the sun is at the center of a concave sphere, shadows might shorten near the "edges" (high latitudes) as rays bend inward, unlike the spherical or flat models.
- **Behavior**: The curve could be concave or convex, but it’s unlikely to match the observed tangent curve without specific adjustments.

**Comparison**:
| Latitude (\( \phi \)) | Spherical (\( s = \tan(\phi) \)) | Flat (\( s = \frac{\phi}{45} \)) | Inverted Spheroid (Hypothetical) |
|-----------------------|----------------------------------|-------------------------------|-----------------------------------|
| 0°                   | 0 m                             | 0 m                          | ~0 m (varies by model)           |
| 30°                  | 0.577 m                         | 0.667 m                      | Potentially shorter/longer       |
| 60°                  | 1.732 m                         | 1.333 m                      | Potentially non-linear           |
| 80°                  | 5.671 m                         | 1.778 m                      | Potentially divergent            |

- **Spherical**: Rapid non-linear increase, matches observations.
- **Flat**: Linear increase, underestimates at high latitudes.
- **Inverted Spheroid**: Unclear without a precise model, but unlikely to fit observed data consistently.

---

### Why Is the Curve Trigonometric, Not Exponential, on a Spheroid?

You asked why the shadow length curve on a spheroid is an "exponential powercurve." This seems to be a misunderstanding—the curve is **trigonometric**, not exponential, due to the geometry of a sphere.

- **Trigonometric Basis**: On a spherical Earth, the shadow length \( s = h \cdot \tan(\phi) \) comes from the right triangle formed by the gnomon, its shadow, and the sun’s rays. The tangent function is trigonometric, tied to angles and circular geometry, not exponential growth (e.g., \( e^x \)).
- **Exponential Misconception**: Exponential functions grow much faster (e.g., \( e^\phi \)) than \( \tan(\phi) \), which only approaches infinity at 90°. The rapid increase of \( \tan(\phi) \) might resemble exponential growth superficially, but it’s fundamentally different.
- **Evidence**: Observations (e.g., Eratosthenes’ measurements) fit \( \tan(\phi) \), not an exponential model.

---

### Connection to Sun’s Position or Ecliptic?

The sun’s position and the ecliptic influence the shadow curve but do not change its trigonometric nature:
- **Sun’s Position**: At the equinox, the sun is above the equator (\( \delta = 0^\circ \)), so \( \theta = \phi \). On other days, the sun’s declination \( \delta \) shifts, making \( \theta = |\phi - \delta| \), but the formula remains \( s = h \cdot \tan(\theta) \)—still trigonometric.
- **Ecliptic**: The ecliptic (the sun’s apparent path) affects \( \delta \) over the year, altering \( \theta \), but the core relationship is governed by the spherical geometry, not the ecliptic itself.

Thus, the sun and ecliptic adjust the specific angles, but the trigonometric form arises from the Earth’s curvature.

---

### Conclusion

- **Flat Earth Inconsistency**: Shadow lengths increase linearly (\( s = h \cdot \frac{d}{H} \)), clashing with the non-linear, trigonometric increase seen in reality, leading to inconsistent global measurements.
- **Curve Differences**: Spherical Earth follows \( s = h \cdot \tan(\phi) \) (non-linear, trigonometric); flat Earth follows \( s = h \cdot \frac{d}{H} \) (linear); inverted spheroid is speculative but likely non-matching.
- **Trigonometric, Not Exponential**: The spheroid’s curve is \( \tan(\phi) \), not exponential, due to spherical geometry.
- **Sun/Ecliptic Role**: They modify the zenith angle but don’t alter the trigonometric relationship.

This analysis, grounded in math and observation, strongly supports the spherical Earth model over alternatives.