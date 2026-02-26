def apply_filters(planet, DEC_MIN, DEC_MAX, SNR_LIM):
    """
    Apply final observability filters to a planet candidate.

    A planet is considered observable only if its declination lies within
    the allowed range and its signal to noise ratio exceeds the required limit.

    This function is designed to be used inside iteration loops or list
    comprehensions.

    Parameters
    planet
    Dictionary containing enriched planet parameters

    DEC_MIN
    Minimum allowed declination in degrees

    DEC_MAX
    Maximum allowed declination in degrees

    SNR_LIM
    Minimum acceptable signal to noise ratio

    Returns
    True if planet passes all filters otherwise False
    """

    dec_ok = DEC_MIN <= planet['Dec'] <= DEC_MAX
    snr_ok = planet['SNR'] >= SNR_LIM
    return dec_ok and snr_ok

