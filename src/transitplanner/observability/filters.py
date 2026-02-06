def apply_filters(planet, DEC_MIN, DEC_MAX, SNR_LIM):
    dec_ok = DEC_MIN <= planet['Dec'] <= DEC_MAX
    snr_ok = planet['SNR'] >= SNR_LIM
    return dec_ok and snr_ok
