import math
from ..constants import A_CONST

def snr_formula(Rmag, depth_mmag, duration_min, telescope_aperture_inches=1.0):
    return (A_CONST * telescope_aperture_inches *
            math.sqrt(10 ** ((12.0 - Rmag) / 2.5)) *
            depth_mmag / math.sqrt((1.0 / duration_min) + (1.0 / 120.0)))
