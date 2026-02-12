

from pathlib import Path
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive
import pickle

CACHE_FILE = Path.home() / ".transitplanner_nasa_cache.pkl"

def load_nasa_data():
    if CACHE_FILE.exists():
        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)

    table = NasaExoplanetArchive.query_criteria(
        table="pscomppars",
        select="pl_name,pl_orbper,pl_tranmid,pl_trandur",
        where="pl_tranflag=1"
    )

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(table, f)

    return table
