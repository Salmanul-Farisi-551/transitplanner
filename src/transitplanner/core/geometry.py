from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u

def radec_to_altaz(coord, location, obstime):
    altaz = coord.transform_to(AltAz(obstime=obstime, location=location))
    return altaz.alt.deg, altaz.az.deg

