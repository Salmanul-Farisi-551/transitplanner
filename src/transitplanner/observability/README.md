

This module retrieves transit and stellar parameters for a selected exoplanet
from both the ExoClock catalogue and the NASA Exoplanet Archive. The two sources
are merged into a single consistent dataset.

When both sources provide the same parameter, NASA values are prioritised.
ExoClock values are used only when the NASA value is missing or NaN.

After merging, the module computes an approximate signal to noise ratio using
stellar magnitude, transit depth, transit duration and telescope parameters.
The final observability decision is based on both SNR and declination limits.

Main responsibilities:

Load ExoClock planet data
Load NASA Exoplanet Archive data

Merge parameters using a NASA first rule

Handle unit differences such as minutes vs hours and fractional depth vs mmag

Compute SNR for each planet

Determine observability based on SNR and declination constraints

