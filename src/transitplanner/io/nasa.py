import pandas as pd
from importlib import resources

def load_nasa_data():
    """
    Instantly loads the NASA data bundled in the package data folder.
    """
    try:
        # This finds the file inside your src/transitplanner/data folder
        # even after the package is installed on another computer.
        data_path = resources.files('transitplanner.data').joinpath('nasa_data.parquet')
        
        with data_path.open("rb") as f:
            df = pd.read_parquet(f)
            
        # Ensure 'pl_name' is the index as your previous code expected
        if "pl_name" in df.columns:
            df.set_index("pl_name", inplace=True)
            
        return df
    except Exception as e:
        print(f"Critical Error: Could not load bundled NASA data. {e}")
        return None
