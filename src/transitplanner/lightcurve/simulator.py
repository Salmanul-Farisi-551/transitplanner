import numpy as np
import pylightcurve as plc

def generate_lightcurve(planet_name, filter='COUSINS_R'):
    planet = plc.get_planet(planet_name)
    startend = float('{:.3f}'.format((planet.transit_duration(filter) / 2) + 0.0417))
    time_array = np.arange(planet.mid_time - startend, planet.mid_time + startend, 0.001)
    obstime = (time_array - time_array[0]) * 24
    transit_flux = planet.transit(time_array, 'BJD_TDB', filter)
    return obstime, transit_flux, np.max(-2.5*np.log10(transit_flux/100)) - np.min(-2.5*np.log10(transit_flux/100))
