import pandas as pd

def dec_to_deg(dec_str):
    """
    Convert a declination string in sexagesimal format into decimal degrees.

    Input format is expected as sign degrees minutes seconds separated by colons.
    Example formats include plus or minus prefixes.

    This conversion is required because catalogue data may use string based
    coordinates while later filtering requires numeric comparisons.

    Parameters
    dec_str
    Declination string in sign deg min sec format

    Returns
    Declination value in decimal degrees
    """

    sign = 1 if dec_str[0] == '+' else -1
    parts = dec_str[1:].split(':')
    deg = float(parts[0])
    minutes = float(parts[1])
    seconds = float(parts[2])
    return sign * (deg + minutes/60 + seconds/3600)


# Choose nasa value unless missing, else exoclock
def choose(nasa_val, exo_val):

    """
    Select between NASA and ExoClock values using a priority rule.

    NASA values are preferred when available. If the NASA value is missing
    or NaN, the ExoClock value is used instead.

    This function ensures consistent parameter selection during catalogue
    merging without duplicating conditional logic.

    Parameters
    nasa_val
    Value retrieved from NASA Exoplanet Archive

    exo_val
    Value retrieved from ExoClock catalogue

    Returns
    Selected value following NASA first priority
    """

    if nasa_val is None:
        return exo_val
    if isinstance(nasa_val, float) and pd.isna(nasa_val):
        return exo_val
    return nasa_val


def enrich_planets(planet_list, exoclock_planets, nasa_df):
    """

    This function merges parameters from ExoClock and NASA for each planet
    already identified as geometrically visible. It also converts declination
    values into numeric degrees for later filtering.

    Parameters added include planet radius ratio, scaled semi major axis and
    orbital inclination.

    Parameters
    planet_list
    List of planet dictionaries from the visibility module

    exoclock_planets
    Dictionary of ExoClock planet data

    nasa_df
    DataFrame of NASA Exoplanet Archive parameters indexed by planet name

    Returns
    Updated planet list with merged parameters
    """

    for planet in planet_list:
        name = planet["Object"]

        exo = exoclock_planets.get(name, {})
        nasa_row = nasa_df.loc[name] if name in nasa_df.index else {}

        planet["Dec"] = dec_to_deg(planet["Dec"])
        planet["RpRs"] = choose(nasa_row.get("pl_ratror"),exo.get("rp_over_rs") )
        planet["aRs"] = choose( nasa_row.get("pl_ratdor"),exo.get("sma_over_rs"))
        planet["inclination"] = choose(nasa_row.get("pl_orbincl"),exo.get("inclination") )

    return planet_list
