def dec_to_deg(dec_str):
    sign = 1 if dec_str[0] == '+' else -1
    parts = dec_str[1:].split(':')
    deg = float(parts[0])
    minutes = float(parts[1])
    seconds = float(parts[2])
    return sign * (deg + minutes/60 + seconds/3600)
