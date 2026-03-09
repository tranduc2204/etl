import pandas as pd
from pathlib import Path

def ufn_reader_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        return df 
    except Exception as  e:
        print(f"error reading file: {e}")
if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parent.parent

    file_path = BASE_DIR / "data" / "customers.csv"
    df = ufn_reader_csv(file_path)
    print (df)