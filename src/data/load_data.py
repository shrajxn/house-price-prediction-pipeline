from pathlib import Path
import pandas as pd 

def load_csv_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.
    """
    try:
        path = Path(file_path)
        df=pd.read_csv(path)
        print(f"Data loaded successfully from {file_path}")
        print(f"Data shape: {df.shape}") 
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
    