Lightcurve Simulation Module

This module generates a predicted transit lightcurve for a selected exoplanet.
It uses the ExoClock catalogue through pylightcurve to obtain transit parameters
and models the expected flux variation during transit.

The module takes the planet name and the estimated SNR from previous modules.
It computes the observation time window, relative flux, transit depth and
measurement uncertainty.

The final output includes printed transit properties and a plotted model
lightcurve with representative error bars.

Main responsibilities:

Retrieve planet transit parameters from ExoClock,
Generate time array covering full transit and baseline,
Compute relative flux and magnitude depth,
Estimate observational error from SNR,
Produce a plotted lightcurve

