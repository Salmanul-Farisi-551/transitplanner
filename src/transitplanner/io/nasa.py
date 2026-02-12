from pathlib import Path
from astroquery.ipac.nexsci.nasa_exoplanet_archive import NasaExoplanetArchive
import pickle

CACHE_FILE = Path.home() / ".transitplanner_nasa_cache.pkl"

def load_nasa_data():
    if CACHE_FILE.exists():
        print("LOADING FROM CACHE")
        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)
            
    print("LOADING FROM NASA")
    table = NasaExoplanetArchive.query_criteria("pscomppars")
    df = table.to_pandas()
    df.set_index("pl_name", inplace=True)

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(df, f)

    return df


