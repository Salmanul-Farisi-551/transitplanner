# Imports
from .core.visibility import find_observable_exoplanets
from .observability.snr import snr_formula
from .observability.summary import check_observability_table
from .lightcurve.simulator import generate_lightcurve
from .lightcurve.plotting import plot_lightcurve
import matplotlib.pyplot as plt

def main():
    # User inputs
    longitude = float(input("Enter longitude (degrees): "))
    latitude = float(input("Enter latitude (degrees): "))
    telescope_aperture_inches = float(input("Enter telescope aperture (inches): "))
    DEC_MIN = float(input("Enter min declination (deg): "))
    DEC_MAX = float(input("Enter max declination (deg): "))
    SNR_LIM = float(input("Enter min SNR: "))
    start_date_str = input("Enter start date (dd/mm/yy): ")
    span_days = int(input("Enter observation span (days): "))
    min_altitude = float(input("Enter min altitude (deg): "))

    # Find planets in observing window
    planet_list = find_observable_exoplanets(
        longitude, latitude, start_date_str, span_days,
        min_altitude, telescope_aperture_inches
    )

    # Compute SNR and status
    for planet in planet_list:
        duration_min = planet["Duration (hours)"] * 60
        planet['SNR'] = snr_formula(
            planet["R Magnitude"], planet["Transit Depth (mmag)"], duration_min,
            telescope_aperture_inches
        )
        planet['Status'] = "Observable" if DEC_MIN <= planet['Dec'] <= DEC_MAX and planet['SNR'] >= SNR_LIM else "Not Observable"

    # Filter observable planets
    observable_planets = [p for p in planet_list if p['Status'] == "Observable"]
    if not observable_planets:
        print("No observable planets in window.")
        return

    # Show list and let user pick
    print("Observable planets:")
    for i, planet in enumerate(observable_planets):
        print(f"{i+1}. {planet['Object']} - Transit at {planet['Transit Start (UTC)']}")

    selection = int(input("Select planet number to model: ")) - 1
    target_name = observable_planets[selection]['Object']

    # Generate light curve
    obstime, flux, depth = generate_lightcurve(target_name)

    # Plot
    plot_lightcurve(obstime, flux, title=f"{target_name} Predicted Light Curve")

if __name__ == "__main__":
    main()
