# Imports
import urllib.request, json
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive
import matplotlib.pyplot as plt
import pandas as pd
from .core.visibility import find_observable_exoplanets
from .observability.enrich import enrich_planets
from .observability.snr import snr_formula
from .observability.summary import check_observability_table
from .lightcurve.simulator import generate_lightcurve
from .lightcurve.plotting import plot_lightcurve
from .io.nasa import load_nasa_data

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

    # 1. Visibility stage
    planet_list = find_observable_exoplanets(
        longitude,
        latitude,
        start_date_str,
        span_days,
        min_altitude,
        telescope_aperture_inches
    )

    if not planet_list:
        print("No transits found in the observing window.")
        return

    # 2. Load catalogues
    url = "https://www.exoclock.space/database/planets_json"
    exoclock_planets = json.loads(urllib.request.urlopen(url).read())

    
    nasa=load_nasa_data()
    # 3. Enrich planet data
    planet_list = enrich_planets(planet_list, exoclock_planets, nasa)

    # 4. Compute SNR and observability
    for planet in planet_list:
        duration_min = planet["Duration (hours)"] * 60

        planet["SNR"] = snr_formula(
            planet["R Magnitude"],
            planet["Transit Depth (mmag)"],
            duration_min,
            telescope_aperture_inches
        )

        planet["Status"] = (
            "Observable"
            if DEC_MIN <= planet["Dec"] <= DEC_MAX and planet["SNR"] >= SNR_LIM
            else "Not Observable"
        )
         
      print(f"\n--- Observability Check for {planet['Object']} ---")
      print(f"Host star: {planet['Object']}")
      print(f"Rp/Rs: {RpRs:.4f}")
      print(f"a/Rs: {aRs:.2f}")
      print(f"Inclination: {inc_deg:.2f} deg")
      print(f"Transit depth: {depth_mmag:.2f} mmag")
      print(f"Transit duration: {duration_min:.1f} min ({duration_hours:.3f} hours)")
      print(f"R magnitude (merged): {Rmag:.2f}")
      print(f"SNR: {snr:.2f}")
      print(f"RA/DEC: {RA}, {DEC:.2f}°")
      print(f"Status: {status}")
    # 5. Summary table
    check_observability_table(
        planet_list,
        export_csv="exoplanet_summary.csv",
        export_excel="exoplanet_summary.xlsx"
    )

    # 6. Select observable planets
    observable_planets = [p for p in planet_list if p["Status"] == "Observable"]

    if not observable_planets:
        print("No observable planets in the selected window.")
        return

    print("Observable planets:")
    for i, planet in enumerate(observable_planets):
        print(f"{i+1}. {planet['Object']} - Transit at {planet['Transit Start (UTC)']}")

    selection = int(input("Select planet number to model: ")) - 1
    target_name = observable_planets[selection]["Object"]

    # 7. Light curve
    obstime, flux, depth = generate_lightcurve(target_name)
    plot_lightcurve(obstime, flux, title=f"{target_name} Predicted Light Curve")


if __name__ == "__main__":
    main()






