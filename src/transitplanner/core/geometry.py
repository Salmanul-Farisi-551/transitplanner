from astropy.coordinates import SkyCoord, EarthLocation, AltAz
import astropy.units as u

def radec_to_altaz(ra, dec, location, obstime):
    coord = SkyCoord(ra=ra, dec=dec, unit=(u.hourangle, u.deg))
    altaz = coord.transform_to(AltAz(obstime=obstime, location=location))
    return altaz.alt.deg, altaz.az.deg
