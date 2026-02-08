import pandas as pd

def dec_to_deg(dec_str):
    sign = 1 if dec_str[0] == '+' else -1
    parts = dec_str[1:].split(':')
    deg = float(parts[0])
    minutes = float(parts[1])
    seconds = float(parts[2])
    return sign * (deg + minutes/60 + seconds/3600)


# Choose nasa value unless missing, else exoclock
def choose(nasa_val, exo_val):
    if nasa_val is None:
        return exo_val
    if isinstance(nasa_val, float) and pd.isna(nasa_val):
        return exo_val
    return nasa_val


def enrich_planets(planet_list, exoclock_planets, nasa_df):
    for planet in planet_list:
        name = planet["Object"]

        exo = exoclock_planets.get(name, {})
        nasa_row = nasa_df.loc[name] if name in nasa_df.index else {}

        planet["Dec"] = dec_to_deg(planet["Dec"])
        planet["RpRs"] = choose(nasa_row.get("pl_ratror"),exo.get("rp_over_rs") )
        planet["aRs"] = choose( nasa_row.get("pl_ratdor"),exo.get("sma_over_rs"))
        planet["inclination"] = choose(nasa_row.get("pl_orbincl"),exo.get("inclination") )

    return planet_list
