import urllib.request, json
from datetime import datetime, timedelta
import numpy as np
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astroplan import Observer
import astropy.units as u

def find_observable_exoplanets(longitude, latitude, start_date_str, span_days,
                               min_altitude, telescope_aperture_inches):
    # Full function code from your main script
    ...
