import math
from ..constants import A_CONST

def snr_formula(Rmag, depth_mmag, duration_min, telescope_aperture_inches=1.0):
    """
    Compute an approximate signal to noise ratio for a transit observation.

    The formula estimates SNR using stellar magnitude, transit depth,
    observation duration and telescope aperture. 

    Parameters
    Rmag
    R band magnitude of the host star

    depth_mmag
    Transit depth in millimagnitudes

    duration_min
    Transit duration in minutes

    telescope_aperture_inches
    Telescope aperture diameter in inches

    Returns
    Estimated signal to noise ratio
    """

    return (A_CONST * telescope_aperture_inches *
            math.sqrt(10 ** ((12.0 - Rmag) / 2.5)) *
            depth_mmag / math.sqrt((1.0 / duration_min) + (1.0 / 120.0)))

